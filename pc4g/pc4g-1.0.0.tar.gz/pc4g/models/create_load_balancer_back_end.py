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


class CreateLoadBalancerBackEnd(object):
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
        'serverpool_id': 'str',
        'target_port': 'int'
    }

    attribute_map = {
        'serverpool_id': 'serverpool_id',
        'target_port': 'target_port'
    }

    def __init__(self, serverpool_id=None, target_port=None, _configuration=None):  # noqa: E501
        """CreateLoadBalancerBackEnd - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._serverpool_id = None
        self._target_port = None
        self.discriminator = None

        self.serverpool_id = serverpool_id
        self.target_port = target_port

    @property
    def serverpool_id(self):
        """Gets the serverpool_id of this CreateLoadBalancerBackEnd.  # noqa: E501

        Server pool ID  # noqa: E501

        :return: The serverpool_id of this CreateLoadBalancerBackEnd.  # noqa: E501
        :rtype: str
        """
        return self._serverpool_id

    @serverpool_id.setter
    def serverpool_id(self, serverpool_id):
        """Sets the serverpool_id of this CreateLoadBalancerBackEnd.

        Server pool ID  # noqa: E501

        :param serverpool_id: The serverpool_id of this CreateLoadBalancerBackEnd.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and serverpool_id is None:
            raise ValueError("Invalid value for `serverpool_id`, must not be `None`")  # noqa: E501

        self._serverpool_id = serverpool_id

    @property
    def target_port(self):
        """Gets the target_port of this CreateLoadBalancerBackEnd.  # noqa: E501

        Port used in the VM that load balancer will forward requests to  # noqa: E501

        :return: The target_port of this CreateLoadBalancerBackEnd.  # noqa: E501
        :rtype: int
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """Sets the target_port of this CreateLoadBalancerBackEnd.

        Port used in the VM that load balancer will forward requests to  # noqa: E501

        :param target_port: The target_port of this CreateLoadBalancerBackEnd.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and target_port is None:
            raise ValueError("Invalid value for `target_port`, must not be `None`")  # noqa: E501

        self._target_port = target_port

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
        if issubclass(CreateLoadBalancerBackEnd, dict):
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
        if not isinstance(other, CreateLoadBalancerBackEnd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLoadBalancerBackEnd):
            return True

        return self.to_dict() != other.to_dict()
