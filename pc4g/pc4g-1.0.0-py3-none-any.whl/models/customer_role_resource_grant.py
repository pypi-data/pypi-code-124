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


class CustomerRoleResourceGrant(object):
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
        'grant_action': 'bool',
        'resource_type': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'grant_action': 'grant_action',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id'
    }

    def __init__(self, grant_action=None, resource_type=None, resource_id=None, _configuration=None):  # noqa: E501
        """CustomerRoleResourceGrant - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._grant_action = None
        self._resource_type = None
        self._resource_id = None
        self.discriminator = None

        if grant_action is not None:
            self.grant_action = grant_action
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def grant_action(self):
        """Gets the grant_action of this CustomerRoleResourceGrant.  # noqa: E501

        If True, grant access to the resource, if False revoke access from the resource  # noqa: E501

        :return: The grant_action of this CustomerRoleResourceGrant.  # noqa: E501
        :rtype: bool
        """
        return self._grant_action

    @grant_action.setter
    def grant_action(self, grant_action):
        """Sets the grant_action of this CustomerRoleResourceGrant.

        If True, grant access to the resource, if False revoke access from the resource  # noqa: E501

        :param grant_action: The grant_action of this CustomerRoleResourceGrant.  # noqa: E501
        :type: bool
        """

        self._grant_action = grant_action

    @property
    def resource_type(self):
        """Gets the resource_type of this CustomerRoleResourceGrant.  # noqa: E501

        Resource type  # noqa: E501

        :return: The resource_type of this CustomerRoleResourceGrant.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this CustomerRoleResourceGrant.

        Resource type  # noqa: E501

        :param resource_type: The resource_type of this CustomerRoleResourceGrant.  # noqa: E501
        :type: str
        """
        allowed_values = ["customer", "location", "cloudspace", "objectspace", "vm", "disk"]  # noqa: E501
        if (self._configuration.client_side_validation and
                resource_type not in allowed_values):
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this CustomerRoleResourceGrant.  # noqa: E501

                 Id of the resource. Not relevant for a customer role. For a location the location code needs to be used. For a virtual machine the id is formed by concatenating the vm cloudspace_id with the vm id separated by a colon (eg kjgkhjgkjhgk:45646 )  # noqa: E501

        :return: The resource_id of this CustomerRoleResourceGrant.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CustomerRoleResourceGrant.

                 Id of the resource. Not relevant for a customer role. For a location the location code needs to be used. For a virtual machine the id is formed by concatenating the vm cloudspace_id with the vm id separated by a colon (eg kjgkhjgkjhgk:45646 )  # noqa: E501

        :param resource_id: The resource_id of this CustomerRoleResourceGrant.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

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
        if issubclass(CustomerRoleResourceGrant, dict):
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
        if not isinstance(other, CustomerRoleResourceGrant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerRoleResourceGrant):
            return True

        return self.to_dict() != other.to_dict()
