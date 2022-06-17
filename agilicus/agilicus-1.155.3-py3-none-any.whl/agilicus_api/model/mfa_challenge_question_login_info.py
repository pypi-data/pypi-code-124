"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2022.06.16
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from agilicus_api.exceptions import ApiAttributeError


def lazy_import():
    from agilicus_api.model.login_session import LoginSession
    from agilicus_api.model.mfa_challenge_method import MFAChallengeMethod
    from agilicus_api.model.user import User
    globals()['LoginSession'] = LoginSession
    globals()['MFAChallengeMethod'] = MFAChallengeMethod
    globals()['User'] = User


class MFAChallengeQuestionLoginInfo(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('user_preference',): {
            'ALWAYS': "always",
            'ORGANISATION_POLICY': "organisation_policy",
        },
    }

    validations = {
        ('client_id',): {
            'max_length': 100,
        },
        ('client_guid',): {
            'max_length': 40,
        },
        ('issuer_org_id',): {
            'max_length': 40,
        },
        ('issuer_guid',): {
            'max_length': 40,
        },
        ('org_id',): {
            'max_length': 40,
        },
        ('user_id',): {
            'max_length': 40,
        },
    }

    @property
    def user_preference(self):
       return self.get("user_preference")

    @user_preference.setter
    def user_preference(self, new_value):
       self.user_preference = new_value

    @property
    def client_id(self):
       return self.get("client_id")

    @client_id.setter
    def client_id(self, new_value):
       self.client_id = new_value

    @property
    def client_guid(self):
       return self.get("client_guid")

    @client_guid.setter
    def client_guid(self, new_value):
       self.client_guid = new_value

    @property
    def issuer_org_id(self):
       return self.get("issuer_org_id")

    @issuer_org_id.setter
    def issuer_org_id(self, new_value):
       self.issuer_org_id = new_value

    @property
    def issuer_guid(self):
       return self.get("issuer_guid")

    @issuer_guid.setter
    def issuer_guid(self, new_value):
       self.issuer_guid = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def user_id(self):
       return self.get("user_id")

    @user_id.setter
    def user_id(self, new_value):
       self.user_id = new_value

    @property
    def user_object(self):
       return self.get("user_object")

    @user_object.setter
    def user_object(self, new_value):
       self.user_object = new_value

    @property
    def login_session(self):
       return self.get("login_session")

    @login_session.setter
    def login_session(self, new_value):
       self.login_session = new_value

    @property
    def upstream_idp(self):
       return self.get("upstream_idp")

    @upstream_idp.setter
    def upstream_idp(self, new_value):
       self.upstream_idp = new_value

    @property
    def ip_address(self):
       return self.get("ip_address")

    @ip_address.setter
    def ip_address(self, new_value):
       self.ip_address = new_value

    @property
    def amr_claim_present(self):
       return self.get("amr_claim_present")

    @amr_claim_present.setter
    def amr_claim_present(self, new_value):
       self.amr_claim_present = new_value

    @property
    def last_mfa_login(self):
       return self.get("last_mfa_login")

    @last_mfa_login.setter
    def last_mfa_login(self, new_value):
       self.last_mfa_login = new_value

    @property
    def user_mfa_preferences(self):
       return self.get("user_mfa_preferences")

    @user_mfa_preferences.setter
    def user_mfa_preferences(self, new_value):
       self.user_mfa_preferences = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'user_preference': (str,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'client_guid': (str,),  # noqa: E501
            'issuer_org_id': (str,),  # noqa: E501
            'issuer_guid': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'user_id': (str,),  # noqa: E501
            'upstream_idp': (str,),  # noqa: E501
            'ip_address': (str,),  # noqa: E501
            'amr_claim_present': (bool,),  # noqa: E501
            'user_object': (User,),  # noqa: E501
            'login_session': (LoginSession,),  # noqa: E501
            'last_mfa_login': (datetime,),  # noqa: E501
            'user_mfa_preferences': ([MFAChallengeMethod],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'user_preference': 'user_preference',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'client_guid': 'client_guid',  # noqa: E501
        'issuer_org_id': 'issuer_org_id',  # noqa: E501
        'issuer_guid': 'issuer_guid',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
        'upstream_idp': 'upstream_idp',  # noqa: E501
        'ip_address': 'ip_address',  # noqa: E501
        'amr_claim_present': 'amr_claim_present',  # noqa: E501
        'user_object': 'user_object',  # noqa: E501
        'login_session': 'login_session',  # noqa: E501
        'last_mfa_login': 'last_mfa_login',  # noqa: E501
        'user_mfa_preferences': 'user_mfa_preferences',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, client_id, client_guid, issuer_org_id, issuer_guid, org_id, user_id, upstream_idp, ip_address, *args, **kwargs):  # noqa: E501
        """MFAChallengeQuestionLoginInfo - a model defined in OpenAPI

        Args:
            client_id (str): The common name of the client initiating the request on behalf of the user
            client_guid (str): The guid of the client initiating the request on behalf of the user
            issuer_org_id (str): The id of the organisation for the issuer the user is logging in through
            issuer_guid (str): The guid of the issuer the user is logging into.
            org_id (str): The id of the organisation the user is a member of
            user_id (str): The id of the user requesting access
            upstream_idp (str): The upstream IDP that the user is authenticating against
            ip_address (str): The source ip address of the user's request. Both IPv4 and IPv6 address are supported

        Keyword Args:
            user_preference (str): The user's preference regarding multi-factor authentication. defaults to "organisation_policy", must be one of ["always", "organisation_policy", ]  # noqa: E501
            amr_claim_present (bool): Whether the amr claim is present in the response from the upstream. defaults to False  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            user_object (User): [optional]  # noqa: E501
            login_session (LoginSession): [optional]  # noqa: E501
            last_mfa_login (datetime): The time of the user's last successful multi-factor authenticated login. [optional]  # noqa: E501
            user_mfa_preferences ([MFAChallengeMethod]): The list of a user's multi-factor challenge methods. [optional]  # noqa: E501
        """

        user_preference = kwargs.get('user_preference', "organisation_policy")
        amr_claim_present = kwargs.get('amr_claim_present', False)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.user_preference = user_preference
        self.client_id = client_id
        self.client_guid = client_guid
        self.issuer_org_id = issuer_org_id
        self.issuer_guid = issuer_guid
        self.org_id = org_id
        self.user_id = user_id
        self.upstream_idp = upstream_idp
        self.ip_address = ip_address
        self.amr_claim_present = amr_claim_present
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    def __python_set(val):
        return set(val)
 
    required_properties = __python_set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, client_id, client_guid, issuer_org_id, issuer_guid, org_id, user_id, upstream_idp, ip_address, *args, **kwargs):  # noqa: E501
        """MFAChallengeQuestionLoginInfo - a model defined in OpenAPI

        Args:
            client_id (str): The common name of the client initiating the request on behalf of the user
            client_guid (str): The guid of the client initiating the request on behalf of the user
            issuer_org_id (str): The id of the organisation for the issuer the user is logging in through
            issuer_guid (str): The guid of the issuer the user is logging into.
            org_id (str): The id of the organisation the user is a member of
            user_id (str): The id of the user requesting access
            upstream_idp (str): The upstream IDP that the user is authenticating against
            ip_address (str): The source ip address of the user's request. Both IPv4 and IPv6 address are supported

        Keyword Args:
            user_preference (str): The user's preference regarding multi-factor authentication. defaults to "organisation_policy", must be one of ["always", "organisation_policy", ]  # noqa: E501
            amr_claim_present (bool): Whether the amr claim is present in the response from the upstream. defaults to False  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            user_object (User): [optional]  # noqa: E501
            login_session (LoginSession): [optional]  # noqa: E501
            last_mfa_login (datetime): The time of the user's last successful multi-factor authenticated login. [optional]  # noqa: E501
            user_mfa_preferences ([MFAChallengeMethod]): The list of a user's multi-factor challenge methods. [optional]  # noqa: E501
        """

        user_preference = kwargs.get('user_preference', "organisation_policy")
        amr_claim_present = kwargs.get('amr_claim_present', False)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.user_preference = user_preference
        self.client_id = client_id
        self.client_guid = client_guid
        self.issuer_org_id = issuer_org_id
        self.issuer_guid = issuer_guid
        self.org_id = org_id
        self.user_id = user_id
        self.upstream_idp = upstream_idp
        self.ip_address = ip_address
        self.amr_claim_present = amr_claim_present
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

