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


class VmStatsModelSeriesVdiskIops(object):
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
        'disk_id': 'str',
        'iops': 'list[float]'
    }

    attribute_map = {
        'disk_id': 'disk_id',
        'iops': 'iops'
    }

    def __init__(self, disk_id=None, iops=None, _configuration=None):  # noqa: E501
        """VmStatsModelSeriesVdiskIops - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._disk_id = None
        self._iops = None
        self.discriminator = None

        if disk_id is not None:
            self.disk_id = disk_id
        if iops is not None:
            self.iops = iops

    @property
    def disk_id(self):
        """Gets the disk_id of this VmStatsModelSeriesVdiskIops.  # noqa: E501


        :return: The disk_id of this VmStatsModelSeriesVdiskIops.  # noqa: E501
        :rtype: str
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, disk_id):
        """Sets the disk_id of this VmStatsModelSeriesVdiskIops.


        :param disk_id: The disk_id of this VmStatsModelSeriesVdiskIops.  # noqa: E501
        :type: str
        """

        self._disk_id = disk_id

    @property
    def iops(self):
        """Gets the iops of this VmStatsModelSeriesVdiskIops.  # noqa: E501


        :return: The iops of this VmStatsModelSeriesVdiskIops.  # noqa: E501
        :rtype: list[float]
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this VmStatsModelSeriesVdiskIops.


        :param iops: The iops of this VmStatsModelSeriesVdiskIops.  # noqa: E501
        :type: list[float]
        """

        self._iops = iops

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
        if issubclass(VmStatsModelSeriesVdiskIops, dict):
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
        if not isinstance(other, VmStatsModelSeriesVdiskIops):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmStatsModelSeriesVdiskIops):
            return True

        return self.to_dict() != other.to_dict()
