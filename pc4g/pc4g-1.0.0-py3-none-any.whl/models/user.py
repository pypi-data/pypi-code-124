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


class User(object):
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
        'username': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'email': 'str',
        'emails': 'list[str]',
        'is_admin': 'bool',
        'iam_domain': 'str',
        'vco_website': 'str',
        'vco_name': 'str',
        'vco_support_email': 'str',
        'customers': 'list[UserCustomer]',
        'admin_of_customers': 'list[UserCustomer]'
    }

    attribute_map = {
        'username': 'username',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'email': 'email',
        'emails': 'emails',
        'is_admin': 'is_admin',
        'iam_domain': 'iam_domain',
        'vco_website': 'vco_website',
        'vco_name': 'vco_name',
        'vco_support_email': 'vco_support_email',
        'customers': 'customers',
        'admin_of_customers': 'admin_of_customers'
    }

    def __init__(self, username=None, firstname=None, lastname=None, email=None, emails=None, is_admin=None, iam_domain=None, vco_website=None, vco_name=None, vco_support_email=None, customers=None, admin_of_customers=None, _configuration=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._username = None
        self._firstname = None
        self._lastname = None
        self._email = None
        self._emails = None
        self._is_admin = None
        self._iam_domain = None
        self._vco_website = None
        self._vco_name = None
        self._vco_support_email = None
        self._customers = None
        self._admin_of_customers = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if email is not None:
            self.email = email
        if emails is not None:
            self.emails = emails
        if is_admin is not None:
            self.is_admin = is_admin
        if iam_domain is not None:
            self.iam_domain = iam_domain
        if vco_website is not None:
            self.vco_website = vco_website
        if vco_name is not None:
            self.vco_name = vco_name
        if vco_support_email is not None:
            self.vco_support_email = vco_support_email
        if customers is not None:
            self.customers = customers
        if admin_of_customers is not None:
            self.admin_of_customers = admin_of_customers

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501

        The username of the user  # noqa: E501

        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        The username of the user  # noqa: E501

        :param username: The username of this User.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def firstname(self):
        """Gets the firstname of this User.  # noqa: E501

        User's first name  # noqa: E501

        :return: The firstname of this User.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this User.

        User's first name  # noqa: E501

        :param firstname: The firstname of this User.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this User.  # noqa: E501

        User's last name  # noqa: E501

        :return: The lastname of this User.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this User.

        User's last name  # noqa: E501

        :param lastname: The lastname of this User.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        User's email  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        User's email  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def emails(self):
        """Gets the emails of this User.  # noqa: E501

        User's list of validated emails  # noqa: E501

        :return: The emails of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this User.

        User's list of validated emails  # noqa: E501

        :param emails: The emails of this User.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def is_admin(self):
        """Gets the is_admin of this User.  # noqa: E501

        is user admin or not  # noqa: E501

        :return: The is_admin of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this User.

        is user admin or not  # noqa: E501

        :param is_admin: The is_admin of this User.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def iam_domain(self):
        """Gets the iam_domain of this User.  # noqa: E501

        IAM domain  # noqa: E501

        :return: The iam_domain of this User.  # noqa: E501
        :rtype: str
        """
        return self._iam_domain

    @iam_domain.setter
    def iam_domain(self, iam_domain):
        """Sets the iam_domain of this User.

        IAM domain  # noqa: E501

        :param iam_domain: The iam_domain of this User.  # noqa: E501
        :type: str
        """

        self._iam_domain = iam_domain

    @property
    def vco_website(self):
        """Gets the vco_website of this User.  # noqa: E501

        Website  # noqa: E501

        :return: The vco_website of this User.  # noqa: E501
        :rtype: str
        """
        return self._vco_website

    @vco_website.setter
    def vco_website(self, vco_website):
        """Sets the vco_website of this User.

        Website  # noqa: E501

        :param vco_website: The vco_website of this User.  # noqa: E501
        :type: str
        """

        self._vco_website = vco_website

    @property
    def vco_name(self):
        """Gets the vco_name of this User.  # noqa: E501

        Company Name  # noqa: E501

        :return: The vco_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._vco_name

    @vco_name.setter
    def vco_name(self, vco_name):
        """Sets the vco_name of this User.

        Company Name  # noqa: E501

        :param vco_name: The vco_name of this User.  # noqa: E501
        :type: str
        """

        self._vco_name = vco_name

    @property
    def vco_support_email(self):
        """Gets the vco_support_email of this User.  # noqa: E501

        VCO Support E-mail  # noqa: E501

        :return: The vco_support_email of this User.  # noqa: E501
        :rtype: str
        """
        return self._vco_support_email

    @vco_support_email.setter
    def vco_support_email(self, vco_support_email):
        """Sets the vco_support_email of this User.

        VCO Support E-mail  # noqa: E501

        :param vco_support_email: The vco_support_email of this User.  # noqa: E501
        :type: str
        """

        self._vco_support_email = vco_support_email

    @property
    def customers(self):
        """Gets the customers of this User.  # noqa: E501

        List of the user's Customers  # noqa: E501

        :return: The customers of this User.  # noqa: E501
        :rtype: list[UserCustomer]
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """Sets the customers of this User.

        List of the user's Customers  # noqa: E501

        :param customers: The customers of this User.  # noqa: E501
        :type: list[UserCustomer]
        """

        self._customers = customers

    @property
    def admin_of_customers(self):
        """Gets the admin_of_customers of this User.  # noqa: E501

        List of the Customers which the user can administrate  # noqa: E501

        :return: The admin_of_customers of this User.  # noqa: E501
        :rtype: list[UserCustomer]
        """
        return self._admin_of_customers

    @admin_of_customers.setter
    def admin_of_customers(self, admin_of_customers):
        """Sets the admin_of_customers of this User.

        List of the Customers which the user can administrate  # noqa: E501

        :param admin_of_customers: The admin_of_customers of this User.  # noqa: E501
        :type: list[UserCustomer]
        """

        self._admin_of_customers = admin_of_customers

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
