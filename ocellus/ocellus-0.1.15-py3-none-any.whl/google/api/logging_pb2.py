# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/logging.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18google/api/logging.proto\x12\ngoogle.api\x1a\x1cgoogle/api/annotations.proto\"\xd7\x01\n\x07Logging\x12\x45\n\x15producer_destinations\x18\x01 \x03(\x0b\x32&.google.api.Logging.LoggingDestination\x12\x45\n\x15\x63onsumer_destinations\x18\x02 \x03(\x0b\x32&.google.api.Logging.LoggingDestination\x1a>\n\x12LoggingDestination\x12\x1a\n\x12monitored_resource\x18\x03 \x01(\t\x12\x0c\n\x04logs\x18\x01 \x03(\tBn\n\x0e\x63om.google.apiB\x0cLoggingProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')



_LOGGING = DESCRIPTOR.message_types_by_name['Logging']
_LOGGING_LOGGINGDESTINATION = _LOGGING.nested_types_by_name['LoggingDestination']
Logging = _reflection.GeneratedProtocolMessageType('Logging', (_message.Message,), {

  'LoggingDestination' : _reflection.GeneratedProtocolMessageType('LoggingDestination', (_message.Message,), {
    'DESCRIPTOR' : _LOGGING_LOGGINGDESTINATION,
    '__module__' : 'google.api.logging_pb2'
    # @@protoc_insertion_point(class_scope:google.api.Logging.LoggingDestination)
    })
  ,
  'DESCRIPTOR' : _LOGGING,
  '__module__' : 'google.api.logging_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Logging)
  })
_sym_db.RegisterMessage(Logging)
_sym_db.RegisterMessage(Logging.LoggingDestination)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.google.apiB\014LoggingProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI'
  _LOGGING._serialized_start=71
  _LOGGING._serialized_end=286
  _LOGGING_LOGGINGDESTINATION._serialized_start=224
  _LOGGING_LOGGINGDESTINATION._serialized_end=286
# @@protoc_insertion_point(module_scope)
