# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/function/trace_type/serialization_test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.function.trace_type import serialization_pb2 as tensorflow_dot_core_dot_function_dot_trace__type_dot_serialization__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/function/trace_type/serialization_test.proto',
  package='tensorflow.core.function.trace_type.serialization_test',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n<tensorflow/core/function/trace_type/serialization_test.proto\x12\x36tensorflow.core.function.trace_type.serialization_test\x1a\x37tensorflow/core/function/trace_type/serialization.proto\"5\n\x16MyCustomRepresentation\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"u\n\x19MyCompositeRepresentation\x12X\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x46.tensorflow.core.function.trace_type.serialization.SerializedTraceType')
  ,
  dependencies=[tensorflow_dot_core_dot_function_dot_trace__type_dot_serialization__pb2.DESCRIPTOR,])




_MYCUSTOMREPRESENTATION = _descriptor.Descriptor(
  name='MyCustomRepresentation',
  full_name='tensorflow.core.function.trace_type.serialization_test.MyCustomRepresentation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='tensorflow.core.function.trace_type.serialization_test.MyCustomRepresentation.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.core.function.trace_type.serialization_test.MyCustomRepresentation.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=230,
)


_MYCOMPOSITEREPRESENTATION = _descriptor.Descriptor(
  name='MyCompositeRepresentation',
  full_name='tensorflow.core.function.trace_type.serialization_test.MyCompositeRepresentation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='tensorflow.core.function.trace_type.serialization_test.MyCompositeRepresentation.elements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=349,
)

_MYCOMPOSITEREPRESENTATION.fields_by_name['elements'].message_type = tensorflow_dot_core_dot_function_dot_trace__type_dot_serialization__pb2._SERIALIZEDTRACETYPE
DESCRIPTOR.message_types_by_name['MyCustomRepresentation'] = _MYCUSTOMREPRESENTATION
DESCRIPTOR.message_types_by_name['MyCompositeRepresentation'] = _MYCOMPOSITEREPRESENTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MyCustomRepresentation = _reflection.GeneratedProtocolMessageType('MyCustomRepresentation', (_message.Message,), {
  'DESCRIPTOR' : _MYCUSTOMREPRESENTATION,
  '__module__' : 'tensorflow.core.function.trace_type.serialization_test_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.core.function.trace_type.serialization_test.MyCustomRepresentation)
  })
_sym_db.RegisterMessage(MyCustomRepresentation)

MyCompositeRepresentation = _reflection.GeneratedProtocolMessageType('MyCompositeRepresentation', (_message.Message,), {
  'DESCRIPTOR' : _MYCOMPOSITEREPRESENTATION,
  '__module__' : 'tensorflow.core.function.trace_type.serialization_test_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.core.function.trace_type.serialization_test.MyCompositeRepresentation)
  })
_sym_db.RegisterMessage(MyCompositeRepresentation)


# @@protoc_insertion_point(module_scope)
