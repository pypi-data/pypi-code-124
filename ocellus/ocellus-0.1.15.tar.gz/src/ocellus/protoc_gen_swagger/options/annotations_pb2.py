# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoc-gen-swagger/options/annotations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from protoc_gen_swagger.options import openapiv2_pb2 as protoc__gen__swagger_dot_options_dot_openapiv2__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,protoc-gen-swagger/options/annotations.proto\x12\'grpc.gateway.protoc_gen_swagger.options\x1a google/protobuf/descriptor.proto\x1a*protoc-gen-swagger/options/openapiv2.proto:j\n\x11openapiv2_swagger\x12\x1c.google.protobuf.FileOptions\x18\x92\x08 \x01(\x0b\x32\x30.grpc.gateway.protoc_gen_swagger.options.Swagger:p\n\x13openapiv2_operation\x12\x1e.google.protobuf.MethodOptions\x18\x92\x08 \x01(\x0b\x32\x32.grpc.gateway.protoc_gen_swagger.options.Operation:k\n\x10openapiv2_schema\x12\x1f.google.protobuf.MessageOptions\x18\x92\x08 \x01(\x0b\x32/.grpc.gateway.protoc_gen_swagger.options.Schema:e\n\ropenapiv2_tag\x12\x1f.google.protobuf.ServiceOptions\x18\x92\x08 \x01(\x0b\x32,.grpc.gateway.protoc_gen_swagger.options.Tag:l\n\x0fopenapiv2_field\x12\x1d.google.protobuf.FieldOptions\x18\x92\x08 \x01(\x0b\x32\x33.grpc.gateway.protoc_gen_swagger.options.JSONSchemaBCZAgithub.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/optionsb\x06proto3')


OPENAPIV2_SWAGGER_FIELD_NUMBER = 1042
openapiv2_swagger = DESCRIPTOR.extensions_by_name['openapiv2_swagger']
OPENAPIV2_OPERATION_FIELD_NUMBER = 1042
openapiv2_operation = DESCRIPTOR.extensions_by_name['openapiv2_operation']
OPENAPIV2_SCHEMA_FIELD_NUMBER = 1042
openapiv2_schema = DESCRIPTOR.extensions_by_name['openapiv2_schema']
OPENAPIV2_TAG_FIELD_NUMBER = 1042
openapiv2_tag = DESCRIPTOR.extensions_by_name['openapiv2_tag']
OPENAPIV2_FIELD_FIELD_NUMBER = 1042
openapiv2_field = DESCRIPTOR.extensions_by_name['openapiv2_field']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(openapiv2_swagger)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(openapiv2_operation)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(openapiv2_schema)
  google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(openapiv2_tag)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(openapiv2_field)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZAgithub.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options'
# @@protoc_insertion_point(module_scope)
