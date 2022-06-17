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


class DisksModel(object):
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
        'status': 'str',
        'disk_size': 'int',
        'disk_name': 'str',
        'description': 'str',
        'deletion_time': 'str',
        'exposed': 'bool',
        'disk_id': 'int',
        'disk_type': 'str',
        'order': 'str',
        'port': 'int',
        'vm_id': 'int',
        'vm_name': 'str',
        'cloudspace_id': 'str',
        'iotune': 'DisksModelIotune'
    }

    attribute_map = {
        'status': 'status',
        'disk_size': 'disk_size',
        'disk_name': 'disk_name',
        'description': 'description',
        'deletion_time': 'deletion_time',
        'exposed': 'exposed',
        'disk_id': 'disk_id',
        'disk_type': 'disk_type',
        'order': 'order',
        'port': 'port',
        'vm_id': 'vm_id',
        'vm_name': 'vm_name',
        'cloudspace_id': 'cloudspace_id',
        'iotune': 'iotune'
    }

    def __init__(self, status=None, disk_size=None, disk_name=None, description=None, deletion_time=None, exposed=None, disk_id=None, disk_type=None, order=None, port=None, vm_id=None, vm_name=None, cloudspace_id=None, iotune=None, _configuration=None):  # noqa: E501
        """DisksModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._disk_size = None
        self._disk_name = None
        self._description = None
        self._deletion_time = None
        self._exposed = None
        self._disk_id = None
        self._disk_type = None
        self._order = None
        self._port = None
        self._vm_id = None
        self._vm_name = None
        self._cloudspace_id = None
        self._iotune = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if disk_size is not None:
            self.disk_size = disk_size
        if disk_name is not None:
            self.disk_name = disk_name
        if description is not None:
            self.description = description
        if deletion_time is not None:
            self.deletion_time = deletion_time
        if exposed is not None:
            self.exposed = exposed
        if disk_id is not None:
            self.disk_id = disk_id
        if disk_type is not None:
            self.disk_type = disk_type
        if order is not None:
            self.order = order
        if port is not None:
            self.port = port
        if vm_id is not None:
            self.vm_id = vm_id
        if vm_name is not None:
            self.vm_name = vm_name
        if cloudspace_id is not None:
            self.cloudspace_id = cloudspace_id
        if iotune is not None:
            self.iotune = iotune

    @property
    def status(self):
        """Gets the status of this DisksModel.  # noqa: E501


        :return: The status of this DisksModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DisksModel.


        :param status: The status of this DisksModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def disk_size(self):
        """Gets the disk_size of this DisksModel.  # noqa: E501


        :return: The disk_size of this DisksModel.  # noqa: E501
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        """Sets the disk_size of this DisksModel.


        :param disk_size: The disk_size of this DisksModel.  # noqa: E501
        :type: int
        """

        self._disk_size = disk_size

    @property
    def disk_name(self):
        """Gets the disk_name of this DisksModel.  # noqa: E501


        :return: The disk_name of this DisksModel.  # noqa: E501
        :rtype: str
        """
        return self._disk_name

    @disk_name.setter
    def disk_name(self, disk_name):
        """Sets the disk_name of this DisksModel.


        :param disk_name: The disk_name of this DisksModel.  # noqa: E501
        :type: str
        """

        self._disk_name = disk_name

    @property
    def description(self):
        """Gets the description of this DisksModel.  # noqa: E501


        :return: The description of this DisksModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DisksModel.


        :param description: The description of this DisksModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def deletion_time(self):
        """Gets the deletion_time of this DisksModel.  # noqa: E501


        :return: The deletion_time of this DisksModel.  # noqa: E501
        :rtype: str
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this DisksModel.


        :param deletion_time: The deletion_time of this DisksModel.  # noqa: E501
        :type: str
        """

        self._deletion_time = deletion_time

    @property
    def exposed(self):
        """Gets the exposed of this DisksModel.  # noqa: E501


        :return: The exposed of this DisksModel.  # noqa: E501
        :rtype: bool
        """
        return self._exposed

    @exposed.setter
    def exposed(self, exposed):
        """Sets the exposed of this DisksModel.


        :param exposed: The exposed of this DisksModel.  # noqa: E501
        :type: bool
        """

        self._exposed = exposed

    @property
    def disk_id(self):
        """Gets the disk_id of this DisksModel.  # noqa: E501


        :return: The disk_id of this DisksModel.  # noqa: E501
        :rtype: int
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, disk_id):
        """Sets the disk_id of this DisksModel.


        :param disk_id: The disk_id of this DisksModel.  # noqa: E501
        :type: int
        """

        self._disk_id = disk_id

    @property
    def disk_type(self):
        """Gets the disk_type of this DisksModel.  # noqa: E501


        :return: The disk_type of this DisksModel.  # noqa: E501
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this DisksModel.


        :param disk_type: The disk_type of this DisksModel.  # noqa: E501
        :type: str
        """

        self._disk_type = disk_type

    @property
    def order(self):
        """Gets the order of this DisksModel.  # noqa: E501


        :return: The order of this DisksModel.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this DisksModel.


        :param order: The order of this DisksModel.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def port(self):
        """Gets the port of this DisksModel.  # noqa: E501


        :return: The port of this DisksModel.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DisksModel.


        :param port: The port of this DisksModel.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def vm_id(self):
        """Gets the vm_id of this DisksModel.  # noqa: E501


        :return: The vm_id of this DisksModel.  # noqa: E501
        :rtype: int
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this DisksModel.


        :param vm_id: The vm_id of this DisksModel.  # noqa: E501
        :type: int
        """

        self._vm_id = vm_id

    @property
    def vm_name(self):
        """Gets the vm_name of this DisksModel.  # noqa: E501

        VM name to which the disk is attached  # noqa: E501

        :return: The vm_name of this DisksModel.  # noqa: E501
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """Sets the vm_name of this DisksModel.

        VM name to which the disk is attached  # noqa: E501

        :param vm_name: The vm_name of this DisksModel.  # noqa: E501
        :type: str
        """

        self._vm_name = vm_name

    @property
    def cloudspace_id(self):
        """Gets the cloudspace_id of this DisksModel.  # noqa: E501

        Cloudspace ID of VM to which the disk is attached  # noqa: E501

        :return: The cloudspace_id of this DisksModel.  # noqa: E501
        :rtype: str
        """
        return self._cloudspace_id

    @cloudspace_id.setter
    def cloudspace_id(self, cloudspace_id):
        """Sets the cloudspace_id of this DisksModel.

        Cloudspace ID of VM to which the disk is attached  # noqa: E501

        :param cloudspace_id: The cloudspace_id of this DisksModel.  # noqa: E501
        :type: str
        """

        self._cloudspace_id = cloudspace_id

    @property
    def iotune(self):
        """Gets the iotune of this DisksModel.  # noqa: E501


        :return: The iotune of this DisksModel.  # noqa: E501
        :rtype: DisksModelIotune
        """
        return self._iotune

    @iotune.setter
    def iotune(self, iotune):
        """Sets the iotune of this DisksModel.


        :param iotune: The iotune of this DisksModel.  # noqa: E501
        :type: DisksModelIotune
        """

        self._iotune = iotune

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
        if issubclass(DisksModel, dict):
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
        if not isinstance(other, DisksModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DisksModel):
            return True

        return self.to_dict() != other.to_dict()
