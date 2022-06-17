import argparse
from ewokscore import cliutils


def test_cli_execute_workflow():
    parser = argparse.ArgumentParser()
    cliutils.add_execute_parameters(parser)
    argv = ["acyclic1", "--test", "-p", "a=1", "-p", "task1:b=test"]
    args, _ = parser.parse_known_args(argv)
    cliutils.apply_execute_parameters(args)

    assert args.graph["graph"]["id"] == "acyclic1"

    execute_options = {
        "inputs": [
            {"name": "a", "value": 1},
            {"label": "task1", "name": "b", "value": "test"},
        ],
        "merge_outputs": False,
        "outputs": [],
        "varinfo": {"root_uri": "", "scheme": "nexus"},
        "load_options": {"root_dir": ""},
        "execinfo": {},
    }
    assert args.execute_options == execute_options


def test_cli_convert_workflow():
    parser = argparse.ArgumentParser()
    cliutils.add_convert_parameters(parser)
    argv = [
        "acyclic1",
        "test.json",
        "--test",
        "-p",
        "a=1",
        "-p",
        "task1:b=test",
        "--src-format",
        "yaml",
        "--dst-format",
        "json",
    ]
    args, _ = parser.parse_known_args(argv)
    cliutils.apply_convert_parameters(args)

    assert args.graph["graph"]["id"] == "acyclic1"

    convert_options = {
        "inputs": [
            {"name": "a", "value": 1},
            {"label": "task1", "name": "b", "value": "test"},
        ],
        "load_options": {"representation": "yaml"},
        "save_options": {"representation": "json"},
    }
    assert args.convert_options == convert_options
