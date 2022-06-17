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


class CustomerSelfCreateCompanyInformation(object):
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
        'address': 'str',
        'coordinates': 'object',
        'billing_information': 'object',
        'contact': 'object',
        'name': 'str'
    }

    attribute_map = {
        'address': 'address',
        'coordinates': 'coordinates',
        'billing_information': 'billing_information',
        'contact': 'contact',
        'name': 'name'
    }

    def __init__(self, address=None, coordinates=None, billing_information=None, contact=None, name=None, _configuration=None):  # noqa: E501
        """CustomerSelfCreateCompanyInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._coordinates = None
        self._billing_information = None
        self._contact = None
        self._name = None
        self.discriminator = None

        self.address = address
        if coordinates is not None:
            self.coordinates = coordinates
        self.billing_information = billing_information
        self.contact = contact
        self.name = name

    @property
    def address(self):
        """Gets the address of this CustomerSelfCreateCompanyInformation.  # noqa: E501

        Company Address  # noqa: E501

        :return: The address of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CustomerSelfCreateCompanyInformation.

        Company Address  # noqa: E501

        :param address: The address of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def coordinates(self):
        """Gets the coordinates of this CustomerSelfCreateCompanyInformation.  # noqa: E501

        Company Coordinates  # noqa: E501

        :return: The coordinates of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :rtype: object
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this CustomerSelfCreateCompanyInformation.

        Company Coordinates  # noqa: E501

        :param coordinates: The coordinates of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :type: object
        """

        self._coordinates = coordinates

    @property
    def billing_information(self):
        """Gets the billing_information of this CustomerSelfCreateCompanyInformation.  # noqa: E501

        Company billing information  # noqa: E501

        :return: The billing_information of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :rtype: object
        """
        return self._billing_information

    @billing_information.setter
    def billing_information(self, billing_information):
        """Sets the billing_information of this CustomerSelfCreateCompanyInformation.

        Company billing information  # noqa: E501

        :param billing_information: The billing_information of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and billing_information is None:
            raise ValueError("Invalid value for `billing_information`, must not be `None`")  # noqa: E501

        self._billing_information = billing_information

    @property
    def contact(self):
        """Gets the contact of this CustomerSelfCreateCompanyInformation.  # noqa: E501

        Company contact person  # noqa: E501

        :return: The contact of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :rtype: object
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this CustomerSelfCreateCompanyInformation.

        Company contact person  # noqa: E501

        :param contact: The contact of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and contact is None:
            raise ValueError("Invalid value for `contact`, must not be `None`")  # noqa: E501

        self._contact = contact

    @property
    def name(self):
        """Gets the name of this CustomerSelfCreateCompanyInformation.  # noqa: E501

        Company Name  # noqa: E501

        :return: The name of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerSelfCreateCompanyInformation.

        Company Name  # noqa: E501

        :param name: The name of this CustomerSelfCreateCompanyInformation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(CustomerSelfCreateCompanyInformation, dict):
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
        if not isinstance(other, CustomerSelfCreateCompanyInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerSelfCreateCompanyInformation):
            return True

        return self.to_dict() != other.to_dict()
