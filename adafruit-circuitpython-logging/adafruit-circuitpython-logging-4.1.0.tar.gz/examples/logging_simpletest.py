# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# pylint:disable=undefined-variable,wildcard-import,no-name-in-module
# pylint:disable=no-member,invalid-name

"""Briefly exercise the logger and null logger."""

import adafruit_logging as logging

# This should produce an error output

logger = logging.getLogger("test")
print_logger = logging.StreamHandler()
logger.addHandler(print_logger)

logger.setLevel(logging.ERROR)
logger.info("Info message")
logger.error("Error message")

# This should produce no output

null_logger = logging.getLogger("null")
null_handler = logging.NullHandler()
null_logger.addHandler(null_handler)

null_logger.setLevel(logging.ERROR)
null_logger.info("Info message")
null_logger.error("Error message")
