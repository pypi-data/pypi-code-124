# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from whatsappcloudapi.api_helper import APIHelper
from whatsappcloudapi.configuration import Server
from whatsappcloudapi.controllers.base_controller import BaseController
from whatsappcloudapi.models.success_response import SuccessResponse


class TwoStepVerificationController(BaseController):

    """A Controller to access Endpoints in the whatsappcloudapi API."""
    def __init__(self, config, auth_managers):
        super(TwoStepVerificationController, self).__init__(config, auth_managers)

    def set_two_step_verification_code(self,
                                       phone_number_id,
                                       body):
        """Does a POST request to /{Phone-Number-ID}.

        You are required to set up two-step verification for your phone
        number, as this provides an extra layer of security to the business
        accounts. You can use this endpoint to change two-step verification
        code associated with your account. 
        After you change the verification code, future requests like changing
        the name, must use the new code. 
        You set up two-factor verification and register a phone number in the
        same API call.

        Args:
            phone_number_id (string): TODO: type description here.
            body (SetTwoStepVerificationCodeRequest): TODO: type description
                here.

        Returns:
            SuccessResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/{Phone-Number-ID}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'Phone-Number-ID': {'value': phone_number_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, SuccessResponse.from_dictionary)

        return decoded
