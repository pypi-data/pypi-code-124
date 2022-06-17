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

class V1UpdateTensorboardResponse(object):
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
        'id': 'str',
        'spec': 'V1TensorboardSpec',
        'status': 'V1TensorboardStatus'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'id': 'id',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, created_at: 'datetime' = None, id: 'str' = None, spec: 'V1TensorboardSpec' = None, status: 'V1TensorboardStatus' = None, _configuration=None):  # noqa: E501
        """V1UpdateTensorboardResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._id = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def created_at(self) -> 'datetime':
        """Gets the created_at of this V1UpdateTensorboardResponse.  # noqa: E501


        :return: The created_at of this V1UpdateTensorboardResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: 'datetime'):
        """Sets the created_at of this V1UpdateTensorboardResponse.


        :param created_at: The created_at of this V1UpdateTensorboardResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self) -> 'str':
        """Gets the id of this V1UpdateTensorboardResponse.  # noqa: E501


        :return: The id of this V1UpdateTensorboardResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: 'str'):
        """Sets the id of this V1UpdateTensorboardResponse.


        :param id: The id of this V1UpdateTensorboardResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def spec(self) -> 'V1TensorboardSpec':
        """Gets the spec of this V1UpdateTensorboardResponse.  # noqa: E501


        :return: The spec of this V1UpdateTensorboardResponse.  # noqa: E501
        :rtype: V1TensorboardSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec: 'V1TensorboardSpec'):
        """Sets the spec of this V1UpdateTensorboardResponse.


        :param spec: The spec of this V1UpdateTensorboardResponse.  # noqa: E501
        :type: V1TensorboardSpec
        """

        self._spec = spec

    @property
    def status(self) -> 'V1TensorboardStatus':
        """Gets the status of this V1UpdateTensorboardResponse.  # noqa: E501


        :return: The status of this V1UpdateTensorboardResponse.  # noqa: E501
        :rtype: V1TensorboardStatus
        """
        return self._status

    @status.setter
    def status(self, status: 'V1TensorboardStatus'):
        """Sets the status of this V1UpdateTensorboardResponse.


        :param status: The status of this V1UpdateTensorboardResponse.  # noqa: E501
        :type: V1TensorboardStatus
        """

        self._status = status

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
        if issubclass(V1UpdateTensorboardResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1UpdateTensorboardResponse') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1UpdateTensorboardResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1UpdateTensorboardResponse') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1UpdateTensorboardResponse):
            return True

        return self.to_dict() != other.to_dict()
