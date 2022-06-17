# coding: utf-8

"""
    external/v1/external_session_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""


import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING

import six

from grid.openapi.configuration import Configuration

if TYPE_CHECKING:
    from datetime import datetime
    from grid.openapi.models import *

class V1SamlOrganizationStatus(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'user_ids': 'list[str]'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'user_ids': 'userIds'
    }

    def __init__(self, created_at: 'datetime' = None, updated_at: 'datetime' = None, user_ids: 'list[str]' = None, _configuration=None):  # noqa: E501
        """V1SamlOrganizationStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._updated_at = None
        self._user_ids = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user_ids is not None:
            self.user_ids = user_ids

    @property
    def created_at(self) -> 'datetime':
        """Gets the created_at of this V1SamlOrganizationStatus.  # noqa: E501


        :return: The created_at of this V1SamlOrganizationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: 'datetime'):
        """Sets the created_at of this V1SamlOrganizationStatus.


        :param created_at: The created_at of this V1SamlOrganizationStatus.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self) -> 'datetime':
        """Gets the updated_at of this V1SamlOrganizationStatus.  # noqa: E501


        :return: The updated_at of this V1SamlOrganizationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: 'datetime'):
        """Sets the updated_at of this V1SamlOrganizationStatus.


        :param updated_at: The updated_at of this V1SamlOrganizationStatus.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user_ids(self) -> 'list[str]':
        """Gets the user_ids of this V1SamlOrganizationStatus.  # noqa: E501


        :return: The user_ids of this V1SamlOrganizationStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids: 'list[str]'):
        """Sets the user_ids of this V1SamlOrganizationStatus.


        :param user_ids: The user_ids of this V1SamlOrganizationStatus.  # noqa: E501
        :type: list[str]
        """

        self._user_ids = user_ids

    def to_dict(self) -> dict:
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
        if issubclass(V1SamlOrganizationStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1SamlOrganizationStatus') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1SamlOrganizationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1SamlOrganizationStatus') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SamlOrganizationStatus):
            return True

        return self.to_dict() != other.to_dict()
