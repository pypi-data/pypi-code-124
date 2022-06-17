# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ocellus_module_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ocellus_types_pb2 as ocellus__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cocellus_module_service.proto\x12\x07ocellus\x1a\x13ocellus_types.proto\":\n\nStateEvent\x12\x1b\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\r.ocellus.Data\x12\x0f\n\x07\x66rameId\x18\x04 \x01(\x03\";\n\x06IOData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\x11.ocellus.DataType\"f\n\x0b\x42indRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x06inputs\x18\x03 \x03(\x0b\x32\x0f.ocellus.IODataB\x02\x18\x01\x12$\n\x07outputs\x18\x04 \x03(\x0b\x32\x0f.ocellus.IODataB\x02\x18\x01\"\xa0\x03\n\nOutputData\x12\'\n\nintrinsics\x18\x01 \x01(\x0b\x32\x13.ocellus.Intrinsics\x12\"\n\x08\x63ontours\x18\x02 \x03(\x0b\x32\x10.ocellus.Contour\x12\x1f\n\x06\x63\x61mera\x18\x03 \x01(\x0b\x32\x0f.ocellus.Camera\x12(\n\x05image\x18\x04 \x01(\x0b\x32\x19.ocellus.OutputData.Image\x12\'\n\npointCloud\x18\x05 \x01(\x0b\x32\x13.ocellus.PointCloud\x12\x1c\n\x05items\x18\x06 \x03(\x0b\x32\r.ocellus.Item\x12\x0f\n\x07\x64\x65\x63imal\x18\x07 \x01(\x01\x12\x0f\n\x07integer\x18\x08 \x01(\x05\x12\x0e\n\x06string\x18\t \x01(\t\x12\x1e\n\x06\x65rrors\x18\n \x03(\x0b\x32\x0e.ocellus.Error\x12#\n\x08position\x18\x0b \x01(\x0b\x32\x11.ocellus.Position\x12%\n\x08rotation\x18\x0c \x01(\x0b\x32\x13.ocellus.Quaternion\x1a\x15\n\x05Image\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"i\n\nModuleData\x12+\n\x0b\x62indRequest\x18\x01 \x01(\x0b\x32\x14.ocellus.BindRequestH\x00\x12#\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x13.ocellus.OutputDataH\x00\x42\t\n\x07payload\"!\n\x12\x44ownloadRefRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\"h\n\nPointCloud\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12%\n\x08vertices\x18\x03 \x03(\x0b\x32\x13.ocellus.Vector3Dim\x12\x14\n\x0cmat32FC1Data\x18\x04 \x01(\x0c\"[\n\x13\x44ownloadRefResponse\x12\x0e\n\x04\x64\x61ta\x18\x01 \x01(\x0cH\x00\x12)\n\npointCloud\x18\x02 \x01(\x0b\x32\x13.ocellus.PointCloudH\x00\x42\t\n\x07payload2\x9a\x01\n\x14OcellusModuleService\x12\x36\n\x04\x42ind\x12\x13.ocellus.ModuleData\x1a\x13.ocellus.StateEvent\"\x00(\x01\x30\x01\x12J\n\x0b\x44ownloadRef\x12\x1b.ocellus.DownloadRefRequest\x1a\x1c.ocellus.DownloadRefResponse\"\x00\x42o\n\x16ocellus.servers.moduleB\x14OcellusModuleServiceP\x01Z\x1egithub.com/byte-motion/ocellus\xa2\x02\x03OSM\xaa\x02\x16Ocellus.Servers.Moduleb\x06proto3')



_STATEEVENT = DESCRIPTOR.message_types_by_name['StateEvent']
_IODATA = DESCRIPTOR.message_types_by_name['IOData']
_BINDREQUEST = DESCRIPTOR.message_types_by_name['BindRequest']
_OUTPUTDATA = DESCRIPTOR.message_types_by_name['OutputData']
_OUTPUTDATA_IMAGE = _OUTPUTDATA.nested_types_by_name['Image']
_MODULEDATA = DESCRIPTOR.message_types_by_name['ModuleData']
_DOWNLOADREFREQUEST = DESCRIPTOR.message_types_by_name['DownloadRefRequest']
_POINTCLOUD = DESCRIPTOR.message_types_by_name['PointCloud']
_DOWNLOADREFRESPONSE = DESCRIPTOR.message_types_by_name['DownloadRefResponse']
StateEvent = _reflection.GeneratedProtocolMessageType('StateEvent', (_message.Message,), {
  'DESCRIPTOR' : _STATEEVENT,
  '__module__' : 'ocellus_module_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.StateEvent)
  })
_sym_db.RegisterMessage(StateEvent)

IOData = _reflection.GeneratedProtocolMessageType('IOData', (_message.Message,), {
  'DESCRIPTOR' : _IODATA,
  '__module__' : 'ocellus_module_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.IOData)
  })
_sym_db.RegisterMessage(IOData)

BindRequest = _reflection.GeneratedProtocolMessageType('BindRequest', (_message.Message,), {
  'DESCRIPTOR' : _BINDREQUEST,
  '__module__' : 'ocellus_module_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.BindRequest)
  })
_sym_db.RegisterMessage(BindRequest)

OutputData = _reflection.GeneratedProtocolMessageType('OutputData', (_message.Message,), {

  'Image' : _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
    'DESCRIPTOR' : _OUTPUTDATA_IMAGE,
    '__module__' : 'ocellus_module_service_pb2'
    # @@protoc_insertion_point(class_scope:ocellus.OutputData.Image)
    })
  ,
  'DESCRIPTOR' : _OUTPUTDATA,
  '__module__' : 'ocellus_module_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.OutputData)
  })
_sym_db.RegisterMessage(OutputData)
_sym_db.RegisterMessage(OutputData.Image)

ModuleData = _reflection.GeneratedProtocolMessageType('ModuleData', (_message.Message,), {
  'DESCRIPTOR' : _MODULEDATA,
  '__module__' : 'ocellus_module_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.ModuleData)
  })
_sym_db.RegisterMessage(ModuleData)

DownloadRefRequest = _reflection.GeneratedProtocolMessageType('DownloadRefRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADREFREQUEST,
  '__module__' : 'ocellus_module_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.DownloadRefRequest)
  })
_sym_db.RegisterMessage(DownloadRefRequest)

PointCloud = _reflection.GeneratedProtocolMessageType('PointCloud', (_message.Message,), {
  'DESCRIPTOR' : _POINTCLOUD,
  '__module__' : 'ocellus_module_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.PointCloud)
  })
_sym_db.RegisterMessage(PointCloud)

DownloadRefResponse = _reflection.GeneratedProtocolMessageType('DownloadRefResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADREFRESPONSE,
  '__module__' : 'ocellus_module_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.DownloadRefResponse)
  })
_sym_db.RegisterMessage(DownloadRefResponse)

_OCELLUSMODULESERVICE = DESCRIPTOR.services_by_name['OcellusModuleService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026ocellus.servers.moduleB\024OcellusModuleServiceP\001Z\036github.com/byte-motion/ocellus\242\002\003OSM\252\002\026Ocellus.Servers.Module'
  _BINDREQUEST.fields_by_name['inputs']._options = None
  _BINDREQUEST.fields_by_name['inputs']._serialized_options = b'\030\001'
  _BINDREQUEST.fields_by_name['outputs']._options = None
  _BINDREQUEST.fields_by_name['outputs']._serialized_options = b'\030\001'
  _STATEEVENT._serialized_start=62
  _STATEEVENT._serialized_end=120
  _IODATA._serialized_start=122
  _IODATA._serialized_end=181
  _BINDREQUEST._serialized_start=183
  _BINDREQUEST._serialized_end=285
  _OUTPUTDATA._serialized_start=288
  _OUTPUTDATA._serialized_end=704
  _OUTPUTDATA_IMAGE._serialized_start=683
  _OUTPUTDATA_IMAGE._serialized_end=704
  _MODULEDATA._serialized_start=706
  _MODULEDATA._serialized_end=811
  _DOWNLOADREFREQUEST._serialized_start=813
  _DOWNLOADREFREQUEST._serialized_end=846
  _POINTCLOUD._serialized_start=848
  _POINTCLOUD._serialized_end=952
  _DOWNLOADREFRESPONSE._serialized_start=954
  _DOWNLOADREFRESPONSE._serialized_end=1045
  _OCELLUSMODULESERVICE._serialized_start=1048
  _OCELLUSMODULESERVICE._serialized_end=1202
# @@protoc_insertion_point(module_scope)
