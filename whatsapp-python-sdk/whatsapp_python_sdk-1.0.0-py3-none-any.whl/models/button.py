# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class Button(object):

    """Implementation of the 'Button' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        title (string): Button title. It cannot be an empty string and must be
            unique within the message. Emojis are supported, markdown is not.
        id (string): Unique identifier for your button. This ID is returned in
            the webhook when the button is clicked by the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "title": 'title',
        "id": 'id'
    }

    _optionals = [
        'title',
        'id',
    ]

    def __init__(self,
                 mtype='reply',
                 title=APIHelper.SKIP,
                 id=APIHelper.SKIP):
        """Constructor for the Button class"""

        # Initialize members of the class
        self.mtype = mtype 
        if title is not APIHelper.SKIP:
            self.title = title 
        if id is not APIHelper.SKIP:
            self.id = id 

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

        mtype = dictionary.get("type") if dictionary.get("type") else 'reply'
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   title,
                   id)
