"""
    Delphix DCT API

    Delphix DCT API  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import delphix.api.gateway
from delphix.api.gateway.model.paginated_response_metadata import PaginatedResponseMetadata
from delphix.api.gateway.model.registered_engine import RegisteredEngine
globals()['PaginatedResponseMetadata'] = PaginatedResponseMetadata
globals()['RegisteredEngine'] = RegisteredEngine
from delphix.api.gateway.model.search_engines_response import SearchEnginesResponse


class TestSearchEnginesResponse(unittest.TestCase):
    """SearchEnginesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchEnginesResponse(self):
        """Test SearchEnginesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchEnginesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
