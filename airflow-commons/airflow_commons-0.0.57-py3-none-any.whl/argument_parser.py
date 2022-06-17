import argparse


class ParseKwargs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        """
        Overrides default argparse argument parser action.
        """
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split("=")
            getattr(namespace, self.dest)[key] = value
