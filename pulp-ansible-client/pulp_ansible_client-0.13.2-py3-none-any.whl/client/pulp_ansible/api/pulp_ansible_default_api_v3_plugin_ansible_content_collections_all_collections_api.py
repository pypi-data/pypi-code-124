# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_ansible.api_client import ApiClient
from pulpcore.client.pulp_ansible.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PulpAnsibleDefaultApiV3PluginAnsibleContentCollectionsAllCollectionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list(self, distro_base_path, **kwargs):  # noqa: E501
        """list  # noqa: E501

        Unpaginated ViewSet for Collections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(distro_base_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str distro_base_path: (required)
        :param bool deprecated:
        :param str name:
        :param str namespace:
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[CollectionResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(distro_base_path, **kwargs)  # noqa: E501

    def list_with_http_info(self, distro_base_path, **kwargs):  # noqa: E501
        """list  # noqa: E501

        Unpaginated ViewSet for Collections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(distro_base_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str distro_base_path: (required)
        :param bool deprecated:
        :param str name:
        :param str namespace:
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[CollectionResponse], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'distro_base_path',
            'deprecated',
            'name',
            'namespace',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'distro_base_path' is set
        if self.api_client.client_side_validation and ('distro_base_path' not in local_var_params or  # noqa: E501
                                                        local_var_params['distro_base_path'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `distro_base_path` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'distro_base_path' in local_var_params:
            path_params['distro_base_path'] = local_var_params['distro_base_path']  # noqa: E501

        query_params = []
        if 'deprecated' in local_var_params and local_var_params['deprecated'] is not None:  # noqa: E501
            query_params.append(('deprecated', local_var_params['deprecated']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'namespace' in local_var_params and local_var_params['namespace'] is not None:  # noqa: E501
            query_params.append(('namespace', local_var_params['namespace']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pulp_ansible/galaxy/default/api/v3/plugin/ansible/content/{distro_base_path}/collections/all-collections/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CollectionResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
