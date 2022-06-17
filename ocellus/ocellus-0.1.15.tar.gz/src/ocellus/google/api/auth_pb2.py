# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15google/api/auth.proto\x12\ngoogle.api\x1a\x1cgoogle/api/annotations.proto\"l\n\x0e\x41uthentication\x12-\n\x05rules\x18\x03 \x03(\x0b\x32\x1e.google.api.AuthenticationRule\x12+\n\tproviders\x18\x04 \x03(\x0b\x32\x18.google.api.AuthProvider\"\xa9\x01\n\x12\x41uthenticationRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12,\n\x05oauth\x18\x02 \x01(\x0b\x32\x1d.google.api.OAuthRequirements\x12 \n\x18\x61llow_without_credential\x18\x05 \x01(\x08\x12\x31\n\x0crequirements\x18\x07 \x03(\x0b\x32\x1b.google.api.AuthRequirement\"j\n\x0c\x41uthProvider\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06issuer\x18\x02 \x01(\t\x12\x10\n\x08jwks_uri\x18\x03 \x01(\t\x12\x11\n\taudiences\x18\x04 \x01(\t\x12\x19\n\x11\x61uthorization_url\x18\x05 \x01(\t\"-\n\x11OAuthRequirements\x12\x18\n\x10\x63\x61nonical_scopes\x18\x01 \x01(\t\"9\n\x0f\x41uthRequirement\x12\x13\n\x0bprovider_id\x18\x01 \x01(\t\x12\x11\n\taudiences\x18\x02 \x01(\tBk\n\x0e\x63om.google.apiB\tAuthProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')



_AUTHENTICATION = DESCRIPTOR.message_types_by_name['Authentication']
_AUTHENTICATIONRULE = DESCRIPTOR.message_types_by_name['AuthenticationRule']
_AUTHPROVIDER = DESCRIPTOR.message_types_by_name['AuthProvider']
_OAUTHREQUIREMENTS = DESCRIPTOR.message_types_by_name['OAuthRequirements']
_AUTHREQUIREMENT = DESCRIPTOR.message_types_by_name['AuthRequirement']
Authentication = _reflection.GeneratedProtocolMessageType('Authentication', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATION,
  '__module__' : 'google.api.auth_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Authentication)
  })
_sym_db.RegisterMessage(Authentication)

AuthenticationRule = _reflection.GeneratedProtocolMessageType('AuthenticationRule', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATIONRULE,
  '__module__' : 'google.api.auth_pb2'
  # @@protoc_insertion_point(class_scope:google.api.AuthenticationRule)
  })
_sym_db.RegisterMessage(AuthenticationRule)

AuthProvider = _reflection.GeneratedProtocolMessageType('AuthProvider', (_message.Message,), {
  'DESCRIPTOR' : _AUTHPROVIDER,
  '__module__' : 'google.api.auth_pb2'
  # @@protoc_insertion_point(class_scope:google.api.AuthProvider)
  })
_sym_db.RegisterMessage(AuthProvider)

OAuthRequirements = _reflection.GeneratedProtocolMessageType('OAuthRequirements', (_message.Message,), {
  'DESCRIPTOR' : _OAUTHREQUIREMENTS,
  '__module__' : 'google.api.auth_pb2'
  # @@protoc_insertion_point(class_scope:google.api.OAuthRequirements)
  })
_sym_db.RegisterMessage(OAuthRequirements)

AuthRequirement = _reflection.GeneratedProtocolMessageType('AuthRequirement', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQUIREMENT,
  '__module__' : 'google.api.auth_pb2'
  # @@protoc_insertion_point(class_scope:google.api.AuthRequirement)
  })
_sym_db.RegisterMessage(AuthRequirement)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.google.apiB\tAuthProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI'
  _AUTHENTICATION._serialized_start=67
  _AUTHENTICATION._serialized_end=175
  _AUTHENTICATIONRULE._serialized_start=178
  _AUTHENTICATIONRULE._serialized_end=347
  _AUTHPROVIDER._serialized_start=349
  _AUTHPROVIDER._serialized_end=455
  _OAUTHREQUIREMENTS._serialized_start=457
  _OAUTHREQUIREMENTS._serialized_end=502
  _AUTHREQUIREMENT._serialized_start=504
  _AUTHREQUIREMENT._serialized_end=561
# @@protoc_insertion_point(module_scope)
