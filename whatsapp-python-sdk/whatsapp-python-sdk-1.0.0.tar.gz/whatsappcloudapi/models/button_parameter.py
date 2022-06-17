# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class ButtonParameter(object):

    """Implementation of the 'ButtonParameter' model.

    TODO: type model description here.

    Attributes:
        mtype (ButtonParameterTypeEnum): Indicates the type of parameter for
            the button.
        payload (string): Required for quick_reply buttons. Developer-defined
            payload that is returned when the button is clicked in addition to
            the display text on the button.
        text (string): Required for URL buttons. Developer-provided suffix
            that is appended to the predefined prefix URL in the template.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "payload": 'payload',
        "text": 'text'
    }

    _optionals = [
        'payload',
        'text',
    ]

    def __init__(self,
                 mtype=None,
                 payload=APIHelper.SKIP,
                 text=APIHelper.SKIP):
        """Constructor for the ButtonParameter class"""

        # Initialize members of the class
        self.mtype = mtype 
        if payload is not APIHelper.SKIP:
            self.payload = payload 
        if text is not APIHelper.SKIP:
            self.text = text 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        mtype = dictionary.get("type") if dictionary.get("type") else None
        payload = dictionary.get("payload") if dictionary.get("payload") else APIHelper.SKIP
        text = dictionary.get("text") if dictionary.get("text") else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   payload,
                   text)
