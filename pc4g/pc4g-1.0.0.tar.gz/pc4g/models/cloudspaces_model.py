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


class CloudspacesModel(object):
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
        'cloudspace_id': 'str',
        'status': 'str',
        'deletion_time': 'str',
        'external_network_ip': 'str',
        'name': 'str',
        'update_time': 'int',
        'creation_time': 'int',
        'router_type': 'str',
        'cloudspace_mode': 'str',
        'private_network': 'str',
        'location': 'str'
    }

    attribute_map = {
        'cloudspace_id': 'cloudspace_id',
        'status': 'status',
        'deletion_time': 'deletion_time',
        'external_network_ip': 'external_network_ip',
        'name': 'name',
        'update_time': 'update_time',
        'creation_time': 'creation_time',
        'router_type': 'router_type',
        'cloudspace_mode': 'cloudspace_mode',
        'private_network': 'private_network',
        'location': 'location'
    }

    def __init__(self, cloudspace_id=None, status=None, deletion_time=None, external_network_ip=None, name=None, update_time=None, creation_time=None, router_type=None, cloudspace_mode=None, private_network=None, location=None, _configuration=None):  # noqa: E501
        """CloudspacesModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cloudspace_id = None
        self._status = None
        self._deletion_time = None
        self._external_network_ip = None
        self._name = None
        self._update_time = None
        self._creation_time = None
        self._router_type = None
        self._cloudspace_mode = None
        self._private_network = None
        self._location = None
        self.discriminator = None

        if cloudspace_id is not None:
            self.cloudspace_id = cloudspace_id
        if status is not None:
            self.status = status
        if deletion_time is not None:
            self.deletion_time = deletion_time
        if external_network_ip is not None:
            self.external_network_ip = external_network_ip
        if name is not None:
            self.name = name
        if update_time is not None:
            self.update_time = update_time
        if creation_time is not None:
            self.creation_time = creation_time
        if router_type is not None:
            self.router_type = router_type
        if cloudspace_mode is not None:
            self.cloudspace_mode = cloudspace_mode
        if private_network is not None:
            self.private_network = private_network
        if location is not None:
            self.location = location

    @property
    def cloudspace_id(self):
        """Gets the cloudspace_id of this CloudspacesModel.  # noqa: E501


        :return: The cloudspace_id of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_id

    @cloudspace_id.setter
    def cloudspace_id(self, cloudspace_id):
        """Sets the cloudspace_id of this CloudspacesModel.


        :param cloudspace_id: The cloudspace_id of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._cloudspace_id = cloudspace_id

    @property
    def status(self):
        """Gets the status of this CloudspacesModel.  # noqa: E501


        :return: The status of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CloudspacesModel.


        :param status: The status of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def deletion_time(self):
        """Gets the deletion_time of this CloudspacesModel.  # noqa: E501


        :return: The deletion_time of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this CloudspacesModel.


        :param deletion_time: The deletion_time of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._deletion_time = deletion_time

    @property
    def external_network_ip(self):
        """Gets the external_network_ip of this CloudspacesModel.  # noqa: E501


        :return: The external_network_ip of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._external_network_ip

    @external_network_ip.setter
    def external_network_ip(self, external_network_ip):
        """Sets the external_network_ip of this CloudspacesModel.


        :param external_network_ip: The external_network_ip of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._external_network_ip = external_network_ip

    @property
    def name(self):
        """Gets the name of this CloudspacesModel.  # noqa: E501


        :return: The name of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudspacesModel.


        :param name: The name of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def update_time(self):
        """Gets the update_time of this CloudspacesModel.  # noqa: E501


        :return: The update_time of this CloudspacesModel.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CloudspacesModel.


        :param update_time: The update_time of this CloudspacesModel.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

    @property
    def creation_time(self):
        """Gets the creation_time of this CloudspacesModel.  # noqa: E501


        :return: The creation_time of this CloudspacesModel.  # noqa: E501
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this CloudspacesModel.


        :param creation_time: The creation_time of this CloudspacesModel.  # noqa: E501
        :type: int
        """

        self._creation_time = creation_time

    @property
    def router_type(self):
        """Gets the router_type of this CloudspacesModel.  # noqa: E501


        :return: The router_type of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._router_type

    @router_type.setter
    def router_type(self, router_type):
        """Sets the router_type of this CloudspacesModel.


        :param router_type: The router_type of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._router_type = router_type

    @property
    def cloudspace_mode(self):
        """Gets the cloudspace_mode of this CloudspacesModel.  # noqa: E501


        :return: The cloudspace_mode of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_mode

    @cloudspace_mode.setter
    def cloudspace_mode(self, cloudspace_mode):
        """Sets the cloudspace_mode of this CloudspacesModel.


        :param cloudspace_mode: The cloudspace_mode of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._cloudspace_mode = cloudspace_mode

    @property
    def private_network(self):
        """Gets the private_network of this CloudspacesModel.  # noqa: E501


        :return: The private_network of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._private_network

    @private_network.setter
    def private_network(self, private_network):
        """Sets the private_network of this CloudspacesModel.


        :param private_network: The private_network of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._private_network = private_network

    @property
    def location(self):
        """Gets the location of this CloudspacesModel.  # noqa: E501


        :return: The location of this CloudspacesModel.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CloudspacesModel.


        :param location: The location of this CloudspacesModel.  # noqa: E501
        :type: str
        """

        self._location = location

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
        if issubclass(CloudspacesModel, dict):
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
        if not isinstance(other, CloudspacesModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudspacesModel):
            return True

        return self.to_dict() != other.to_dict()
