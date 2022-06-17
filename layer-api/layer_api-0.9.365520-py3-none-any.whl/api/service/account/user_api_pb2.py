# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/service/account/user_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api.entity import connection_pb2 as api_dot_entity_dot_connection__pb2
from layerapi.api.entity import organization_pb2 as api_dot_entity_dot_organization__pb2
from layerapi.api.entity import organization_invite_pb2 as api_dot_entity_dot_organization__invite__pb2
from layerapi.api.entity import organization_view_pb2 as api_dot_entity_dot_organization__view__pb2
from layerapi.api.entity import tier_pb2 as api_dot_entity_dot_tier__pb2
from layerapi.api.entity import user_pb2 as api_dot_entity_dot_user__pb2
from layerapi.api import ids_pb2 as api_dot_ids__pb2
from layerapi.api.service.options import custom_options_pb2 as api_dot_service_dot_options_dot_custom__options__pb2
from layerapi.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/service/account/user_api.proto\x12\x03\x61pi\x1a\x1b\x61pi/entity/connection.proto\x1a\x1d\x61pi/entity/organization.proto\x1a$api/entity/organization_invite.proto\x1a\"api/entity/organization_view.proto\x1a\x15\x61pi/entity/tier.proto\x1a\x15\x61pi/entity/user.proto\x1a\rapi/ids.proto\x1a(api/service/options/custom_options.proto\x1a\x17validate/validate.proto\"\x12\n\x10GetMyUserRequest\",\n\x11GetMyUserResponse\x12\x17\n\x04user\x18\x01 \x01(\x0b\x32\t.api.User\"\x19\n\x17GetMyPermissionsRequest\"/\n\x18GetMyPermissionsResponse\x12\x13\n\x0bpermissions\x18\x01 \x03(\t\".\n\x0eGetUserRequest\x12\x1c\n\x07user_id\x18\x01 \x01(\x0b\x32\x0b.api.UserId\"*\n\x0fGetUserResponse\x12\x17\n\x04user\x18\x01 \x01(\x0b\x32\t.api.User\"\x19\n\x17GetOrganizationsRequest\"D\n\x18GetOrganizationsResponse\x12(\n\rorganizations\x18\x01 \x03(\x0b\x32\x11.api.Organization\"X\n\x1dGetOrganizationMembersRequest\x12\x37\n\x15\x61uth0_organization_id\x18\x01 \x01(\x0b\x32\x18.api.Auth0OrganizationId\"I\n\x1eGetOrganizationMembersResponse\x12\'\n\x14organization_members\x18\x01 \x03(\x0b\x32\t.api.User\"8\n\x1cGetOrganizationByNameRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\x80\x02\"H\n\x1dGetOrganizationByNameResponse\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\"<\n GetOrganizationViewByNameRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\x80\x02\"\x8e\x01\n!GetOrganizationViewByNameResponse\x12,\n\x0forganization_id\x18\x01 \x01(\x0b\x32\x13.api.OrganizationId\x12\x19\n\x11organization_name\x18\x02 \x01(\t\x12 \n\x0c\x64isplay_name\x18\x03 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\x80\x02\"N\n\x1eGetOrganizationViewByIdRequest\x12,\n\x0forganization_id\x18\x01 \x01(\x0b\x32\x13.api.OrganizationId\"S\n\x1fGetOrganizationViewByIdResponse\x12\x30\n\x11organization_view\x18\x01 \x01(\x0b\x32\x15.api.OrganizationView\"N\n\x1eGetOrganizationNameByIdRequest\x12,\n\x0forganization_id\x18\x01 \x01(\x0b\x32\x13.api.OrganizationId\"<\n\x1fGetOrganizationNameByIdResponse\x12\x19\n\x11organization_name\x18\x01 \x01(\t\"\xc3\x01\n<ReCreateLayerOrganizationForExistingAuth0OrganizationRequest\x12,\n\x0forganization_id\x18\x01 \x01(\x0b\x32\x13.api.OrganizationId\x12\x37\n\x15\x61uth0_organization_id\x18\x02 \x01(\x0b\x32\x18.api.Auth0OrganizationId\x12\x1c\n\x07tier_id\x18\x03 \x01(\x0b\x32\x0b.api.TierId\"h\n=ReCreateLayerOrganizationForExistingAuth0OrganizationResponse\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\"P\n\x19UpdateOrganizationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x0f\n\x07\x64omains\x18\x03 \x03(\t\"E\n\x1aUpdateOrganizationResponse\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\"X\n\x1dGetOrganizationInvitesRequest\x12\x37\n\x15\x61uth0_organization_id\x18\x01 \x01(\x0b\x32\x18.api.Auth0OrganizationId\"W\n\x1eGetOrganizationInvitesResponse\x12\x35\n\x14organization_invites\x18\x01 \x03(\x0b\x32\x17.api.OrganizationInvite\"\xac\x01\n\x1f\x43reateOrganizationInviteRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x37\n\x15\x61uth0_organization_id\x18\x02 \x01(\x0b\x32\x18.api.Auth0OrganizationId\x12\x1a\n\x05roles\x18\x03 \x03(\x0b\x32\x0b.api.RoleId\x12%\n\tclient_id\x18\x04 \x01(\x0b\x32\x12.api.Auth0ClientId\"X\n CreateOrganizationInviteResponse\x12\x34\n\x13organization_invite\x18\x01 \x01(\x0b\x32\x17.api.OrganizationInvite\"\x81\x01\n\x1fRevokeOrganizationInviteRequest\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x19.api.OrganizationInviteId\x12\x37\n\x15\x61uth0_organization_id\x18\x02 \x01(\x0b\x32\x18.api.Auth0OrganizationId\"[\n RevokeOrganizationInviteResponse\x12\x37\n\x15\x61uth0_organization_id\x18\x01 \x01(\x0b\x32\x18.api.Auth0OrganizationId\"i\n#ToggleOrganizationActivationRequest\x12\x31\n\x0forganization_id\x18\x01 \x01(\x0b\x32\x18.api.Auth0OrganizationId\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"O\n$ToggleOrganizationActivationResponse\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\"z\n!RemoveUserFromOrganizationRequest\x12\x37\n\x15\x61uth0_organization_id\x18\x01 \x01(\x0b\x32\x18.api.Auth0OrganizationId\x12\x1c\n\x07user_id\x18\x02 \x01(\x0b\x32\x0b.api.UserId\"]\n\"RemoveUserFromOrganizationResponse\x12\x37\n\x15\x61uth0_organization_id\x18\x01 \x01(\x0b\x32\x18.api.Auth0OrganizationId\"\x17\n\x15GetConnectionsRequest\">\n\x16GetConnectionsResponse\x12$\n\x0b\x63onnections\x18\x01 \x03(\x0b\x32\x0f.api.Connection\"\x8b\x01\n&EnableConnectionForOrganizationRequest\x12\x37\n\x15\x61uth0_organization_id\x18\x01 \x01(\x0b\x32\x18.api.Auth0OrganizationId\x12(\n\rconnection_id\x18\x02 \x01(\x0b\x32\x11.api.ConnectionId\"S\n\'EnableConnectionForOrganizationResponse\x12(\n\rconnection_id\x18\x01 \x01(\x0b\x32\x11.api.ConnectionId\"\x1a\n\x18GetMyOrganizationRequest\"D\n\x19GetMyOrganizationResponse\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\"m\n\x1f\x41ssignTierToOrganizationRequest\x12,\n\x0forganization_id\x18\x01 \x01(\x0b\x32\x13.api.OrganizationId\x12\x1c\n\x07tier_id\x18\x02 \x01(\x0b\x32\x0b.api.TierId\"K\n AssignTierToOrganizationResponse\x12\'\n\x0corganization\x18\x01 \x01(\x0b\x32\x11.api.Organization\"\x12\n\x10GetMyTierRequest\",\n\x11GetMyTierResponse\x12\x17\n\x04tier\x18\x01 \x01(\x0b\x32\t.api.Tier\"\x1a\n\x18GetGuestAuthTokenRequest\"*\n\x19GetGuestAuthTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t2\xe5\x10\n\x07UserAPI\x12\x34\n\x07GetUser\x12\x13.api.GetUserRequest\x1a\x14.api.GetUserResponse\x12:\n\tGetMyUser\x12\x15.api.GetMyUserRequest\x1a\x16.api.GetMyUserResponse\x12O\n\x10GetMyPermissions\x12\x1c.api.GetMyPermissionsRequest\x1a\x1d.api.GetMyPermissionsResponse\x12O\n\x10GetOrganizations\x12\x1c.api.GetOrganizationsRequest\x1a\x1d.api.GetOrganizationsResponse\x12^\n\x15GetOrganizationByName\x12!.api.GetOrganizationByNameRequest\x1a\".api.GetOrganizationByNameResponse\x12j\n\x19GetOrganizationViewByName\x12%.api.GetOrganizationViewByNameRequest\x1a&.api.GetOrganizationViewByNameResponse\x12\x64\n\x17GetOrganizationViewById\x12#.api.GetOrganizationViewByIdRequest\x1a$.api.GetOrganizationViewByIdResponse\x12\x64\n\x17GetOrganizationNameById\x12#.api.GetOrganizationNameByIdRequest\x1a$.api.GetOrganizationNameByIdResponse\x12\x61\n\x16GetOrganizationMembers\x12\".api.GetOrganizationMembersRequest\x1a#.api.GetOrganizationMembersResponse\x12\xbe\x01\n5ReCreateLayerOrganizationForExistingAuth0Organization\x12\x41.api.ReCreateLayerOrganizationForExistingAuth0OrganizationRequest\x1a\x42.api.ReCreateLayerOrganizationForExistingAuth0OrganizationResponse\x12U\n\x12UpdateOrganization\x12\x1e.api.UpdateOrganizationRequest\x1a\x1f.api.UpdateOrganizationResponse\x12\x61\n\x16GetOrganizationInvites\x12\".api.GetOrganizationInvitesRequest\x1a#.api.GetOrganizationInvitesResponse\x12g\n\x18\x43reateOrganizationInvite\x12$.api.CreateOrganizationInviteRequest\x1a%.api.CreateOrganizationInviteResponse\x12g\n\x18RevokeOrganizationInvite\x12$.api.RevokeOrganizationInviteRequest\x1a%.api.RevokeOrganizationInviteResponse\x12s\n\x1cToggleOrganizationActivation\x12(.api.ToggleOrganizationActivationRequest\x1a).api.ToggleOrganizationActivationResponse\x12m\n\x1aRemoveUserFromOrganization\x12&.api.RemoveUserFromOrganizationRequest\x1a\'.api.RemoveUserFromOrganizationResponse\x12I\n\x0eGetConnections\x12\x1a.api.GetConnectionsRequest\x1a\x1b.api.GetConnectionsResponse\x12|\n\x1f\x45nableConnectionForOrganization\x12+.api.EnableConnectionForOrganizationRequest\x1a,.api.EnableConnectionForOrganizationResponse\x12R\n\x11GetMyOrganization\x12\x1d.api.GetMyOrganizationRequest\x1a\x1e.api.GetMyOrganizationResponse\x12g\n\x18\x41ssignTierToOrganization\x12$.api.AssignTierToOrganizationRequest\x1a%.api.AssignTierToOrganizationResponse\x12:\n\tGetMyTier\x12\x15.api.GetMyTierRequest\x1a\x16.api.GetMyTierResponse\x12X\n\x11GetGuestAuthToken\x12\x1d.api.GetGuestAuthTokenRequest\x1a\x1e.api.GetGuestAuthTokenResponse\"\x04\xc0\xb5\x18\x01\x42\x1f\n\rcom.layer.apiB\x0cUserApiProtoP\x01\x62\x06proto3')



_GETMYUSERREQUEST = DESCRIPTOR.message_types_by_name['GetMyUserRequest']
_GETMYUSERRESPONSE = DESCRIPTOR.message_types_by_name['GetMyUserResponse']
_GETMYPERMISSIONSREQUEST = DESCRIPTOR.message_types_by_name['GetMyPermissionsRequest']
_GETMYPERMISSIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetMyPermissionsResponse']
_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_GETUSERRESPONSE = DESCRIPTOR.message_types_by_name['GetUserResponse']
_GETORGANIZATIONSREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationsRequest']
_GETORGANIZATIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationsResponse']
_GETORGANIZATIONMEMBERSREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationMembersRequest']
_GETORGANIZATIONMEMBERSRESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationMembersResponse']
_GETORGANIZATIONBYNAMEREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationByNameRequest']
_GETORGANIZATIONBYNAMERESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationByNameResponse']
_GETORGANIZATIONVIEWBYNAMEREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationViewByNameRequest']
_GETORGANIZATIONVIEWBYNAMERESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationViewByNameResponse']
_GETORGANIZATIONVIEWBYIDREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationViewByIdRequest']
_GETORGANIZATIONVIEWBYIDRESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationViewByIdResponse']
_GETORGANIZATIONNAMEBYIDREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationNameByIdRequest']
_GETORGANIZATIONNAMEBYIDRESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationNameByIdResponse']
_RECREATELAYERORGANIZATIONFOREXISTINGAUTH0ORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['ReCreateLayerOrganizationForExistingAuth0OrganizationRequest']
_RECREATELAYERORGANIZATIONFOREXISTINGAUTH0ORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['ReCreateLayerOrganizationForExistingAuth0OrganizationResponse']
_UPDATEORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['UpdateOrganizationRequest']
_UPDATEORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['UpdateOrganizationResponse']
_GETORGANIZATIONINVITESREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationInvitesRequest']
_GETORGANIZATIONINVITESRESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationInvitesResponse']
_CREATEORGANIZATIONINVITEREQUEST = DESCRIPTOR.message_types_by_name['CreateOrganizationInviteRequest']
_CREATEORGANIZATIONINVITERESPONSE = DESCRIPTOR.message_types_by_name['CreateOrganizationInviteResponse']
_REVOKEORGANIZATIONINVITEREQUEST = DESCRIPTOR.message_types_by_name['RevokeOrganizationInviteRequest']
_REVOKEORGANIZATIONINVITERESPONSE = DESCRIPTOR.message_types_by_name['RevokeOrganizationInviteResponse']
_TOGGLEORGANIZATIONACTIVATIONREQUEST = DESCRIPTOR.message_types_by_name['ToggleOrganizationActivationRequest']
_TOGGLEORGANIZATIONACTIVATIONRESPONSE = DESCRIPTOR.message_types_by_name['ToggleOrganizationActivationResponse']
_REMOVEUSERFROMORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['RemoveUserFromOrganizationRequest']
_REMOVEUSERFROMORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['RemoveUserFromOrganizationResponse']
_GETCONNECTIONSREQUEST = DESCRIPTOR.message_types_by_name['GetConnectionsRequest']
_GETCONNECTIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetConnectionsResponse']
_ENABLECONNECTIONFORORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['EnableConnectionForOrganizationRequest']
_ENABLECONNECTIONFORORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['EnableConnectionForOrganizationResponse']
_GETMYORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['GetMyOrganizationRequest']
_GETMYORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetMyOrganizationResponse']
_ASSIGNTIERTOORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['AssignTierToOrganizationRequest']
_ASSIGNTIERTOORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['AssignTierToOrganizationResponse']
_GETMYTIERREQUEST = DESCRIPTOR.message_types_by_name['GetMyTierRequest']
_GETMYTIERRESPONSE = DESCRIPTOR.message_types_by_name['GetMyTierResponse']
_GETGUESTAUTHTOKENREQUEST = DESCRIPTOR.message_types_by_name['GetGuestAuthTokenRequest']
_GETGUESTAUTHTOKENRESPONSE = DESCRIPTOR.message_types_by_name['GetGuestAuthTokenResponse']
GetMyUserRequest = _reflection.GeneratedProtocolMessageType('GetMyUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMYUSERREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyUserRequest)
  })
_sym_db.RegisterMessage(GetMyUserRequest)

GetMyUserResponse = _reflection.GeneratedProtocolMessageType('GetMyUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMYUSERRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyUserResponse)
  })
_sym_db.RegisterMessage(GetMyUserResponse)

GetMyPermissionsRequest = _reflection.GeneratedProtocolMessageType('GetMyPermissionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMYPERMISSIONSREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyPermissionsRequest)
  })
_sym_db.RegisterMessage(GetMyPermissionsRequest)

GetMyPermissionsResponse = _reflection.GeneratedProtocolMessageType('GetMyPermissionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMYPERMISSIONSRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyPermissionsResponse)
  })
_sym_db.RegisterMessage(GetMyPermissionsResponse)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)

GetOrganizationsRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONSREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationsRequest)
  })
_sym_db.RegisterMessage(GetOrganizationsRequest)

GetOrganizationsResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONSRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationsResponse)
  })
_sym_db.RegisterMessage(GetOrganizationsResponse)

GetOrganizationMembersRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationMembersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONMEMBERSREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationMembersRequest)
  })
_sym_db.RegisterMessage(GetOrganizationMembersRequest)

GetOrganizationMembersResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationMembersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONMEMBERSRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationMembersResponse)
  })
_sym_db.RegisterMessage(GetOrganizationMembersResponse)

GetOrganizationByNameRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONBYNAMEREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationByNameRequest)
  })
_sym_db.RegisterMessage(GetOrganizationByNameRequest)

GetOrganizationByNameResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONBYNAMERESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationByNameResponse)
  })
_sym_db.RegisterMessage(GetOrganizationByNameResponse)

GetOrganizationViewByNameRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationViewByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONVIEWBYNAMEREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationViewByNameRequest)
  })
_sym_db.RegisterMessage(GetOrganizationViewByNameRequest)

GetOrganizationViewByNameResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationViewByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONVIEWBYNAMERESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationViewByNameResponse)
  })
_sym_db.RegisterMessage(GetOrganizationViewByNameResponse)

GetOrganizationViewByIdRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationViewByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONVIEWBYIDREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationViewByIdRequest)
  })
_sym_db.RegisterMessage(GetOrganizationViewByIdRequest)

GetOrganizationViewByIdResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationViewByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONVIEWBYIDRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationViewByIdResponse)
  })
_sym_db.RegisterMessage(GetOrganizationViewByIdResponse)

GetOrganizationNameByIdRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationNameByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONNAMEBYIDREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationNameByIdRequest)
  })
_sym_db.RegisterMessage(GetOrganizationNameByIdRequest)

GetOrganizationNameByIdResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationNameByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONNAMEBYIDRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationNameByIdResponse)
  })
_sym_db.RegisterMessage(GetOrganizationNameByIdResponse)

ReCreateLayerOrganizationForExistingAuth0OrganizationRequest = _reflection.GeneratedProtocolMessageType('ReCreateLayerOrganizationForExistingAuth0OrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECREATELAYERORGANIZATIONFOREXISTINGAUTH0ORGANIZATIONREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ReCreateLayerOrganizationForExistingAuth0OrganizationRequest)
  })
_sym_db.RegisterMessage(ReCreateLayerOrganizationForExistingAuth0OrganizationRequest)

ReCreateLayerOrganizationForExistingAuth0OrganizationResponse = _reflection.GeneratedProtocolMessageType('ReCreateLayerOrganizationForExistingAuth0OrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECREATELAYERORGANIZATIONFOREXISTINGAUTH0ORGANIZATIONRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ReCreateLayerOrganizationForExistingAuth0OrganizationResponse)
  })
_sym_db.RegisterMessage(ReCreateLayerOrganizationForExistingAuth0OrganizationResponse)

UpdateOrganizationRequest = _reflection.GeneratedProtocolMessageType('UpdateOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORGANIZATIONREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateOrganizationRequest)
  })
_sym_db.RegisterMessage(UpdateOrganizationRequest)

UpdateOrganizationResponse = _reflection.GeneratedProtocolMessageType('UpdateOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORGANIZATIONRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateOrganizationResponse)
  })
_sym_db.RegisterMessage(UpdateOrganizationResponse)

GetOrganizationInvitesRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationInvitesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONINVITESREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationInvitesRequest)
  })
_sym_db.RegisterMessage(GetOrganizationInvitesRequest)

GetOrganizationInvitesResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationInvitesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONINVITESRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetOrganizationInvitesResponse)
  })
_sym_db.RegisterMessage(GetOrganizationInvitesResponse)

CreateOrganizationInviteRequest = _reflection.GeneratedProtocolMessageType('CreateOrganizationInviteRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGANIZATIONINVITEREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateOrganizationInviteRequest)
  })
_sym_db.RegisterMessage(CreateOrganizationInviteRequest)

CreateOrganizationInviteResponse = _reflection.GeneratedProtocolMessageType('CreateOrganizationInviteResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGANIZATIONINVITERESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.CreateOrganizationInviteResponse)
  })
_sym_db.RegisterMessage(CreateOrganizationInviteResponse)

RevokeOrganizationInviteRequest = _reflection.GeneratedProtocolMessageType('RevokeOrganizationInviteRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEORGANIZATIONINVITEREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.RevokeOrganizationInviteRequest)
  })
_sym_db.RegisterMessage(RevokeOrganizationInviteRequest)

RevokeOrganizationInviteResponse = _reflection.GeneratedProtocolMessageType('RevokeOrganizationInviteResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEORGANIZATIONINVITERESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.RevokeOrganizationInviteResponse)
  })
_sym_db.RegisterMessage(RevokeOrganizationInviteResponse)

ToggleOrganizationActivationRequest = _reflection.GeneratedProtocolMessageType('ToggleOrganizationActivationRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEORGANIZATIONACTIVATIONREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ToggleOrganizationActivationRequest)
  })
_sym_db.RegisterMessage(ToggleOrganizationActivationRequest)

ToggleOrganizationActivationResponse = _reflection.GeneratedProtocolMessageType('ToggleOrganizationActivationResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEORGANIZATIONACTIVATIONRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.ToggleOrganizationActivationResponse)
  })
_sym_db.RegisterMessage(ToggleOrganizationActivationResponse)

RemoveUserFromOrganizationRequest = _reflection.GeneratedProtocolMessageType('RemoveUserFromOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEUSERFROMORGANIZATIONREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.RemoveUserFromOrganizationRequest)
  })
_sym_db.RegisterMessage(RemoveUserFromOrganizationRequest)

RemoveUserFromOrganizationResponse = _reflection.GeneratedProtocolMessageType('RemoveUserFromOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEUSERFROMORGANIZATIONRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.RemoveUserFromOrganizationResponse)
  })
_sym_db.RegisterMessage(RemoveUserFromOrganizationResponse)

GetConnectionsRequest = _reflection.GeneratedProtocolMessageType('GetConnectionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTIONSREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetConnectionsRequest)
  })
_sym_db.RegisterMessage(GetConnectionsRequest)

GetConnectionsResponse = _reflection.GeneratedProtocolMessageType('GetConnectionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTIONSRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetConnectionsResponse)
  })
_sym_db.RegisterMessage(GetConnectionsResponse)

EnableConnectionForOrganizationRequest = _reflection.GeneratedProtocolMessageType('EnableConnectionForOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENABLECONNECTIONFORORGANIZATIONREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.EnableConnectionForOrganizationRequest)
  })
_sym_db.RegisterMessage(EnableConnectionForOrganizationRequest)

EnableConnectionForOrganizationResponse = _reflection.GeneratedProtocolMessageType('EnableConnectionForOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENABLECONNECTIONFORORGANIZATIONRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.EnableConnectionForOrganizationResponse)
  })
_sym_db.RegisterMessage(EnableConnectionForOrganizationResponse)

GetMyOrganizationRequest = _reflection.GeneratedProtocolMessageType('GetMyOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMYORGANIZATIONREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyOrganizationRequest)
  })
_sym_db.RegisterMessage(GetMyOrganizationRequest)

GetMyOrganizationResponse = _reflection.GeneratedProtocolMessageType('GetMyOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMYORGANIZATIONRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyOrganizationResponse)
  })
_sym_db.RegisterMessage(GetMyOrganizationResponse)

AssignTierToOrganizationRequest = _reflection.GeneratedProtocolMessageType('AssignTierToOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNTIERTOORGANIZATIONREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.AssignTierToOrganizationRequest)
  })
_sym_db.RegisterMessage(AssignTierToOrganizationRequest)

AssignTierToOrganizationResponse = _reflection.GeneratedProtocolMessageType('AssignTierToOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNTIERTOORGANIZATIONRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.AssignTierToOrganizationResponse)
  })
_sym_db.RegisterMessage(AssignTierToOrganizationResponse)

GetMyTierRequest = _reflection.GeneratedProtocolMessageType('GetMyTierRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMYTIERREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyTierRequest)
  })
_sym_db.RegisterMessage(GetMyTierRequest)

GetMyTierResponse = _reflection.GeneratedProtocolMessageType('GetMyTierResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMYTIERRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetMyTierResponse)
  })
_sym_db.RegisterMessage(GetMyTierResponse)

GetGuestAuthTokenRequest = _reflection.GeneratedProtocolMessageType('GetGuestAuthTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGUESTAUTHTOKENREQUEST,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetGuestAuthTokenRequest)
  })
_sym_db.RegisterMessage(GetGuestAuthTokenRequest)

GetGuestAuthTokenResponse = _reflection.GeneratedProtocolMessageType('GetGuestAuthTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGUESTAUTHTOKENRESPONSE,
  '__module__' : 'api.service.account.user_api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetGuestAuthTokenResponse)
  })
_sym_db.RegisterMessage(GetGuestAuthTokenResponse)

_USERAPI = DESCRIPTOR.services_by_name['UserAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiB\014UserApiProtoP\001'
  _GETORGANIZATIONBYNAMEREQUEST.fields_by_name['name']._options = None
  _GETORGANIZATIONBYNAMEREQUEST.fields_by_name['name']._serialized_options = b'\372B\007r\005\020\001\030\200\002'
  _GETORGANIZATIONVIEWBYNAMEREQUEST.fields_by_name['name']._options = None
  _GETORGANIZATIONVIEWBYNAMEREQUEST.fields_by_name['name']._serialized_options = b'\372B\007r\005\020\001\030\200\002'
  _GETORGANIZATIONVIEWBYNAMERESPONSE.fields_by_name['display_name']._options = None
  _GETORGANIZATIONVIEWBYNAMERESPONSE.fields_by_name['display_name']._serialized_options = b'\372B\007r\005\020\001\030\200\002'
  _USERAPI.methods_by_name['GetGuestAuthToken']._options = None
  _USERAPI.methods_by_name['GetGuestAuthToken']._serialized_options = b'\300\265\030\001'
  _GETMYUSERREQUEST._serialized_start=305
  _GETMYUSERREQUEST._serialized_end=323
  _GETMYUSERRESPONSE._serialized_start=325
  _GETMYUSERRESPONSE._serialized_end=369
  _GETMYPERMISSIONSREQUEST._serialized_start=371
  _GETMYPERMISSIONSREQUEST._serialized_end=396
  _GETMYPERMISSIONSRESPONSE._serialized_start=398
  _GETMYPERMISSIONSRESPONSE._serialized_end=445
  _GETUSERREQUEST._serialized_start=447
  _GETUSERREQUEST._serialized_end=493
  _GETUSERRESPONSE._serialized_start=495
  _GETUSERRESPONSE._serialized_end=537
  _GETORGANIZATIONSREQUEST._serialized_start=539
  _GETORGANIZATIONSREQUEST._serialized_end=564
  _GETORGANIZATIONSRESPONSE._serialized_start=566
  _GETORGANIZATIONSRESPONSE._serialized_end=634
  _GETORGANIZATIONMEMBERSREQUEST._serialized_start=636
  _GETORGANIZATIONMEMBERSREQUEST._serialized_end=724
  _GETORGANIZATIONMEMBERSRESPONSE._serialized_start=726
  _GETORGANIZATIONMEMBERSRESPONSE._serialized_end=799
  _GETORGANIZATIONBYNAMEREQUEST._serialized_start=801
  _GETORGANIZATIONBYNAMEREQUEST._serialized_end=857
  _GETORGANIZATIONBYNAMERESPONSE._serialized_start=859
  _GETORGANIZATIONBYNAMERESPONSE._serialized_end=931
  _GETORGANIZATIONVIEWBYNAMEREQUEST._serialized_start=933
  _GETORGANIZATIONVIEWBYNAMEREQUEST._serialized_end=993
  _GETORGANIZATIONVIEWBYNAMERESPONSE._serialized_start=996
  _GETORGANIZATIONVIEWBYNAMERESPONSE._serialized_end=1138
  _GETORGANIZATIONVIEWBYIDREQUEST._serialized_start=1140
  _GETORGANIZATIONVIEWBYIDREQUEST._serialized_end=1218
  _GETORGANIZATIONVIEWBYIDRESPONSE._serialized_start=1220
  _GETORGANIZATIONVIEWBYIDRESPONSE._serialized_end=1303
  _GETORGANIZATIONNAMEBYIDREQUEST._serialized_start=1305
  _GETORGANIZATIONNAMEBYIDREQUEST._serialized_end=1383
  _GETORGANIZATIONNAMEBYIDRESPONSE._serialized_start=1385
  _GETORGANIZATIONNAMEBYIDRESPONSE._serialized_end=1445
  _RECREATELAYERORGANIZATIONFOREXISTINGAUTH0ORGANIZATIONREQUEST._serialized_start=1448
  _RECREATELAYERORGANIZATIONFOREXISTINGAUTH0ORGANIZATIONREQUEST._serialized_end=1643
  _RECREATELAYERORGANIZATIONFOREXISTINGAUTH0ORGANIZATIONRESPONSE._serialized_start=1645
  _RECREATELAYERORGANIZATIONFOREXISTINGAUTH0ORGANIZATIONRESPONSE._serialized_end=1749
  _UPDATEORGANIZATIONREQUEST._serialized_start=1751
  _UPDATEORGANIZATIONREQUEST._serialized_end=1831
  _UPDATEORGANIZATIONRESPONSE._serialized_start=1833
  _UPDATEORGANIZATIONRESPONSE._serialized_end=1902
  _GETORGANIZATIONINVITESREQUEST._serialized_start=1904
  _GETORGANIZATIONINVITESREQUEST._serialized_end=1992
  _GETORGANIZATIONINVITESRESPONSE._serialized_start=1994
  _GETORGANIZATIONINVITESRESPONSE._serialized_end=2081
  _CREATEORGANIZATIONINVITEREQUEST._serialized_start=2084
  _CREATEORGANIZATIONINVITEREQUEST._serialized_end=2256
  _CREATEORGANIZATIONINVITERESPONSE._serialized_start=2258
  _CREATEORGANIZATIONINVITERESPONSE._serialized_end=2346
  _REVOKEORGANIZATIONINVITEREQUEST._serialized_start=2349
  _REVOKEORGANIZATIONINVITEREQUEST._serialized_end=2478
  _REVOKEORGANIZATIONINVITERESPONSE._serialized_start=2480
  _REVOKEORGANIZATIONINVITERESPONSE._serialized_end=2571
  _TOGGLEORGANIZATIONACTIVATIONREQUEST._serialized_start=2573
  _TOGGLEORGANIZATIONACTIVATIONREQUEST._serialized_end=2678
  _TOGGLEORGANIZATIONACTIVATIONRESPONSE._serialized_start=2680
  _TOGGLEORGANIZATIONACTIVATIONRESPONSE._serialized_end=2759
  _REMOVEUSERFROMORGANIZATIONREQUEST._serialized_start=2761
  _REMOVEUSERFROMORGANIZATIONREQUEST._serialized_end=2883
  _REMOVEUSERFROMORGANIZATIONRESPONSE._serialized_start=2885
  _REMOVEUSERFROMORGANIZATIONRESPONSE._serialized_end=2978
  _GETCONNECTIONSREQUEST._serialized_start=2980
  _GETCONNECTIONSREQUEST._serialized_end=3003
  _GETCONNECTIONSRESPONSE._serialized_start=3005
  _GETCONNECTIONSRESPONSE._serialized_end=3067
  _ENABLECONNECTIONFORORGANIZATIONREQUEST._serialized_start=3070
  _ENABLECONNECTIONFORORGANIZATIONREQUEST._serialized_end=3209
  _ENABLECONNECTIONFORORGANIZATIONRESPONSE._serialized_start=3211
  _ENABLECONNECTIONFORORGANIZATIONRESPONSE._serialized_end=3294
  _GETMYORGANIZATIONREQUEST._serialized_start=3296
  _GETMYORGANIZATIONREQUEST._serialized_end=3322
  _GETMYORGANIZATIONRESPONSE._serialized_start=3324
  _GETMYORGANIZATIONRESPONSE._serialized_end=3392
  _ASSIGNTIERTOORGANIZATIONREQUEST._serialized_start=3394
  _ASSIGNTIERTOORGANIZATIONREQUEST._serialized_end=3503
  _ASSIGNTIERTOORGANIZATIONRESPONSE._serialized_start=3505
  _ASSIGNTIERTOORGANIZATIONRESPONSE._serialized_end=3580
  _GETMYTIERREQUEST._serialized_start=3582
  _GETMYTIERREQUEST._serialized_end=3600
  _GETMYTIERRESPONSE._serialized_start=3602
  _GETMYTIERRESPONSE._serialized_end=3646
  _GETGUESTAUTHTOKENREQUEST._serialized_start=3648
  _GETGUESTAUTHTOKENREQUEST._serialized_end=3674
  _GETGUESTAUTHTOKENRESPONSE._serialized_start=3676
  _GETGUESTAUTHTOKENRESPONSE._serialized_end=3718
  _USERAPI._serialized_start=3721
  _USERAPI._serialized_end=5870
# @@protoc_insertion_point(module_scope)
