# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import label_pb2 as google_dot_api_dot_label__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14google/api/log.proto\x12\ngoogle.api\x1a\x16google/api/label.proto\"u\n\rLogDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x06labels\x18\x02 \x03(\x0b\x32\x1b.google.api.LabelDescriptor\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\tBj\n\x0e\x63om.google.apiB\x08LogProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')



_LOGDESCRIPTOR = DESCRIPTOR.message_types_by_name['LogDescriptor']
LogDescriptor = _reflection.GeneratedProtocolMessageType('LogDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _LOGDESCRIPTOR,
  '__module__' : 'google.api.log_pb2'
  # @@protoc_insertion_point(class_scope:google.api.LogDescriptor)
  })
_sym_db.RegisterMessage(LogDescriptor)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.google.apiB\010LogProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI'
  _LOGDESCRIPTOR._serialized_start=60
  _LOGDESCRIPTOR._serialized_end=177
# @@protoc_insertion_point(module_scope)
