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


class NotificationConfig(object):
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
        'content': 'str',
        'created_at': 'int',
        'from_time': 'int',
        'issuer_id': 'str',
        'locations': 'list[NotificationConfigNotificationLocation]',
        'maintenance_status': 'str',
        'notification_type': 'str',
        'reason': 'str',
        'sender': 'str',
        'service_impact': 'str',
        'status': 'str',
        'till_time': 'int',
        'title': 'str',
        'id': 'str'
    }

    attribute_map = {
        'content': 'content',
        'created_at': 'created_at',
        'from_time': 'from_time',
        'issuer_id': 'issuer_id',
        'locations': 'locations',
        'maintenance_status': 'maintenance_status',
        'notification_type': 'notification_type',
        'reason': 'reason',
        'sender': 'sender',
        'service_impact': 'service_impact',
        'status': 'status',
        'till_time': 'till_time',
        'title': 'title',
        'id': 'id'
    }

    def __init__(self, content=None, created_at=None, from_time=None, issuer_id=None, locations=None, maintenance_status=None, notification_type=None, reason=None, sender=None, service_impact=None, status=None, till_time=None, title=None, id=None, _configuration=None):  # noqa: E501
        """NotificationConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content = None
        self._created_at = None
        self._from_time = None
        self._issuer_id = None
        self._locations = None
        self._maintenance_status = None
        self._notification_type = None
        self._reason = None
        self._sender = None
        self._service_impact = None
        self._status = None
        self._till_time = None
        self._title = None
        self._id = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if created_at is not None:
            self.created_at = created_at
        if from_time is not None:
            self.from_time = from_time
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if locations is not None:
            self.locations = locations
        if maintenance_status is not None:
            self.maintenance_status = maintenance_status
        if notification_type is not None:
            self.notification_type = notification_type
        if reason is not None:
            self.reason = reason
        if sender is not None:
            self.sender = sender
        if service_impact is not None:
            self.service_impact = service_impact
        if status is not None:
            self.status = status
        if till_time is not None:
            self.till_time = till_time
        if title is not None:
            self.title = title
        if id is not None:
            self.id = id

    @property
    def content(self):
        """Gets the content of this NotificationConfig.  # noqa: E501

        notification content  # noqa: E501

        :return: The content of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this NotificationConfig.

        notification content  # noqa: E501

        :param content: The content of this NotificationConfig.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this NotificationConfig.  # noqa: E501

        when notification was created  # noqa: E501

        :return: The created_at of this NotificationConfig.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NotificationConfig.

        when notification was created  # noqa: E501

        :param created_at: The created_at of this NotificationConfig.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def from_time(self):
        """Gets the from_time of this NotificationConfig.  # noqa: E501

        maintenance start time  # noqa: E501

        :return: The from_time of this NotificationConfig.  # noqa: E501
        :rtype: int
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this NotificationConfig.

        maintenance start time  # noqa: E501

        :param from_time: The from_time of this NotificationConfig.  # noqa: E501
        :type: int
        """

        self._from_time = from_time

    @property
    def issuer_id(self):
        """Gets the issuer_id of this NotificationConfig.  # noqa: E501

        GIG or CE:[ce_id] or VCO:[vco_id]  # noqa: E501

        :return: The issuer_id of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this NotificationConfig.

        GIG or CE:[ce_id] or VCO:[vco_id]  # noqa: E501

        :param issuer_id: The issuer_id of this NotificationConfig.  # noqa: E501
        :type: str
        """

        self._issuer_id = issuer_id

    @property
    def locations(self):
        """Gets the locations of this NotificationConfig.  # noqa: E501

        notification locations  # noqa: E501

        :return: The locations of this NotificationConfig.  # noqa: E501
        :rtype: list[NotificationConfigNotificationLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this NotificationConfig.

        notification locations  # noqa: E501

        :param locations: The locations of this NotificationConfig.  # noqa: E501
        :type: list[NotificationConfigNotificationLocation]
        """

        self._locations = locations

    @property
    def maintenance_status(self):
        """Gets the maintenance_status of this NotificationConfig.  # noqa: E501

        maintenance status ['PLANNED', 'CANCELED']  # noqa: E501

        :return: The maintenance_status of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_status

    @maintenance_status.setter
    def maintenance_status(self, maintenance_status):
        """Sets the maintenance_status of this NotificationConfig.

        maintenance status ['PLANNED', 'CANCELED']  # noqa: E501

        :param maintenance_status: The maintenance_status of this NotificationConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["PLANNED", "CANCELED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                maintenance_status not in allowed_values):
            raise ValueError(
                "Invalid value for `maintenance_status` ({0}), must be one of {1}"  # noqa: E501
                .format(maintenance_status, allowed_values)
            )

        self._maintenance_status = maintenance_status

    @property
    def notification_type(self):
        """Gets the notification_type of this NotificationConfig.  # noqa: E501

        notification type ['PLANNED_MAINTENANCE', 'OUTAGE_WARNING', 'NEWS_AND_UPDATES']  # noqa: E501

        :return: The notification_type of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this NotificationConfig.

        notification type ['PLANNED_MAINTENANCE', 'OUTAGE_WARNING', 'NEWS_AND_UPDATES']  # noqa: E501

        :param notification_type: The notification_type of this NotificationConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["PLANNED_MAINTENANCE", "OUTAGE_WARNING", "NEWS_AND_UPDATES"]  # noqa: E501
        if (self._configuration.client_side_validation and
                notification_type not in allowed_values):
            raise ValueError(
                "Invalid value for `notification_type` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_type, allowed_values)
            )

        self._notification_type = notification_type

    @property
    def reason(self):
        """Gets the reason of this NotificationConfig.  # noqa: E501

        maintenance reason  # noqa: E501

        :return: The reason of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this NotificationConfig.

        maintenance reason  # noqa: E501

        :param reason: The reason of this NotificationConfig.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def sender(self):
        """Gets the sender of this NotificationConfig.  # noqa: E501

        notification sender  # noqa: E501

        :return: The sender of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this NotificationConfig.

        notification sender  # noqa: E501

        :param sender: The sender of this NotificationConfig.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def service_impact(self):
        """Gets the service_impact of this NotificationConfig.  # noqa: E501

        the impact on the service                          ['NOT_APPLICABLE', 'NO_IMPACT', 'LIMITED_IMPACT', 'DEGRADED_SERVICE', 'DOWN']  # noqa: E501

        :return: The service_impact of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._service_impact

    @service_impact.setter
    def service_impact(self, service_impact):
        """Sets the service_impact of this NotificationConfig.

        the impact on the service                          ['NOT_APPLICABLE', 'NO_IMPACT', 'LIMITED_IMPACT', 'DEGRADED_SERVICE', 'DOWN']  # noqa: E501

        :param service_impact: The service_impact of this NotificationConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOT_APPLICABLE", "NO_IMPACT", "LIMITED_IMPACT", "DEGRADED_SERVICE", "DOWN"]  # noqa: E501
        if (self._configuration.client_side_validation and
                service_impact not in allowed_values):
            raise ValueError(
                "Invalid value for `service_impact` ({0}), must be one of {1}"  # noqa: E501
                .format(service_impact, allowed_values)
            )

        self._service_impact = service_impact

    @property
    def status(self):
        """Gets the status of this NotificationConfig.  # noqa: E501

        notification status ['DRAFT', 'SENT']  # noqa: E501

        :return: The status of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NotificationConfig.

        notification status ['DRAFT', 'SENT']  # noqa: E501

        :param status: The status of this NotificationConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["DRAFT", "SENT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def till_time(self):
        """Gets the till_time of this NotificationConfig.  # noqa: E501

        maintenance end time  # noqa: E501

        :return: The till_time of this NotificationConfig.  # noqa: E501
        :rtype: int
        """
        return self._till_time

    @till_time.setter
    def till_time(self, till_time):
        """Sets the till_time of this NotificationConfig.

        maintenance end time  # noqa: E501

        :param till_time: The till_time of this NotificationConfig.  # noqa: E501
        :type: int
        """

        self._till_time = till_time

    @property
    def title(self):
        """Gets the title of this NotificationConfig.  # noqa: E501

        notification title  # noqa: E501

        :return: The title of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NotificationConfig.

        notification title  # noqa: E501

        :param title: The title of this NotificationConfig.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def id(self):
        """Gets the id of this NotificationConfig.  # noqa: E501

        Notifications identifier  # noqa: E501

        :return: The id of this NotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationConfig.

        Notifications identifier  # noqa: E501

        :param id: The id of this NotificationConfig.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(NotificationConfig, dict):
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
        if not isinstance(other, NotificationConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationConfig):
            return True

        return self.to_dict() != other.to_dict()
