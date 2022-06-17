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


class VmConsumptionTsModelVm(object):
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
        'timestamp': 'int',
        'data': 'VmConsumptionTsModelVmData'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'data': 'data'
    }

    def __init__(self, timestamp=None, data=None, _configuration=None):  # noqa: E501
        """VmConsumptionTsModelVm - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._timestamp = None
        self._data = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if data is not None:
            self.data = data

    @property
    def timestamp(self):
        """Gets the timestamp of this VmConsumptionTsModelVm.  # noqa: E501


        :return: The timestamp of this VmConsumptionTsModelVm.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VmConsumptionTsModelVm.


        :param timestamp: The timestamp of this VmConsumptionTsModelVm.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def data(self):
        """Gets the data of this VmConsumptionTsModelVm.  # noqa: E501


        :return: The data of this VmConsumptionTsModelVm.  # noqa: E501
        :rtype: VmConsumptionTsModelVmData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VmConsumptionTsModelVm.


        :param data: The data of this VmConsumptionTsModelVm.  # noqa: E501
        :type: VmConsumptionTsModelVmData
        """

        self._data = data

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
        if issubclass(VmConsumptionTsModelVm, dict):
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
        if not isinstance(other, VmConsumptionTsModelVm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmConsumptionTsModelVm):
            return True

        return self.to_dict() != other.to_dict()
