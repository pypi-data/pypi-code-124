# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apeman/model/model_instance_task_type.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+apeman/model/model_instance_task_type.proto*;\n\x15ModelInstanceTaskType\x12\x0e\n\nTASK_TRAIN\x10\x00\x12\x12\n\x0eTASK_INFERENCE\x10\x01\x42>\n\x1e\x63om.apeman.meta.grpc.lib.modelB\x1aModelInstanceTaskTypeProtoP\x01\x62\x06proto3')

_MODELINSTANCETASKTYPE = DESCRIPTOR.enum_types_by_name['ModelInstanceTaskType']
ModelInstanceTaskType = enum_type_wrapper.EnumTypeWrapper(_MODELINSTANCETASKTYPE)
TASK_TRAIN = 0
TASK_INFERENCE = 1


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.apeman.meta.grpc.lib.modelB\032ModelInstanceTaskTypeProtoP\001'
  _MODELINSTANCETASKTYPE._serialized_start=47
  _MODELINSTANCETASKTYPE._serialized_end=106
# @@protoc_insertion_point(module_scope)
