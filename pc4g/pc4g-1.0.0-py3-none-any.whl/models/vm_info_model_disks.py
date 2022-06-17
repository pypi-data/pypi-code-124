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


class VmInfoModelDisks(object):
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
        'exposed': 'bool',
        'pci_bus': 'int',
        'pci_slot': 'int',
        'disk_id': 'int',
        'disk_type': 'str',
        'order': 'str'
    }

    attribute_map = {
        'status': 'status',
        'disk_size': 'disk_size',
        'disk_name': 'disk_name',
        'description': 'description',
        'exposed': 'exposed',
        'pci_bus': 'pci_bus',
        'pci_slot': 'pci_slot',
        'disk_id': 'disk_id',
        'disk_type': 'disk_type',
        'order': 'order'
    }

    def __init__(self, status=None, disk_size=None, disk_name=None, description=None, exposed=None, pci_bus=None, pci_slot=None, disk_id=None, disk_type=None, order=None, _configuration=None):  # noqa: E501
        """VmInfoModelDisks - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._disk_size = None
        self._disk_name = None
        self._description = None
        self._exposed = None
        self._pci_bus = None
        self._pci_slot = None
        self._disk_id = None
        self._disk_type = None
        self._order = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if disk_size is not None:
            self.disk_size = disk_size
        if disk_name is not None:
            self.disk_name = disk_name
        if description is not None:
            self.description = description
        if exposed is not None:
            self.exposed = exposed
        if pci_bus is not None:
            self.pci_bus = pci_bus
        if pci_slot is not None:
            self.pci_slot = pci_slot
        if disk_id is not None:
            self.disk_id = disk_id
        if disk_type is not None:
            self.disk_type = disk_type
        if order is not None:
            self.order = order

    @property
    def status(self):
        """Gets the status of this VmInfoModelDisks.  # noqa: E501


        :return: The status of this VmInfoModelDisks.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VmInfoModelDisks.


        :param status: The status of this VmInfoModelDisks.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def disk_size(self):
        """Gets the disk_size of this VmInfoModelDisks.  # noqa: E501


        :return: The disk_size of this VmInfoModelDisks.  # noqa: E501
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        """Sets the disk_size of this VmInfoModelDisks.


        :param disk_size: The disk_size of this VmInfoModelDisks.  # noqa: E501
        :type: int
        """

        self._disk_size = disk_size

    @property
    def disk_name(self):
        """Gets the disk_name of this VmInfoModelDisks.  # noqa: E501


        :return: The disk_name of this VmInfoModelDisks.  # noqa: E501
        :rtype: str
        """
        return self._disk_name

    @disk_name.setter
    def disk_name(self, disk_name):
        """Sets the disk_name of this VmInfoModelDisks.


        :param disk_name: The disk_name of this VmInfoModelDisks.  # noqa: E501
        :type: str
        """

        self._disk_name = disk_name

    @property
    def description(self):
        """Gets the description of this VmInfoModelDisks.  # noqa: E501


        :return: The description of this VmInfoModelDisks.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VmInfoModelDisks.


        :param description: The description of this VmInfoModelDisks.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def exposed(self):
        """Gets the exposed of this VmInfoModelDisks.  # noqa: E501


        :return: The exposed of this VmInfoModelDisks.  # noqa: E501
        :rtype: bool
        """
        return self._exposed

    @exposed.setter
    def exposed(self, exposed):
        """Sets the exposed of this VmInfoModelDisks.


        :param exposed: The exposed of this VmInfoModelDisks.  # noqa: E501
        :type: bool
        """

        self._exposed = exposed

    @property
    def pci_bus(self):
        """Gets the pci_bus of this VmInfoModelDisks.  # noqa: E501


        :return: The pci_bus of this VmInfoModelDisks.  # noqa: E501
        :rtype: int
        """
        return self._pci_bus

    @pci_bus.setter
    def pci_bus(self, pci_bus):
        """Sets the pci_bus of this VmInfoModelDisks.


        :param pci_bus: The pci_bus of this VmInfoModelDisks.  # noqa: E501
        :type: int
        """

        self._pci_bus = pci_bus

    @property
    def pci_slot(self):
        """Gets the pci_slot of this VmInfoModelDisks.  # noqa: E501


        :return: The pci_slot of this VmInfoModelDisks.  # noqa: E501
        :rtype: int
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """Sets the pci_slot of this VmInfoModelDisks.


        :param pci_slot: The pci_slot of this VmInfoModelDisks.  # noqa: E501
        :type: int
        """

        self._pci_slot = pci_slot

    @property
    def disk_id(self):
        """Gets the disk_id of this VmInfoModelDisks.  # noqa: E501


        :return: The disk_id of this VmInfoModelDisks.  # noqa: E501
        :rtype: int
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, disk_id):
        """Sets the disk_id of this VmInfoModelDisks.


        :param disk_id: The disk_id of this VmInfoModelDisks.  # noqa: E501
        :type: int
        """

        self._disk_id = disk_id

    @property
    def disk_type(self):
        """Gets the disk_type of this VmInfoModelDisks.  # noqa: E501


        :return: The disk_type of this VmInfoModelDisks.  # noqa: E501
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this VmInfoModelDisks.


        :param disk_type: The disk_type of this VmInfoModelDisks.  # noqa: E501
        :type: str
        """

        self._disk_type = disk_type

    @property
    def order(self):
        """Gets the order of this VmInfoModelDisks.  # noqa: E501


        :return: The order of this VmInfoModelDisks.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this VmInfoModelDisks.


        :param order: The order of this VmInfoModelDisks.  # noqa: E501
        :type: str
        """

        self._order = order

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
        if issubclass(VmInfoModelDisks, dict):
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
        if not isinstance(other, VmInfoModelDisks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmInfoModelDisks):
            return True

        return self.to_dict() != other.to_dict()
