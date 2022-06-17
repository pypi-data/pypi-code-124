"""
    Delphix DCT API

    Delphix DCT API  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from delphix.api.gateway.api_client import ApiClient, Endpoint as _Endpoint
from delphix.api.gateway.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from delphix.api.gateway.model.list_sources_response import ListSourcesResponse
from delphix.api.gateway.model.search_body import SearchBody
from delphix.api.gateway.model.search_sources_response import SearchSourcesResponse
from delphix.api.gateway.model.source import Source


class SourcesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_source_by_id(
            self,
            source_id,
            **kwargs
        ):
            """Get a source by ID.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_source_by_id(source_id, async_req=True)
            >>> result = thread.get()

            Args:
                source_id (str): The ID of the source.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Source
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['source_id'] = \
                source_id
            return self.call_with_http_info(**kwargs)

        self.get_source_by_id = _Endpoint(
            settings={
                'response_type': (Source,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/sources/{sourceId}',
                'operation_id': 'get_source_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'source_id',
                ],
                'required': [
                    'source_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'source_id',
                ]
            },
            root_map={
                'validations': {
                    ('source_id',): {

                        'min_length': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'source_id':
                        (str,),
                },
                'attribute_map': {
                    'source_id': 'sourceId',
                },
                'location_map': {
                    'source_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_source_by_id
        )

        def __get_sources(
            self,
            **kwargs
        ):
            """List all sources.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_sources(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                limit (int): Maximum number of objects to return per query. The value must be between 1 and 1000. Default is 100.. [optional] if omitted the server will use the default value of 100
                cursor (str): Cursor to fetch the next or previous page of results. The value of this property must be extracted from the 'prev_cursor' or 'next_cursor' property of a PaginatedResponseMetadata which is contained in the response of list and search API endpoints.. [optional]
                sort (str, none_type): The field to sort results by. A property name with a prepended '-' signifies descending order.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListSourcesResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_sources = _Endpoint(
            settings={
                'response_type': (ListSourcesResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/sources',
                'operation_id': 'get_sources',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                    'sort',
                ],
                'required': [],
                'nullable': [
                    'sort',
                ],
                'enum': [
                    'sort',
                ],
                'validation': [
                    'limit',
                    'cursor',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                    ('cursor',): {
                        'max_length': 4096,
                        'min_length': 1,
                    },
                },
                'allowed_values': {
                    ('sort',): {
                        'None': None,
                        "ID": "id",
                        "-ID": "-id",
                        "DATABASE_TYPE": "database_type",
                        "-DATABASE_TYPE": "-database_type",
                        "NAME": "name",
                        "-NAME": "-name",
                        "DATABASE_VERSION": "database_version",
                        "-DATABASE_VERSION": "-database_version",
                        "ENVIRONMENT_ID": "environment_id",
                        "-ENVIRONMENT_ID": "-environment_id",
                        "DATA_UUID": "data_uuid",
                        "-DATA_UUID": "-data_uuid",
                        "IP_ADDRESS": "ip_address",
                        "-IP_ADDRESS": "-ip_address",
                        "FQDN": "fqdn",
                        "-FQDN": "-fqdn",
                        "SIZE": "size",
                        "-SIZE": "-size",
                        "JDBC_CONNECTION_STRING": "jdbc_connection_string",
                        "-JDBC_CONNECTION_STRING": "-jdbc_connection_string",
                        "PLUGIN_VERSION": "plugin_version",
                        "-PLUGIN_VERSION": "-plugin_version"
                    },
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                    'sort':
                        (str, none_type,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                    'sort': 'sort',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_sources
        )

        def __search_sources(
            self,
            **kwargs
        ):
            """Search for Sources.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.search_sources(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                limit (int): Maximum number of objects to return per query. The value must be between 1 and 1000. Default is 100.. [optional] if omitted the server will use the default value of 100
                cursor (str): Cursor to fetch the next or previous page of results. The value of this property must be extracted from the 'prev_cursor' or 'next_cursor' property of a PaginatedResponseMetadata which is contained in the response of list and search API endpoints.. [optional]
                sort (str, none_type): The field to sort results by. A property name with a prepended '-' signifies descending order.. [optional]
                search_body (SearchBody): A request body containing a filter expression. This enables searching for items matching arbitrarily complex conditions. The list of attributes which can be used in filter expressions is available in the x-filterable vendor extension.  # Filter Expression Overview **Note: All keywords are case-insensitive**  ## Comparison Operators | Operator | Description | Example | | --- | --- | --- | | CONTAINS | Substring or membership testing for string and list attributes respectively. | field3 CONTAINS 'foobar', field4 CONTAINS TRUE  | | IN | Tests if field is a member of a list literal. List can contain a maximum of 100 values | field2 IN ['Goku', 'Vegeta'] | | GE | Tests if a field is greater than or equal to a literal value | field1 GE 1.2e-2 | | GT | Tests if a field is greater than a literal value | field1 GT 1.2e-2 | | LE | Tests if a field is less than or equal to a literal value | field1 LE 9000 | | LT | Tests if a field is less than a literal value | field1 LT 9.02 | | NE | Tests if a field is not equal to a literal value | field1 NE 42 | | EQ | Tests if a field is equal to a literal value | field1 EQ 42 |  ## Search Operator The SEARCH operator filters for items which have any filterable attribute that contains the input string as a substring, comparison is done case-insensitively. This is not restricted to attributes with string values. Specifically `SEARCH '12'` would match an item with an attribute with an integer value of `123`.  ## Logical Operators Ordered by precedence. | Operator | Description | Example | | --- | --- | --- | | NOT | Logical NOT (Right associative) | NOT field1 LE 9000 | | AND | Logical AND (Left Associative) | field1 GT 9000 AND field2 EQ 'Goku' | | OR | Logical OR (Left Associative) | field1 GT 9000 OR field2 EQ 'Goku' |  ## Grouping Parenthesis `()` can be used to override operator precedence.  For example: NOT (field1 LT 1234 AND field2 CONTAINS 'foo')  ## Literal Values | Literal      | Description | Examples | | --- | --- | --- | | Nil | Represents the absence of a value | nil, Nil, nIl, NIL | | Boolean | true/false boolean | true, false, True, False, TRUE, FALSE | | Number | Signed integer and floating point numbers. Also supports scientific notation. | 0, 1, -1, 1.2, 0.35, 1.2e-2, -1.2e+2 | | String | Single or double quoted | \"foo\", \"bar\", \"foo bar\", 'foo', 'bar', 'foo bar' | | Datetime | Formatted according to [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) | 2018-04-27T18:39:26.397237+00:00 | | List | Comma-separated literals wrapped in square brackets | [0], [0, 1], ['foo', \"bar\"] |  ## Limitations - A maximum of 8 unique identifiers may be used inside a filter expression. . [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SearchSourcesResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.search_sources = _Endpoint(
            settings={
                'response_type': (SearchSourcesResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/sources/search',
                'operation_id': 'search_sources',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                    'sort',
                    'search_body',
                ],
                'required': [],
                'nullable': [
                    'sort',
                ],
                'enum': [
                    'sort',
                ],
                'validation': [
                    'limit',
                    'cursor',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                    ('cursor',): {
                        'max_length': 4096,
                        'min_length': 1,
                    },
                },
                'allowed_values': {
                    ('sort',): {
                        'None': None,
                        "ID": "id",
                        "-ID": "-id",
                        "DATABASE_TYPE": "database_type",
                        "-DATABASE_TYPE": "-database_type",
                        "NAME": "name",
                        "-NAME": "-name",
                        "DATABASE_VERSION": "database_version",
                        "-DATABASE_VERSION": "-database_version",
                        "ENVIRONMENT_ID": "environment_id",
                        "-ENVIRONMENT_ID": "-environment_id",
                        "DATA_UUID": "data_uuid",
                        "-DATA_UUID": "-data_uuid",
                        "IP_ADDRESS": "ip_address",
                        "-IP_ADDRESS": "-ip_address",
                        "FQDN": "fqdn",
                        "-FQDN": "-fqdn",
                        "SIZE": "size",
                        "-SIZE": "-size",
                        "JDBC_CONNECTION_STRING": "jdbc_connection_string",
                        "-JDBC_CONNECTION_STRING": "-jdbc_connection_string",
                        "PLUGIN_VERSION": "plugin_version",
                        "-PLUGIN_VERSION": "-plugin_version"
                    },
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                    'sort':
                        (str, none_type,),
                    'search_body':
                        (SearchBody,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                    'sort': 'sort',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
                    'sort': 'query',
                    'search_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__search_sources
        )
