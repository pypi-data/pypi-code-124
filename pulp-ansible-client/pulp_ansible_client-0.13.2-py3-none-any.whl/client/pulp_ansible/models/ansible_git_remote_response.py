# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_ansible.configuration import Configuration


class AnsibleGitRemoteResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sock_read_timeout': 'float',
        'pulp_created': 'datetime',
        'ca_cert': 'str',
        'connect_timeout': 'float',
        'pulp_last_updated': 'datetime',
        'pulp_href': 'str',
        'max_retries': 'int',
        'url': 'str',
        'download_concurrency': 'int',
        'sock_connect_timeout': 'float',
        'client_cert': 'str',
        'name': 'str',
        'pulp_labels': 'object',
        'rate_limit': 'int',
        'total_timeout': 'float',
        'tls_validation': 'bool',
        'headers': 'list[object]',
        'proxy_url': 'str',
        'metadata_only': 'bool',
        'git_ref': 'str'
    }

    attribute_map = {
        'sock_read_timeout': 'sock_read_timeout',
        'pulp_created': 'pulp_created',
        'ca_cert': 'ca_cert',
        'connect_timeout': 'connect_timeout',
        'pulp_last_updated': 'pulp_last_updated',
        'pulp_href': 'pulp_href',
        'max_retries': 'max_retries',
        'url': 'url',
        'download_concurrency': 'download_concurrency',
        'sock_connect_timeout': 'sock_connect_timeout',
        'client_cert': 'client_cert',
        'name': 'name',
        'pulp_labels': 'pulp_labels',
        'rate_limit': 'rate_limit',
        'total_timeout': 'total_timeout',
        'tls_validation': 'tls_validation',
        'headers': 'headers',
        'proxy_url': 'proxy_url',
        'metadata_only': 'metadata_only',
        'git_ref': 'git_ref'
    }

    def __init__(self, sock_read_timeout=None, pulp_created=None, ca_cert=None, connect_timeout=None, pulp_last_updated=None, pulp_href=None, max_retries=None, url=None, download_concurrency=None, sock_connect_timeout=None, client_cert=None, name=None, pulp_labels=None, rate_limit=None, total_timeout=None, tls_validation=None, headers=None, proxy_url=None, metadata_only=None, git_ref=None, local_vars_configuration=None):  # noqa: E501
        """AnsibleGitRemoteResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sock_read_timeout = None
        self._pulp_created = None
        self._ca_cert = None
        self._connect_timeout = None
        self._pulp_last_updated = None
        self._pulp_href = None
        self._max_retries = None
        self._url = None
        self._download_concurrency = None
        self._sock_connect_timeout = None
        self._client_cert = None
        self._name = None
        self._pulp_labels = None
        self._rate_limit = None
        self._total_timeout = None
        self._tls_validation = None
        self._headers = None
        self._proxy_url = None
        self._metadata_only = None
        self._git_ref = None
        self.discriminator = None

        self.sock_read_timeout = sock_read_timeout
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.ca_cert = ca_cert
        self.connect_timeout = connect_timeout
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        if pulp_href is not None:
            self.pulp_href = pulp_href
        self.max_retries = max_retries
        self.url = url
        self.download_concurrency = download_concurrency
        self.sock_connect_timeout = sock_connect_timeout
        self.client_cert = client_cert
        self.name = name
        if pulp_labels is not None:
            self.pulp_labels = pulp_labels
        self.rate_limit = rate_limit
        self.total_timeout = total_timeout
        if tls_validation is not None:
            self.tls_validation = tls_validation
        if headers is not None:
            self.headers = headers
        self.proxy_url = proxy_url
        if metadata_only is not None:
            self.metadata_only = metadata_only
        if git_ref is not None:
            self.git_ref = git_ref

    @property
    def sock_read_timeout(self):
        """Gets the sock_read_timeout of this AnsibleGitRemoteResponse.  # noqa: E501

        aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :return: The sock_read_timeout of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: float
        """
        return self._sock_read_timeout

    @sock_read_timeout.setter
    def sock_read_timeout(self, sock_read_timeout):
        """Sets the sock_read_timeout of this AnsibleGitRemoteResponse.

        aiohttp.ClientTimeout.sock_read (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :param sock_read_timeout: The sock_read_timeout of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                sock_read_timeout is not None and sock_read_timeout < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `sock_read_timeout`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._sock_read_timeout = sock_read_timeout

    @property
    def pulp_created(self):
        """Gets the pulp_created of this AnsibleGitRemoteResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this AnsibleGitRemoteResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def ca_cert(self):
        """Gets the ca_cert of this AnsibleGitRemoteResponse.  # noqa: E501

        A PEM encoded CA certificate used to validate the server certificate presented by the remote server.  # noqa: E501

        :return: The ca_cert of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this AnsibleGitRemoteResponse.

        A PEM encoded CA certificate used to validate the server certificate presented by the remote server.  # noqa: E501

        :param ca_cert: The ca_cert of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: str
        """

        self._ca_cert = ca_cert

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this AnsibleGitRemoteResponse.  # noqa: E501

        aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :return: The connect_timeout of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: float
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this AnsibleGitRemoteResponse.

        aiohttp.ClientTimeout.connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :param connect_timeout: The connect_timeout of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                connect_timeout is not None and connect_timeout < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `connect_timeout`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._connect_timeout = connect_timeout

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this AnsibleGitRemoteResponse.  # noqa: E501

        Timestamp of the most recent update of the remote.  # noqa: E501

        :return: The pulp_last_updated of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this AnsibleGitRemoteResponse.

        Timestamp of the most recent update of the remote.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def pulp_href(self):
        """Gets the pulp_href of this AnsibleGitRemoteResponse.  # noqa: E501


        :return: The pulp_href of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this AnsibleGitRemoteResponse.


        :param pulp_href: The pulp_href of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def max_retries(self):
        """Gets the max_retries of this AnsibleGitRemoteResponse.  # noqa: E501

        Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used.  # noqa: E501

        :return: The max_retries of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this AnsibleGitRemoteResponse.

        Maximum number of retry attempts after a download failure. If not set then the default value (3) will be used.  # noqa: E501

        :param max_retries: The max_retries of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: int
        """

        self._max_retries = max_retries

    @property
    def url(self):
        """Gets the url of this AnsibleGitRemoteResponse.  # noqa: E501

        The URL of an external content source.  # noqa: E501

        :return: The url of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AnsibleGitRemoteResponse.

        The URL of an external content source.  # noqa: E501

        :param url: The url of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def download_concurrency(self):
        """Gets the download_concurrency of this AnsibleGitRemoteResponse.  # noqa: E501

        Total number of simultaneous connections. If not set then the default value will be used.  # noqa: E501

        :return: The download_concurrency of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: int
        """
        return self._download_concurrency

    @download_concurrency.setter
    def download_concurrency(self, download_concurrency):
        """Sets the download_concurrency of this AnsibleGitRemoteResponse.

        Total number of simultaneous connections. If not set then the default value will be used.  # noqa: E501

        :param download_concurrency: The download_concurrency of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                download_concurrency is not None and download_concurrency < 1):  # noqa: E501
            raise ValueError("Invalid value for `download_concurrency`, must be a value greater than or equal to `1`")  # noqa: E501

        self._download_concurrency = download_concurrency

    @property
    def sock_connect_timeout(self):
        """Gets the sock_connect_timeout of this AnsibleGitRemoteResponse.  # noqa: E501

        aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :return: The sock_connect_timeout of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: float
        """
        return self._sock_connect_timeout

    @sock_connect_timeout.setter
    def sock_connect_timeout(self, sock_connect_timeout):
        """Sets the sock_connect_timeout of this AnsibleGitRemoteResponse.

        aiohttp.ClientTimeout.sock_connect (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :param sock_connect_timeout: The sock_connect_timeout of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                sock_connect_timeout is not None and sock_connect_timeout < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `sock_connect_timeout`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._sock_connect_timeout = sock_connect_timeout

    @property
    def client_cert(self):
        """Gets the client_cert of this AnsibleGitRemoteResponse.  # noqa: E501

        A PEM encoded client certificate used for authentication.  # noqa: E501

        :return: The client_cert of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_cert

    @client_cert.setter
    def client_cert(self, client_cert):
        """Sets the client_cert of this AnsibleGitRemoteResponse.

        A PEM encoded client certificate used for authentication.  # noqa: E501

        :param client_cert: The client_cert of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: str
        """

        self._client_cert = client_cert

    @property
    def name(self):
        """Gets the name of this AnsibleGitRemoteResponse.  # noqa: E501

        A unique name for this remote.  # noqa: E501

        :return: The name of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnsibleGitRemoteResponse.

        A unique name for this remote.  # noqa: E501

        :param name: The name of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def pulp_labels(self):
        """Gets the pulp_labels of this AnsibleGitRemoteResponse.  # noqa: E501


        :return: The pulp_labels of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: object
        """
        return self._pulp_labels

    @pulp_labels.setter
    def pulp_labels(self, pulp_labels):
        """Sets the pulp_labels of this AnsibleGitRemoteResponse.


        :param pulp_labels: The pulp_labels of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: object
        """

        self._pulp_labels = pulp_labels

    @property
    def rate_limit(self):
        """Gets the rate_limit of this AnsibleGitRemoteResponse.  # noqa: E501

        Limits requests per second for each concurrent downloader  # noqa: E501

        :return: The rate_limit of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """Sets the rate_limit of this AnsibleGitRemoteResponse.

        Limits requests per second for each concurrent downloader  # noqa: E501

        :param rate_limit: The rate_limit of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: int
        """

        self._rate_limit = rate_limit

    @property
    def total_timeout(self):
        """Gets the total_timeout of this AnsibleGitRemoteResponse.  # noqa: E501

        aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :return: The total_timeout of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_timeout

    @total_timeout.setter
    def total_timeout(self, total_timeout):
        """Sets the total_timeout of this AnsibleGitRemoteResponse.

        aiohttp.ClientTimeout.total (q.v.) for download-connections. The default is null, which will cause the default from the aiohttp library to be used.  # noqa: E501

        :param total_timeout: The total_timeout of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                total_timeout is not None and total_timeout < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `total_timeout`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._total_timeout = total_timeout

    @property
    def tls_validation(self):
        """Gets the tls_validation of this AnsibleGitRemoteResponse.  # noqa: E501

        If True, TLS peer validation must be performed.  # noqa: E501

        :return: The tls_validation of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: bool
        """
        return self._tls_validation

    @tls_validation.setter
    def tls_validation(self, tls_validation):
        """Sets the tls_validation of this AnsibleGitRemoteResponse.

        If True, TLS peer validation must be performed.  # noqa: E501

        :param tls_validation: The tls_validation of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: bool
        """

        self._tls_validation = tls_validation

    @property
    def headers(self):
        """Gets the headers of this AnsibleGitRemoteResponse.  # noqa: E501

        Headers for aiohttp.Clientsession  # noqa: E501

        :return: The headers of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this AnsibleGitRemoteResponse.

        Headers for aiohttp.Clientsession  # noqa: E501

        :param headers: The headers of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: list[object]
        """

        self._headers = headers

    @property
    def proxy_url(self):
        """Gets the proxy_url of this AnsibleGitRemoteResponse.  # noqa: E501

        The proxy URL. Format: scheme://host:port  # noqa: E501

        :return: The proxy_url of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this AnsibleGitRemoteResponse.

        The proxy URL. Format: scheme://host:port  # noqa: E501

        :param proxy_url: The proxy_url of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: str
        """

        self._proxy_url = proxy_url

    @property
    def metadata_only(self):
        """Gets the metadata_only of this AnsibleGitRemoteResponse.  # noqa: E501

        If True, only metadata about the content will be stored in Pulp. Clients will retrieve content from the remote URL.  # noqa: E501

        :return: The metadata_only of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: bool
        """
        return self._metadata_only

    @metadata_only.setter
    def metadata_only(self, metadata_only):
        """Sets the metadata_only of this AnsibleGitRemoteResponse.

        If True, only metadata about the content will be stored in Pulp. Clients will retrieve content from the remote URL.  # noqa: E501

        :param metadata_only: The metadata_only of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: bool
        """

        self._metadata_only = metadata_only

    @property
    def git_ref(self):
        """Gets the git_ref of this AnsibleGitRemoteResponse.  # noqa: E501

        A git ref. e.g.: branch, tag, or commit sha.  # noqa: E501

        :return: The git_ref of this AnsibleGitRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._git_ref

    @git_ref.setter
    def git_ref(self, git_ref):
        """Sets the git_ref of this AnsibleGitRemoteResponse.

        A git ref. e.g.: branch, tag, or commit sha.  # noqa: E501

        :param git_ref: The git_ref of this AnsibleGitRemoteResponse.  # noqa: E501
        :type: str
        """

        self._git_ref = git_ref

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnsibleGitRemoteResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnsibleGitRemoteResponse):
            return True

        return self.to_dict() != other.to_dict()
