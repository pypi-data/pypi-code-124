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


class AccountConsumptionModelCloudspacesVms(object):
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
        'vm_id': 'int',
        'name': 'str',
        'consumption': 'AccountConsumptionModelCloudspacesVmsConsumption'
    }

    attribute_map = {
        'vm_id': 'vm_id',
        'name': 'name',
        'consumption': 'consumption'
    }

    def __init__(self, vm_id=None, name=None, consumption=None, _configuration=None):  # noqa: E501
        """AccountConsumptionModelCloudspacesVms - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vm_id = None
        self._name = None
        self._consumption = None
        self.discriminator = None

        if vm_id is not None:
            self.vm_id = vm_id
        if name is not None:
            self.name = name
        if consumption is not None:
            self.consumption = consumption

    @property
    def vm_id(self):
        """Gets the vm_id of this AccountConsumptionModelCloudspacesVms.  # noqa: E501


        :return: The vm_id of this AccountConsumptionModelCloudspacesVms.  # noqa: E501
        :rtype: int
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this AccountConsumptionModelCloudspacesVms.


        :param vm_id: The vm_id of this AccountConsumptionModelCloudspacesVms.  # noqa: E501
        :type: int
        """

        self._vm_id = vm_id

    @property
    def name(self):
        """Gets the name of this AccountConsumptionModelCloudspacesVms.  # noqa: E501


        :return: The name of this AccountConsumptionModelCloudspacesVms.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountConsumptionModelCloudspacesVms.


        :param name: The name of this AccountConsumptionModelCloudspacesVms.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def consumption(self):
        """Gets the consumption of this AccountConsumptionModelCloudspacesVms.  # noqa: E501


        :return: The consumption of this AccountConsumptionModelCloudspacesVms.  # noqa: E501
        :rtype: AccountConsumptionModelCloudspacesVmsConsumption
        """
        return self._consumption

    @consumption.setter
    def consumption(self, consumption):
        """Sets the consumption of this AccountConsumptionModelCloudspacesVms.


        :param consumption: The consumption of this AccountConsumptionModelCloudspacesVms.  # noqa: E501
        :type: AccountConsumptionModelCloudspacesVmsConsumption
        """

        self._consumption = consumption

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
        if issubclass(AccountConsumptionModelCloudspacesVms, dict):
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
        if not isinstance(other, AccountConsumptionModelCloudspacesVms):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountConsumptionModelCloudspacesVms):
            return True

        return self.to_dict() != other.to_dict()
