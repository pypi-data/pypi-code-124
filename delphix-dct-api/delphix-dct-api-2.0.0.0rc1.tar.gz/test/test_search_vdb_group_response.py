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
from delphix.api.gateway.model.vdb_group import VDBGroup
globals()['PaginatedResponseMetadata'] = PaginatedResponseMetadata
globals()['VDBGroup'] = VDBGroup
from delphix.api.gateway.model.search_vdb_group_response import SearchVDBGroupResponse


class TestSearchVDBGroupResponse(unittest.TestCase):
    """SearchVDBGroupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchVDBGroupResponse(self):
        """Test SearchVDBGroupResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchVDBGroupResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
