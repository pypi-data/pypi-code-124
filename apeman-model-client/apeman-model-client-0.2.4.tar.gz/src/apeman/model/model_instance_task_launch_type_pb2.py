# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apeman/model/model_instance_task_launch_type.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2apeman/model/model_instance_task_launch_type.proto*A\n\x1bModelInstanceTaskLaunchType\x12\x0e\n\nTASK_ADHOC\x10\x00\x12\x12\n\x0eTASK_SCHEDULED\x10\x01\x42\x44\n\x1e\x63om.apeman.meta.grpc.lib.modelB ModelInstanceTaskLaunchTypeProtoP\x01\x62\x06proto3')

_MODELINSTANCETASKLAUNCHTYPE = DESCRIPTOR.enum_types_by_name['ModelInstanceTaskLaunchType']
ModelInstanceTaskLaunchType = enum_type_wrapper.EnumTypeWrapper(_MODELINSTANCETASKLAUNCHTYPE)
TASK_ADHOC = 0
TASK_SCHEDULED = 1


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.apeman.meta.grpc.lib.modelB ModelInstanceTaskLaunchTypeProtoP\001'
  _MODELINSTANCETASKLAUNCHTYPE._serialized_start=54
  _MODELINSTANCETASKLAUNCHTYPE._serialized_end=119
# @@protoc_insertion_point(module_scope)
