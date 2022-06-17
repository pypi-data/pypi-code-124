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


class CustomerSelfCreate(object):
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
        'company_information': 'object',
        'external_customer_id': 'str'
    }

    attribute_map = {
        'company_information': 'company_information',
        'external_customer_id': 'external_customer_id'
    }

    def __init__(self, company_information=None, external_customer_id=None, _configuration=None):  # noqa: E501
        """CustomerSelfCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._company_information = None
        self._external_customer_id = None
        self.discriminator = None

        self.company_information = company_information
        if external_customer_id is not None:
            self.external_customer_id = external_customer_id

    @property
    def company_information(self):
        """Gets the company_information of this CustomerSelfCreate.  # noqa: E501

        Company Information  # noqa: E501

        :return: The company_information of this CustomerSelfCreate.  # noqa: E501
        :rtype: object
        """
        return self._company_information

    @company_information.setter
    def company_information(self, company_information):
        """Sets the company_information of this CustomerSelfCreate.

        Company Information  # noqa: E501

        :param company_information: The company_information of this CustomerSelfCreate.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and company_information is None:
            raise ValueError("Invalid value for `company_information`, must not be `None`")  # noqa: E501

        self._company_information = company_information

    @property
    def external_customer_id(self):
        """Gets the external_customer_id of this CustomerSelfCreate.  # noqa: E501

        Reference to this customer in an external system  # noqa: E501

        :return: The external_customer_id of this CustomerSelfCreate.  # noqa: E501
        :rtype: str
        """
        return self._external_customer_id

    @external_customer_id.setter
    def external_customer_id(self, external_customer_id):
        """Sets the external_customer_id of this CustomerSelfCreate.

        Reference to this customer in an external system  # noqa: E501

        :param external_customer_id: The external_customer_id of this CustomerSelfCreate.  # noqa: E501
        :type: str
        """

        self._external_customer_id = external_customer_id

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
        if issubclass(CustomerSelfCreate, dict):
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
        if not isinstance(other, CustomerSelfCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerSelfCreate):
            return True

        return self.to_dict() != other.to_dict()
