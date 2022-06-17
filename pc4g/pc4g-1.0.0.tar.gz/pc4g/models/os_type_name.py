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


class OSTypeName(object):
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
        'os_type': 'str',
        'os_names': 'list[str]'
    }

    attribute_map = {
        'os_type': 'os_type',
        'os_names': 'os_names'
    }

    def __init__(self, os_type=None, os_names=None, _configuration=None):  # noqa: E501
        """OSTypeName - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._os_type = None
        self._os_names = None
        self.discriminator = None

        if os_type is not None:
            self.os_type = os_type
        if os_names is not None:
            self.os_names = os_names

    @property
    def os_type(self):
        """Gets the os_type of this OSTypeName.  # noqa: E501


        :return: The os_type of this OSTypeName.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this OSTypeName.


        :param os_type: The os_type of this OSTypeName.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def os_names(self):
        """Gets the os_names of this OSTypeName.  # noqa: E501


        :return: The os_names of this OSTypeName.  # noqa: E501
        :rtype: list[str]
        """
        return self._os_names

    @os_names.setter
    def os_names(self, os_names):
        """Sets the os_names of this OSTypeName.


        :param os_names: The os_names of this OSTypeName.  # noqa: E501
        :type: list[str]
        """

        self._os_names = os_names

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
        if issubclass(OSTypeName, dict):
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
        if not isinstance(other, OSTypeName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OSTypeName):
            return True

        return self.to_dict() != other.to_dict()
