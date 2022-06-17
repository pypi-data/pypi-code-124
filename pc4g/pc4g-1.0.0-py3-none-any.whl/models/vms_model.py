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


class VmsModel(object):
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
        'vm_id': 'int',
        'name': 'str',
        'status': 'str',
        'deletion_time': 'str',
        'stack_id': 'int',
        'creation_time': 'float',
        'update_time': 'float',
        'reference_id': 'str',
        'image_id': 'int',
        'storage': 'int',
        'vcpus': 'int',
        'memory': 'int',
        'appliance': 'bool',
        'disks': 'list[int]',
        'network_interfaces': 'list[VmsModelNetworkInterfaces]'
    }

    attribute_map = {
        'vm_id': 'vm_id',
        'name': 'name',
        'status': 'status',
        'deletion_time': 'deletion_time',
        'stack_id': 'stack_id',
        'creation_time': 'creation_time',
        'update_time': 'update_time',
        'reference_id': 'reference_id',
        'image_id': 'image_id',
        'storage': 'storage',
        'vcpus': 'vcpus',
        'memory': 'memory',
        'appliance': 'appliance',
        'disks': 'disks',
        'network_interfaces': 'network_interfaces'
    }

    def __init__(self, vm_id=None, name=None, status=None, deletion_time=None, stack_id=None, creation_time=None, update_time=None, reference_id=None, image_id=None, storage=None, vcpus=None, memory=None, appliance=None, disks=None, network_interfaces=None, _configuration=None):  # noqa: E501
        """VmsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vm_id = None
        self._name = None
        self._status = None
        self._deletion_time = None
        self._stack_id = None
        self._creation_time = None
        self._update_time = None
        self._reference_id = None
        self._image_id = None
        self._storage = None
        self._vcpus = None
        self._memory = None
        self._appliance = None
        self._disks = None
        self._network_interfaces = None
        self.discriminator = None

        if vm_id is not None:
            self.vm_id = vm_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if deletion_time is not None:
            self.deletion_time = deletion_time
        if stack_id is not None:
            self.stack_id = stack_id
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time
        if reference_id is not None:
            self.reference_id = reference_id
        if image_id is not None:
            self.image_id = image_id
        if storage is not None:
            self.storage = storage
        if vcpus is not None:
            self.vcpus = vcpus
        if memory is not None:
            self.memory = memory
        if appliance is not None:
            self.appliance = appliance
        if disks is not None:
            self.disks = disks
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces

    @property
    def vm_id(self):
        """Gets the vm_id of this VmsModel.  # noqa: E501


        :return: The vm_id of this VmsModel.  # noqa: E501
        :rtype: int
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this VmsModel.


        :param vm_id: The vm_id of this VmsModel.  # noqa: E501
        :type: int
        """

        self._vm_id = vm_id

    @property
    def name(self):
        """Gets the name of this VmsModel.  # noqa: E501


        :return: The name of this VmsModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmsModel.


        :param name: The name of this VmsModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this VmsModel.  # noqa: E501


        :return: The status of this VmsModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VmsModel.


        :param status: The status of this VmsModel.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def deletion_time(self):
        """Gets the deletion_time of this VmsModel.  # noqa: E501


        :return: The deletion_time of this VmsModel.  # noqa: E501
        :rtype: str
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this VmsModel.


        :param deletion_time: The deletion_time of this VmsModel.  # noqa: E501
        :type: str
        """

        self._deletion_time = deletion_time

    @property
    def stack_id(self):
        """Gets the stack_id of this VmsModel.  # noqa: E501


        :return: The stack_id of this VmsModel.  # noqa: E501
        :rtype: int
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this VmsModel.


        :param stack_id: The stack_id of this VmsModel.  # noqa: E501
        :type: int
        """

        self._stack_id = stack_id

    @property
    def creation_time(self):
        """Gets the creation_time of this VmsModel.  # noqa: E501


        :return: The creation_time of this VmsModel.  # noqa: E501
        :rtype: float
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this VmsModel.


        :param creation_time: The creation_time of this VmsModel.  # noqa: E501
        :type: float
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this VmsModel.  # noqa: E501


        :return: The update_time of this VmsModel.  # noqa: E501
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VmsModel.


        :param update_time: The update_time of this VmsModel.  # noqa: E501
        :type: float
        """

        self._update_time = update_time

    @property
    def reference_id(self):
        """Gets the reference_id of this VmsModel.  # noqa: E501


        :return: The reference_id of this VmsModel.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this VmsModel.


        :param reference_id: The reference_id of this VmsModel.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def image_id(self):
        """Gets the image_id of this VmsModel.  # noqa: E501


        :return: The image_id of this VmsModel.  # noqa: E501
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this VmsModel.


        :param image_id: The image_id of this VmsModel.  # noqa: E501
        :type: int
        """

        self._image_id = image_id

    @property
    def storage(self):
        """Gets the storage of this VmsModel.  # noqa: E501


        :return: The storage of this VmsModel.  # noqa: E501
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this VmsModel.


        :param storage: The storage of this VmsModel.  # noqa: E501
        :type: int
        """

        self._storage = storage

    @property
    def vcpus(self):
        """Gets the vcpus of this VmsModel.  # noqa: E501


        :return: The vcpus of this VmsModel.  # noqa: E501
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this VmsModel.


        :param vcpus: The vcpus of this VmsModel.  # noqa: E501
        :type: int
        """

        self._vcpus = vcpus

    @property
    def memory(self):
        """Gets the memory of this VmsModel.  # noqa: E501


        :return: The memory of this VmsModel.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this VmsModel.


        :param memory: The memory of this VmsModel.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def appliance(self):
        """Gets the appliance of this VmsModel.  # noqa: E501


        :return: The appliance of this VmsModel.  # noqa: E501
        :rtype: bool
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this VmsModel.


        :param appliance: The appliance of this VmsModel.  # noqa: E501
        :type: bool
        """

        self._appliance = appliance

    @property
    def disks(self):
        """Gets the disks of this VmsModel.  # noqa: E501


        :return: The disks of this VmsModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this VmsModel.


        :param disks: The disks of this VmsModel.  # noqa: E501
        :type: list[int]
        """

        self._disks = disks

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this VmsModel.  # noqa: E501


        :return: The network_interfaces of this VmsModel.  # noqa: E501
        :rtype: list[VmsModelNetworkInterfaces]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this VmsModel.


        :param network_interfaces: The network_interfaces of this VmsModel.  # noqa: E501
        :type: list[VmsModelNetworkInterfaces]
        """

        self._network_interfaces = network_interfaces

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
        if issubclass(VmsModel, dict):
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
        if not isinstance(other, VmsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmsModel):
            return True

        return self.to_dict() != other.to_dict()
