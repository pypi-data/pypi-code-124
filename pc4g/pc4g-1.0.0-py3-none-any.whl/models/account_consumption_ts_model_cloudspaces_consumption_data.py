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


class AccountConsumptionTsModelCloudspacesConsumptionData(object):
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
        'su': 'float',
        'tu': 'float',
        'nu': 'float',
        'vcu': 'float',
        'mu': 'float',
        'piu': 'float',
        'wu': 'float'
    }

    attribute_map = {
        'su': 'su',
        'tu': 'tu',
        'nu': 'nu',
        'vcu': 'vcu',
        'mu': 'mu',
        'piu': 'piu',
        'wu': 'wu'
    }

    def __init__(self, su=None, tu=None, nu=None, vcu=None, mu=None, piu=None, wu=None, _configuration=None):  # noqa: E501
        """AccountConsumptionTsModelCloudspacesConsumptionData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._su = None
        self._tu = None
        self._nu = None
        self._vcu = None
        self._mu = None
        self._piu = None
        self._wu = None
        self.discriminator = None

        if su is not None:
            self.su = su
        if tu is not None:
            self.tu = tu
        if nu is not None:
            self.nu = nu
        if vcu is not None:
            self.vcu = vcu
        if mu is not None:
            self.mu = mu
        if piu is not None:
            self.piu = piu
        if wu is not None:
            self.wu = wu

    @property
    def su(self):
        """Gets the su of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501


        :return: The su of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :rtype: float
        """
        return self._su

    @su.setter
    def su(self, su):
        """Sets the su of this AccountConsumptionTsModelCloudspacesConsumptionData.


        :param su: The su of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :type: float
        """

        self._su = su

    @property
    def tu(self):
        """Gets the tu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501


        :return: The tu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :rtype: float
        """
        return self._tu

    @tu.setter
    def tu(self, tu):
        """Sets the tu of this AccountConsumptionTsModelCloudspacesConsumptionData.


        :param tu: The tu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :type: float
        """

        self._tu = tu

    @property
    def nu(self):
        """Gets the nu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501


        :return: The nu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :rtype: float
        """
        return self._nu

    @nu.setter
    def nu(self, nu):
        """Sets the nu of this AccountConsumptionTsModelCloudspacesConsumptionData.


        :param nu: The nu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :type: float
        """

        self._nu = nu

    @property
    def vcu(self):
        """Gets the vcu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501


        :return: The vcu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :rtype: float
        """
        return self._vcu

    @vcu.setter
    def vcu(self, vcu):
        """Sets the vcu of this AccountConsumptionTsModelCloudspacesConsumptionData.


        :param vcu: The vcu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :type: float
        """

        self._vcu = vcu

    @property
    def mu(self):
        """Gets the mu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501


        :return: The mu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :rtype: float
        """
        return self._mu

    @mu.setter
    def mu(self, mu):
        """Sets the mu of this AccountConsumptionTsModelCloudspacesConsumptionData.


        :param mu: The mu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :type: float
        """

        self._mu = mu

    @property
    def piu(self):
        """Gets the piu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501


        :return: The piu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :rtype: float
        """
        return self._piu

    @piu.setter
    def piu(self, piu):
        """Sets the piu of this AccountConsumptionTsModelCloudspacesConsumptionData.


        :param piu: The piu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :type: float
        """

        self._piu = piu

    @property
    def wu(self):
        """Gets the wu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501


        :return: The wu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :rtype: float
        """
        return self._wu

    @wu.setter
    def wu(self, wu):
        """Sets the wu of this AccountConsumptionTsModelCloudspacesConsumptionData.


        :param wu: The wu of this AccountConsumptionTsModelCloudspacesConsumptionData.  # noqa: E501
        :type: float
        """

        self._wu = wu

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
        if issubclass(AccountConsumptionTsModelCloudspacesConsumptionData, dict):
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
        if not isinstance(other, AccountConsumptionTsModelCloudspacesConsumptionData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountConsumptionTsModelCloudspacesConsumptionData):
            return True

        return self.to_dict() != other.to_dict()
