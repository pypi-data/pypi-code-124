# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UploadMediaRequest(object):

    """Implementation of the 'UploadMediaRequest' model.

    TODO: type model description here.

    Attributes:
        messaging_product (string): Messaging service used for the request. In
            this case, use whatsapp.
        file (string): Path to the file stored in your local directory. For
            example: "@/local/path/file.jpg".
        mtype (string): Type of media file being uploaded. See Supported Media
            Types for more information.    Supported options for images are:
            `image/jpeg`, `image/png`    Supported options for documents are:
            `text/plain`, `application/pdf`, `application/vnd.ms-powerpoint`,
            `application/msword`, `application/vnd.ms-excel`,
            `application/vnd.openxmlformats-officedocument.wordprocessingml.doc
            ument`,
            `application/vnd.openxmlformats-officedocument.presentationml.prese
            ntation`,
            `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
            Supported options for audio are: `audio/aac`, `audio/mp4`,
            `audio/mpeg`, `audio/amr`, `audio/ogg`, `audio/opus`  Supported
            options for video are: `video/mp4`, `video/3gp`  Supported options
            for stickers are: `image/webp`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "messaging_product": 'messaging_product',
        "file": 'file',
        "mtype": 'type'
    }

    def __init__(self,
                 messaging_product=None,
                 file=None,
                 mtype=None):
        """Constructor for the UploadMediaRequest class"""

        # Initialize members of the class
        self.messaging_product = messaging_product 
        self.file = file 
        self.mtype = mtype 

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

        messaging_product = dictionary.get("messaging_product") if dictionary.get("messaging_product") else None
        file = dictionary.get("file") if dictionary.get("file") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        # Return an object of this model
        return cls(messaging_product,
                   file,
                   mtype)
