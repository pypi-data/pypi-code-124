# coding: utf-8

"""
    Python client for GIG based clouds (pc4g)

    RESTful api client to a GIG based cloud.  # noqa: E501

    OpenAPI spec version: v1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pc4g.configuration import Configuration


class ExternalNICSElement(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_network_id': 'int',
        'ip_address': 'str'
    }

    attribute_map = {
        'external_network_id': 'external_network_id',
        'ip_address': 'ip_address'
    }

    def __init__(self, external_network_id=None, ip_address=None, _configuration=None):  # noqa: E501
        """ExternalNICSElement - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._external_network_id = None
        self._ip_address = None
        self.discriminator = None

        if external_network_id is not None:
            self.external_network_id = external_network_id
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def external_network_id(self):
        """Gets the external_network_id of this ExternalNICSElement.  # noqa: E501

        External Network ID  # noqa: E501

        :return: The external_network_id of this ExternalNICSElement.  # noqa: E501
        :rtype: int
        """
        return self._external_network_id

    @external_network_id.setter
    def external_network_id(self, external_network_id):
        """Sets the external_network_id of this ExternalNICSElement.

        External Network ID  # noqa: E501

        :param external_network_id: The external_network_id of this ExternalNICSElement.  # noqa: E501
        :type: int
        """

        self._external_network_id = external_network_id

    @property
    def ip_address(self):
        """Gets the ip_address of this ExternalNICSElement.  # noqa: E501

        IP Address  # noqa: E501

        :return: The ip_address of this ExternalNICSElement.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ExternalNICSElement.

        IP Address  # noqa: E501

        :param ip_address: The ip_address of this ExternalNICSElement.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ExternalNICSElement, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalNICSElement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalNICSElement):
            return True

        return self.to_dict() != other.to_dict()
