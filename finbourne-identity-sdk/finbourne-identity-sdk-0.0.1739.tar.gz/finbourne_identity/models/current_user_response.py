# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1739
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

from finbourne_identity.configuration import Configuration


class CurrentUserResponse(object):
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
        'id': 'str',
        'email_address': 'str',
        'type': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'email_address': 'emailAddress',
        'type': 'type',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'email_address': 'required',
        'type': 'required',
        'links': 'optional'
    }

    def __init__(self, id=None, email_address=None, type=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CurrentUserResponse - a model defined in OpenAPI"
        
        :param id:  The user's system supplied unique identifier (required)
        :type id: str
        :param email_address:  The user's email address which may be null depending on the authentication method (required)
        :type email_address: str
        :param type:  The type of user (e.g. Personal or Service) (required)
        :type type: str
        :param links: 
        :type links: list[finbourne_identity.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email_address = None
        self._type = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.email_address = email_address
        self.type = type
        self.links = links

    @property
    def id(self):
        """Gets the id of this CurrentUserResponse.  # noqa: E501

        The user's system supplied unique identifier  # noqa: E501

        :return: The id of this CurrentUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrentUserResponse.

        The user's system supplied unique identifier  # noqa: E501

        :param id: The id of this CurrentUserResponse.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email_address(self):
        """Gets the email_address of this CurrentUserResponse.  # noqa: E501

        The user's email address which may be null depending on the authentication method  # noqa: E501

        :return: The email_address of this CurrentUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CurrentUserResponse.

        The user's email address which may be null depending on the authentication method  # noqa: E501

        :param email_address: The email_address of this CurrentUserResponse.  # noqa: E501
        :type email_address: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def type(self):
        """Gets the type of this CurrentUserResponse.  # noqa: E501

        The type of user (e.g. Personal or Service)  # noqa: E501

        :return: The type of this CurrentUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CurrentUserResponse.

        The type of user (e.g. Personal or Service)  # noqa: E501

        :param type: The type of this CurrentUserResponse.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def links(self):
        """Gets the links of this CurrentUserResponse.  # noqa: E501


        :return: The links of this CurrentUserResponse.  # noqa: E501
        :rtype: list[finbourne_identity.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CurrentUserResponse.


        :param links: The links of this CurrentUserResponse.  # noqa: E501
        :type links: list[finbourne_identity.Link]
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
        if not isinstance(other, CurrentUserResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrentUserResponse):
            return True

        return self.to_dict() != other.to_dict()
