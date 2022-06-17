# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lndgrpc/compiled/lncli.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lndgrpc.compiled import verrpc_pb2 as lndgrpc_dot_compiled_dot_verrpc__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lndgrpc/compiled/lncli.proto',
  package='lnclipb',
  syntax='proto3',
  serialized_options=b'Z-github.com/lightningnetwork/lnd/lnrpc/lnclipb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1clndgrpc/compiled/lncli.proto\x12\x07lnclipb\x1a\x1dlndgrpc/compiled/verrpc.proto\"O\n\x0fVersionResponse\x12\x1e\n\x05lncli\x18\x01 \x01(\x0b\x32\x0f.verrpc.Version\x12\x1c\n\x03lnd\x18\x02 \x01(\x0b\x32\x0f.verrpc.VersionB/Z-github.com/lightningnetwork/lnd/lnrpc/lnclipbb\x06proto3'
  ,
  dependencies=[lndgrpc_dot_compiled_dot_verrpc__pb2.DESCRIPTOR,])




_VERSIONRESPONSE = _descriptor.Descriptor(
  name='VersionResponse',
  full_name='lnclipb.VersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lncli', full_name='lnclipb.VersionResponse.lncli', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lnd', full_name='lnclipb.VersionResponse.lnd', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=151,
)

_VERSIONRESPONSE.fields_by_name['lncli'].message_type = lndgrpc_dot_compiled_dot_verrpc__pb2._VERSION
_VERSIONRESPONSE.fields_by_name['lnd'].message_type = lndgrpc_dot_compiled_dot_verrpc__pb2._VERSION
DESCRIPTOR.message_types_by_name['VersionResponse'] = _VERSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VersionResponse = _reflection.GeneratedProtocolMessageType('VersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONRESPONSE,
  '__module__' : 'lndgrpc.compiled.lncli_pb2'
  # @@protoc_insertion_point(class_scope:lnclipb.VersionResponse)
  })
_sym_db.RegisterMessage(VersionResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
