from __future__ import absolute_import
import argparse
import logging
import logging.config

import docker
import multiprocessing.pool
import os
import psutil
import random
import shutil
import sys
import traceback

from ann_benchmarks.datasets import get_dataset, DATASETS
from ann_benchmarks.constants import INDEX_DIR
from ann_benchmarks.algorithms.definitions import (get_definitions,
                                                   list_algorithms,
                                                   algorithm_status,
                                                   InstantiationStatus)
from ann_benchmarks.results import get_result_filename
from ann_benchmarks.runner import run, run_docker


def positive_int(s):
    i = None
    try:
        i = int(s)
    except ValueError:
        pass
    if not i or i < 1:
        raise argparse.ArgumentTypeError("%r is not a positive integer" % s)
    return i


def run_worker(cpu, args, queue):
    while not queue.empty():
        definition = queue.get()
        if args.local:
            run(definition, args.dataset, args.count, args.runs, args.batch,
                args.build_only, args.test_only, args.total_clients, args.client_id)
        else:
            memory_margin = 500e6  # reserve some extra memory for misc stuff
            mem_limit = int((psutil.virtual_memory().available - memory_margin) / args.parallelism)
            cpu_limit = str(cpu)
            if args.batch:
                cpu_limit = "0-%d" % (multiprocessing.cpu_count() - 1)

            run_docker(definition, args.dataset, args.count,
                       args.runs, args.timeout, args.batch, cpu_limit, mem_limit)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--dataset',
        metavar='NAME',
        help='the dataset to load training points from',
        default='glove-100-angular',
        choices=DATASETS.keys())
    parser.add_argument(
        "-k", "--count",
        default=10,
        type=positive_int,
        help="the number of near neighbours to search for")
    parser.add_argument(
        '--definitions',
        metavar='FILE',
        help='load algorithm definitions from FILE',
        default='algos.yaml')
    parser.add_argument(
        '--algorithm',
        metavar='NAME',
        help='run only the named algorithm',
        default=None)
    parser.add_argument(
        '--run-group',
        metavar='NAME',
        help='run only the named run group',
        default=None)
    parser.add_argument(
        '--docker-tag',
        metavar='NAME',
        help='run only algorithms in a particular docker image',
        default=None)
    parser.add_argument(
        '--list-algorithms',
        help='print the names of all known algorithms and exit',
        action='store_true')
    parser.add_argument(
        '--force',
        help='re-run algorithms even if their results already exist',
        action='store_true')
    parser.add_argument(
        '--runs',
        metavar='COUNT',
        type=positive_int,
        help='run each algorithm instance %(metavar)s times and use only'
             ' the best result',
        default=5)
    parser.add_argument(
        '--timeout',
        type=int,
        help='Timeout (in seconds) for each individual algorithm run, or -1'
             'if no timeout should be set',
        default=2 * 3600)
    parser.add_argument(
        '--local',
        action='store_true',
        help='If set, then will run everything locally (inside the same '
             'process) rather than using Docker')
    parser.add_argument(
        '--batch',
        action='store_true',
        help='If set, algorithms get all queries at once')
    parser.add_argument(
        '--max-n-algorithms',
        type=int,
        help='Max number of algorithms to run (just used for testing)',
        default=-1)
    parser.add_argument(
        '--run-disabled',
        help='run algorithms that are disabled in algos.yml',
        action='store_true')
    parser.add_argument(
        '--parallelism',
        type=positive_int,
        help='Number of Docker containers in parallel',
        default=1)
    parser.add_argument(
        '--build-only',
        action='store_true',
        help='building index only, not testing with queries')
    parser.add_argument(
        '--test-only',
        action='store_true',
        help='querying index only, not building it (should be built first)')
    parser.add_argument(
        '--cluster',
        action='store_true',
        help='working with a cluster')
    parser.add_argument(
        '--host',
        metavar='NAME',
        help='host name or IP',
        default=None)
    parser.add_argument(
        '--port',
        type=positive_int,
        help='the port "host" is listening on',
        default=None)
    parser.add_argument(
        '--auth', '-a',
        metavar='PASSWORD',
        help='password for connection',
        default=None)
    parser.add_argument(
        '--user',
        metavar='NAME',
        help='user name for connection',
        default=None)
    parser.add_argument(
        '--total-clients',
        metavar='NUM',
        type=positive_int,
        help='total number of clients running in parallel',
        default=1)
    parser.add_argument(
        '--client-id',
        metavar='NUM',
        type=positive_int,
        help='specific client id (among the total clients)',
        default=1)
    parser.add_argument(
        '--shards',
        type=str,
        metavar='NUM',
        default="1",
        help='specify number of shards')

    args = parser.parse_args()
    if args.timeout == -1:
        args.timeout = None

    if args.list_algorithms:
        list_algorithms(args.definitions)
        sys.exit(0)
    
    if args.build_only and args.test_only:
        raise Exception('Nothing to run (build only and test only was specified)')
    if (args.build_only or args.test_only) and not args.local:
        raise Exception('Can\'t run build or test only on docker')

    conn_params = {'host': args.host, 'port': args.port, 'auth': args.auth, 'user': args.user, 'cluster': args.cluster, 'shards': args.shards}

    if args.total_clients < args.client_id:
        raise Exception('must satisfy 1 <= client_id <= total_clients')

    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("annb")

    # Nmslib specific code
    # Remove old indices stored on disk
    if os.path.exists(INDEX_DIR):
        shutil.rmtree(INDEX_DIR)

    dataset, dimension = get_dataset(args.dataset)
    point_type = dataset.attrs.get('point_type', 'float')
    distance = dataset.attrs['distance']
    definitions = get_definitions(
        args.definitions, dimension, point_type, distance, args.count, conn_params)

    # Filter out, from the loaded definitions, all those query argument groups
    # that correspond to experiments that have already been run. (This might
    # mean removing a definition altogether, so we can't just use a list
    # comprehension.)
    filtered_definitions = []
    for definition in definitions:
        query_argument_groups = definition.query_argument_groups
        if not query_argument_groups:
            query_argument_groups = [[]]
        not_yet_run = []
        for query_arguments in query_argument_groups:
            fn = get_result_filename(args.dataset,
                                     args.count, definition,
                                     query_arguments, args.batch)
            if args.force or not os.path.exists(fn):
                not_yet_run.append(query_arguments)
        if not_yet_run:
            if definition.query_argument_groups:
                definition = definition._replace(
                    query_argument_groups=not_yet_run)
            filtered_definitions.append(definition)
    definitions = filtered_definitions

    random.shuffle(definitions)

    if args.algorithm:
        logger.info(f'running only {args.algorithm} algorithms')
        definitions = [d for d in definitions if d.algorithm == args.algorithm]

    if args.run_group:
        logger.info(f'running only {args.run_group} run groups')
        definitions = [d for d in definitions if d.run_group == args.run_group]

    if not args.local:
        # See which Docker images we have available
        docker_client = docker.from_env()
        docker_tags = set()
        for image in docker_client.images.list():
            for tag in image.tags:
                tag = tag.split(':')[0]
                docker_tags.add(tag)

        if args.docker_tag:
            logger.info(f'running only {args.docker_tag}')
            definitions = [
                d for d in definitions if d.docker_tag == args.docker_tag]

        if set(d.docker_tag for d in definitions).difference(docker_tags):
            logger.info(f'not all docker images available, only: {set(docker_tags)}')
            logger.info(f'missing docker images: '
                        f'{str(set(d.docker_tag for d in definitions).difference(docker_tags))}')
            definitions = [
                d for d in definitions if d.docker_tag in docker_tags]
    else:
        def _test(df):
            status = algorithm_status(df)
            # If the module was loaded but doesn't actually have a constructor
            # of the right name, then the definition is broken
            if status == InstantiationStatus.NO_CONSTRUCTOR:
                raise Exception("%s.%s(%s): error: the module '%s' does not"
                                " expose the named constructor" % (
                                    df.module, df.constructor,
                                    df.arguments, df.module))

            if status == InstantiationStatus.NO_MODULE:
                # If the module couldn't be loaded (presumably because
                # of a missing dependency), print a warning and remove
                # this definition from the list of things to be run
                logging.warning("%s.%s(%s): the module '%s' could not be "
                      "loaded; skipping" % (df.module, df.constructor,
                                            df.arguments, df.module))
                return False
            else:
                return True
        definitions = [d for d in definitions if _test(d)]

    if not args.run_disabled:
        if len([d for d in definitions if d.disabled]):
            logger.info(f'Not running disabled algorithms {[d for d in definitions if d.disabled]}')
        definitions = [d for d in definitions if not d.disabled]

    if args.max_n_algorithms >= 0:
        definitions = definitions[:args.max_n_algorithms]

    if len(definitions) == 0:
        raise Exception('Nothing to run')
    else:
        logger.info(f'Order: {definitions}')

    if args.parallelism > multiprocessing.cpu_count() - 1:
        raise Exception('Parallelism larger than %d! (CPU count minus one)' % (multiprocessing.cpu_count() - 1))

    # Multiprocessing magic to farm this out to all CPUs
    queue = multiprocessing.Queue()
    for definition in definitions:
        queue.put(definition)
    if args.batch and args.parallelism > 1:
        raise Exception(f"Batch mode uses all available CPU resources, --parallelism should be set to 1. (Was: {args.parallelism})")
    workers = [multiprocessing.Process(target=run_worker, args=(i+1, args, queue))
               for i in range(args.parallelism)]
    [worker.start() for worker in workers]
    [worker.join() for worker in workers]

    # TODO: need to figure out cleanup handling here
