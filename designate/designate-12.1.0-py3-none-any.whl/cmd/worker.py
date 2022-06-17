# Copyright 2016 Rackspace Inc.
#
# Author: Tim Simmons <tim.simmons@rackspace.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import sys

from oslo_log import log as logging
from oslo_reports import guru_meditation_report as gmr

import designate.conf
from designate import heartbeat_emitter
from designate import hookpoints
from designate import service
from designate import utils
from designate import version
from designate.worker import service as worker_service

LOG = logging.getLogger(__name__)
CONF = designate.conf.CONF
CONF.import_opt('workers', 'designate.worker', group='service:worker')


def main():
    utils.read_config('designate', sys.argv)
    logging.setup(CONF, 'designate')
    gmr.TextGuruMeditation.setup_autorun(version)

    hookpoints.log_hook_setup()

    server = worker_service.Service()
    heartbeat = heartbeat_emitter.get_heartbeat_emitter(server.service_name)
    service.serve(server, workers=CONF['service:worker'].workers)
    heartbeat.start()
    service.wait()
