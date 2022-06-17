# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1741
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


class OAuthApplication(object):
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
        'type': 'str',
        'display_name': 'str',
        'secret': 'str',
        'client_id': 'str',
        'issuer': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'display_name': 'displayName',
        'secret': 'secret',
        'client_id': 'clientId',
        'issuer': 'issuer'
    }

    required_map = {
        'id': 'required',
        'type': 'required',
        'display_name': 'required',
        'secret': 'optional',
        'client_id': 'required',
        'issuer': 'required'
    }

    def __init__(self, id=None, type=None, display_name=None, secret=None, client_id=None, issuer=None, local_vars_configuration=None):  # noqa: E501
        """OAuthApplication - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: str
        :param type:  (required)
        :type type: str
        :param display_name:  (required)
        :type display_name: str
        :param secret: 
        :type secret: str
        :param client_id:  (required)
        :type client_id: str
        :param issuer:  (required)
        :type issuer: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._display_name = None
        self._secret = None
        self._client_id = None
        self._issuer = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.display_name = display_name
        self.secret = secret
        self.client_id = client_id
        self.issuer = issuer

    @property
    def id(self):
        """Gets the id of this OAuthApplication.  # noqa: E501


        :return: The id of this OAuthApplication.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuthApplication.


        :param id: The id of this OAuthApplication.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this OAuthApplication.  # noqa: E501


        :return: The type of this OAuthApplication.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OAuthApplication.


        :param type: The type of this OAuthApplication.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this OAuthApplication.  # noqa: E501


        :return: The display_name of this OAuthApplication.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OAuthApplication.


        :param display_name: The display_name of this OAuthApplication.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 512):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def secret(self):
        """Gets the secret of this OAuthApplication.  # noqa: E501


        :return: The secret of this OAuthApplication.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this OAuthApplication.


        :param secret: The secret of this OAuthApplication.  # noqa: E501
        :type secret: str
        """

        self._secret = secret

    @property
    def client_id(self):
        """Gets the client_id of this OAuthApplication.  # noqa: E501


        :return: The client_id of this OAuthApplication.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OAuthApplication.


        :param client_id: The client_id of this OAuthApplication.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def issuer(self):
        """Gets the issuer of this OAuthApplication.  # noqa: E501


        :return: The issuer of this OAuthApplication.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this OAuthApplication.


        :param issuer: The issuer of this OAuthApplication.  # noqa: E501
        :type issuer: str
        """
        if self.local_vars_configuration.client_side_validation and issuer is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

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
        if not isinstance(other, OAuthApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuthApplication):
            return True

        return self.to_dict() != other.to_dict()
