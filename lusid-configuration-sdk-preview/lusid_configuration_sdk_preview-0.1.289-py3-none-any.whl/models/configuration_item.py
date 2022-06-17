# coding: utf-8

"""
    FINBOURNE ConfigurationService API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.289
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_configuration.configuration import Configuration


class ConfigurationItem(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'created_at': 'datetime',
        'created_by': 'str',
        'last_modified_at': 'datetime',
        'last_modified_by': 'str',
        'description': 'str',
        'key': 'str',
        'value': 'str',
        'value_type': 'str',
        'is_secret': 'bool',
        'ref': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'last_modified_at': 'lastModifiedAt',
        'last_modified_by': 'lastModifiedBy',
        'description': 'description',
        'key': 'key',
        'value': 'value',
        'value_type': 'valueType',
        'is_secret': 'isSecret',
        'ref': 'ref',
        'links': 'links'
    }

    required_map = {
        'created_at': 'required',
        'created_by': 'required',
        'last_modified_at': 'required',
        'last_modified_by': 'required',
        'description': 'optional',
        'key': 'required',
        'value': 'required',
        'value_type': 'required',
        'is_secret': 'required',
        'ref': 'required',
        'links': 'optional'
    }

    def __init__(self, created_at=None, created_by=None, last_modified_at=None, last_modified_by=None, description=None, key=None, value=None, value_type=None, is_secret=None, ref=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ConfigurationItem - a model defined in OpenAPI"
        
        :param created_at:  The date referring to the creation date of the configuration item (required)
        :type created_at: datetime
        :param created_by:  Who created the configuration item (required)
        :type created_by: str
        :param last_modified_at:  The date referring to the date when the configuration item was last modified (required)
        :type last_modified_at: datetime
        :param last_modified_by:  Who modified the configuration item most recently (required)
        :type last_modified_by: str
        :param description:  Describes the configuration item
        :type description: str
        :param key:  The key which identifies the configuration item (required)
        :type key: str
        :param value:  The value of the configuration item (required)
        :type value: str
        :param value_type:  The type of the configuration item's value (required)
        :type value_type: str
        :param is_secret:  Defines whether or not the value is a secret. (required)
        :type is_secret: bool
        :param ref:  The reference to the configuration item (required)
        :type ref: str
        :param links: 
        :type links: list[lusid_configuration.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._created_by = None
        self._last_modified_at = None
        self._last_modified_by = None
        self._description = None
        self._key = None
        self._value = None
        self._value_type = None
        self._is_secret = None
        self._ref = None
        self._links = None
        self.discriminator = None

        self.created_at = created_at
        self.created_by = created_by
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.description = description
        self.key = key
        self.value = value
        self.value_type = value_type
        self.is_secret = is_secret
        self.ref = ref
        self.links = links

    @property
    def created_at(self):
        """Gets the created_at of this ConfigurationItem.  # noqa: E501

        The date referring to the creation date of the configuration item  # noqa: E501

        :return: The created_at of this ConfigurationItem.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConfigurationItem.

        The date referring to the creation date of the configuration item  # noqa: E501

        :param created_at: The created_at of this ConfigurationItem.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this ConfigurationItem.  # noqa: E501

        Who created the configuration item  # noqa: E501

        :return: The created_by of this ConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ConfigurationItem.

        Who created the configuration item  # noqa: E501

        :param created_by: The created_by of this ConfigurationItem.  # noqa: E501
        :type created_by: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this ConfigurationItem.  # noqa: E501

        The date referring to the date when the configuration item was last modified  # noqa: E501

        :return: The last_modified_at of this ConfigurationItem.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this ConfigurationItem.

        The date referring to the date when the configuration item was last modified  # noqa: E501

        :param last_modified_at: The last_modified_at of this ConfigurationItem.  # noqa: E501
        :type last_modified_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_at`, must not be `None`")  # noqa: E501

        self._last_modified_at = last_modified_at

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ConfigurationItem.  # noqa: E501

        Who modified the configuration item most recently  # noqa: E501

        :return: The last_modified_by of this ConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ConfigurationItem.

        Who modified the configuration item most recently  # noqa: E501

        :param last_modified_by: The last_modified_by of this ConfigurationItem.  # noqa: E501
        :type last_modified_by: str
        """
        if self.local_vars_configuration.client_side_validation and last_modified_by is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_by`, must not be `None`")  # noqa: E501

        self._last_modified_by = last_modified_by

    @property
    def description(self):
        """Gets the description of this ConfigurationItem.  # noqa: E501

        Describes the configuration item  # noqa: E501

        :return: The description of this ConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationItem.

        Describes the configuration item  # noqa: E501

        :param description: The description of this ConfigurationItem.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def key(self):
        """Gets the key of this ConfigurationItem.  # noqa: E501

        The key which identifies the configuration item  # noqa: E501

        :return: The key of this ConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ConfigurationItem.

        The key which identifies the configuration item  # noqa: E501

        :param key: The key of this ConfigurationItem.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this ConfigurationItem.  # noqa: E501

        The value of the configuration item  # noqa: E501

        :return: The value of this ConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConfigurationItem.

        The value of the configuration item  # noqa: E501

        :param value: The value of this ConfigurationItem.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def value_type(self):
        """Gets the value_type of this ConfigurationItem.  # noqa: E501

        The type of the configuration item's value  # noqa: E501

        :return: The value_type of this ConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ConfigurationItem.

        The type of the configuration item's value  # noqa: E501

        :param value_type: The value_type of this ConfigurationItem.  # noqa: E501
        :type value_type: str
        """
        if self.local_vars_configuration.client_side_validation and value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501

        self._value_type = value_type

    @property
    def is_secret(self):
        """Gets the is_secret of this ConfigurationItem.  # noqa: E501

        Defines whether or not the value is a secret.  # noqa: E501

        :return: The is_secret of this ConfigurationItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_secret

    @is_secret.setter
    def is_secret(self, is_secret):
        """Sets the is_secret of this ConfigurationItem.

        Defines whether or not the value is a secret.  # noqa: E501

        :param is_secret: The is_secret of this ConfigurationItem.  # noqa: E501
        :type is_secret: bool
        """
        if self.local_vars_configuration.client_side_validation and is_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `is_secret`, must not be `None`")  # noqa: E501

        self._is_secret = is_secret

    @property
    def ref(self):
        """Gets the ref of this ConfigurationItem.  # noqa: E501

        The reference to the configuration item  # noqa: E501

        :return: The ref of this ConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ConfigurationItem.

        The reference to the configuration item  # noqa: E501

        :param ref: The ref of this ConfigurationItem.  # noqa: E501
        :type ref: str
        """
        if self.local_vars_configuration.client_side_validation and ref is None:  # noqa: E501
            raise ValueError("Invalid value for `ref`, must not be `None`")  # noqa: E501

        self._ref = ref

    @property
    def links(self):
        """Gets the links of this ConfigurationItem.  # noqa: E501


        :return: The links of this ConfigurationItem.  # noqa: E501
        :rtype: list[lusid_configuration.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ConfigurationItem.


        :param links: The links of this ConfigurationItem.  # noqa: E501
        :type links: list[lusid_configuration.Link]
        """

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigurationItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigurationItem):
            return True

        return self.to_dict() != other.to_dict()
