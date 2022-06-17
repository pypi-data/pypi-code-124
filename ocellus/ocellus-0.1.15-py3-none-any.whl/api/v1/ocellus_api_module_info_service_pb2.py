# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1/ocellus_api_module_info_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import ocellus_module_service_pb2 as ocellus__module__service__pb2
import ocellus_types_pb2 as ocellus__types__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,api/v1/ocellus_api_module_info_service.proto\x12\x1aocellus.api.v1.module.info\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cocellus_module_service.proto\x1a\x13ocellus_types.proto\x1a,protoc-gen-swagger/options/annotations.proto\"%\n\x11GetModulesRequest\x12\x10\n\x08moduleId\x18\x01 \x01(\t\"\xe4O\n\x12GetModulesResponse\x12(\n\x07modules\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct:\xa3O\x92\x41\x9fO2\x9cO\x12\x99O{\"modules\": [{\"inputParameters\": [],\"outputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"\" }],\"id\": \"rs1\",\"active\": true,\"render\": true,\"ordinal\": 0,\"pipeline\": 0,\"type\": \"RealSense\",\"moduleState\": 1,\"stateText\": \"\",\"rsCamera\": { \"processingBlocks\": {  \"alignEnabled\": true,  \"alignTo\": 2,  \"decimationFilterEnabled\": true,  \"streamFilter\": 1,  \"formatFilter\": 1,  \"filterMagnitude\": 8,  \"thresholdFilterEnabled\": false,  \"thresholdMaxDistance\": 1.5,  \"thresholdMinDistance\": 0,  \"disparityMode02\": 0,  \"spatialFilterEnabled\": false,  \"spatialMagnitude\": 1,  \"spatialSmoothAlpha\": 0.72000002861022949,  \"spatialSmoothDelta\": 9,  \"holeFillingMode\": 0,  \"temporalFilterEnabled\": false,  \"temporalSmoothAlpha\": 0.079999998211860657,  \"temporalSmoothDelta\": 100,  \"temporalPersistance\": 6,  \"holeFillingFilterEnabled\": false,  \"holesFill\": 2,  \"colorizerEnabled\": true,  \"visualPreset\": 0,  \"colorScheme\": 5,  \"histogramEqualization\": true,  \"colorizerMinDistance\": 0,  \"colorizerMaxDistance\": 6,  \"pointCloudEnabled\": true,  \"occlusionRemoval\": 2,  \"textureStream\": 1,  \"textureFormat\": 5 }, \"cameraInfo\": {  \"name\": \"\",  \"serialNumber\": \"\",  \"firmwareVersion\": \"\",  \"recommendedFirmwareVersion\": \"\",  \"physicalPort\": \"\",  \"debugOpCode\": \"\",  \"advancedMode\": \"\",  \"productId\": \"\",  \"cameraLocked\": \"\",  \"usbTypeDescriptor\": \"\" }, \"depthResolution\": {  \"width\": 0,  \"height\": 0 }, \"colorResolution\": {  \"width\": 0,  \"height\": 0 }, \"depthFps\": 2, \"colorFps\": 2, \"serialNumber\": \"\", \"mode\": 1, \"playbackFile\": \"/home/kcarlson/Documents/test/longredtape.bag\", \"availableFps\": [  6,  15,  30,  60 ], \"availableDepthResolutions\": [  {   \"devicePrefix\": \"D\",   \"resolutions\": [    {     \"width\": 424,     \"height\": 240    },    {     \"width\": 640,     \"height\": 360    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 848,     \"height\": 100    },    {     \"width\": 848,     \"height\": 480    },    {     \"width\": 1280,     \"height\": 720    }   ]  },  {   \"devicePrefix\": \"L\",   \"resolutions\": [    {     \"width\": 240,     \"height\": 640    },    {     \"width\": 384,     \"height\": 1024    },    {     \"width\": 480,     \"height\": 640    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 768,     \"height\": 1024    },    {     \"width\": 1024,     \"height\": 768    }   ]  } ], \"availableColorResolutions\": [  {   \"devicePrefix\": \"D\",   \"resolutions\": [    {     \"width\": 424,     \"height\": 240    },    {     \"width\": 640,     \"height\": 360    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 848,     \"height\": 480    },    {     \"width\": 960,     \"height\": 540    },    {     \"width\": 1280,     \"height\": 720    }   ]  },  {   \"devicePrefix\": \"L\",   \"resolutions\": [    {     \"width\": 1280,     \"height\": 720    },    {     \"width\": 1920,     \"height\": 1080    }   ]  } ]},\"position\": { \"x\": 0.0052760359831154346, \"y\": 0.058778461068868637, \"z\": -0.00064044661121442914},\"orientation\": { \"x\": 5.0150761604309082, \"y\": 82.971817016601562, \"z\": 358.756103515625},\"showPointcloud\": false,\"depthImage\": false,\"imu\": false,\"errors\": []},{\"inputParameters\": [],\"outputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"\" }, {  \"name\": \"ITEMS\",  \"dataType\": 3,  \"key\": \"\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"\" }],\"id\": \"img\",\"active\": true,\"render\": true,\"ordinal\": 1,\"pipeline\": 0,\"type\": \"ImageSource\",\"moduleState\": 0,\"stateText\": \"\",\"flipImage\": false,\"undistort\": false,\"contourThickness\": 1,\"path\": \"/home/kcarlson/Documents/test/slideshow\",\"displayTimeSeconds\": 5,\"intrinsicsConfigName\": \"\",\"position\": { \"x\": 0, \"y\": 0, \"z\": 0},\"orientation\": { \"x\": 0, \"y\": 0, \"z\": 0},\"itemProducerOptions\": { \"graphicType\": 0, \"showPointCloud\": false, \"surface2PolygonMeshOpts\": {  \"searchRadius\": 0.02500000037252903,  \"mu\": 2.5,  \"maximumNearestNeighbors\": 100,  \"maximumSurfaceAngle\": 45,  \"minimumAngle\": 10,  \"maximumAngle\": 120,  \"normalConsistency\": false,  \"consistentVertexOrdering\": true,  \"kSearch\": 20 }},\"errors\": []},{\"inputParameters\": [],\"outputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"\" }],\"id\": \"rs2\",\"active\": true,\"render\": true,\"ordinal\": 2,\"pipeline\": 1,\"type\": \"RealSense\",\"moduleState\": 1,\"stateText\": \"\",\"rsCamera\": { \"processingBlocks\": {  \"alignEnabled\": true,  \"alignTo\": 2,  \"decimationFilterEnabled\": true,  \"streamFilter\": 1,  \"formatFilter\": 1,  \"filterMagnitude\": 8,  \"thresholdFilterEnabled\": false,  \"thresholdMaxDistance\": 1.5,  \"thresholdMinDistance\": 0,  \"disparityMode02\": 0,  \"spatialFilterEnabled\": false,  \"spatialMagnitude\": 1,  \"spatialSmoothAlpha\": 0.72000002861022949,  \"spatialSmoothDelta\": 9,  \"holeFillingMode\": 0,  \"temporalFilterEnabled\": false,  \"temporalSmoothAlpha\": 0.079999998211860657,  \"temporalSmoothDelta\": 100,  \"temporalPersistance\": 6,  \"holeFillingFilterEnabled\": false,  \"holesFill\": 2,  \"colorizerEnabled\": true,  \"visualPreset\": 0,  \"colorScheme\": 5,  \"histogramEqualization\": true,  \"colorizerMinDistance\": 0,  \"colorizerMaxDistance\": 6,  \"pointCloudEnabled\": true,  \"occlusionRemoval\": 2,  \"textureStream\": 1,  \"textureFormat\": 5 }, \"cameraInfo\": {  \"name\": \"\",  \"serialNumber\": \"\",  \"firmwareVersion\": \"\",  \"recommendedFirmwareVersion\": \"\",  \"physicalPort\": \"\",  \"debugOpCode\": \"\",  \"advancedMode\": \"\",  \"productId\": \"\",  \"cameraLocked\": \"\",  \"usbTypeDescriptor\": \"\" }, \"depthResolution\": {  \"width\": 0,  \"height\": 0 }, \"colorResolution\": {  \"width\": 0,  \"height\": 0 }, \"depthFps\": 2, \"colorFps\": 2, \"serialNumber\": \"\", \"mode\": 1, \"playbackFile\": \"/home/kcarlson/Documents/test/longredtape.bag\", \"availableFps\": [  6,  15,  30,  60 ], \"availableDepthResolutions\": [  {   \"devicePrefix\": \"D\",   \"resolutions\": [    {     \"width\": 424,     \"height\": 240    },    {     \"width\": 640,     \"height\": 360    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 848,     \"height\": 100    },    {     \"width\": 848,     \"height\": 480    },    {     \"width\": 1280,     \"height\": 720    }   ]  },  {   \"devicePrefix\": \"L\",   \"resolutions\": [    {     \"width\": 240,     \"height\": 640    },    {     \"width\": 384,     \"height\": 1024    },    {     \"width\": 480,     \"height\": 640    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 768,     \"height\": 1024    },    {     \"width\": 1024,     \"height\": 768    }   ]  } ], \"availableColorResolutions\": [  {   \"devicePrefix\": \"D\",   \"resolutions\": [    {     \"width\": 424,     \"height\": 240    },    {     \"width\": 640,     \"height\": 360    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 848,     \"height\": 480    },    {     \"width\": 960,     \"height\": 540    },    {     \"width\": 1280,     \"height\": 720    }   ]  },  {   \"devicePrefix\": \"L\",   \"resolutions\": [    {     \"width\": 1280,     \"height\": 720    },    {     \"width\": 1920,     \"height\": 1080    }   ]  } ]},\"position\": { \"x\": 0.0052760359831154346, \"y\": 0.058778461068868637, \"z\": -0.00064044661121442914},\"orientation\": { \"x\": 5.0150761604309082, \"y\": 82.971817016601562, \"z\": 358.756103515625},\"showPointcloud\": false,\"depthImage\": false,\"imu\": false,\"errors\": []},{\"inputParameters\": [],\"outputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"\" }, {  \"name\": \"ITEMS\",  \"dataType\": 3,  \"key\": \"\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"\" }],\"id\": \"img2\",\"active\": true,\"render\": true,\"ordinal\": 3,\"pipeline\": 1,\"type\": \"ImageSource\",\"moduleState\": 0,\"stateText\": \"\",\"flipImage\": false,\"undistort\": false,\"contourThickness\": 1,\"path\": \"/home/kcarlson/Documents/test/slideshow\",\"displayTimeSeconds\": 5,\"intrinsicsConfigName\": \"\",\"position\": { \"x\": 0, \"y\": 0, \"z\": 0},\"orientation\": { \"x\": 0, \"y\": 0, \"z\": 0},\"itemProducerOptions\": { \"graphicType\": 0, \"showPointCloud\": false, \"surface2PolygonMeshOpts\": {  \"searchRadius\": 0.02500000037252903,  \"mu\": 2.5,  \"maximumNearestNeighbors\": 100,  \"maximumSurfaceAngle\": 45,  \"minimumAngle\": 10,  \"maximumAngle\": 120,  \"normalConsistency\": false,  \"consistentVertexOrdering\": true,  \"kSearch\": 20 }},\"errors\": []},{\"inputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"rs1/RGBA_IMAGE\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"rs1/POINTCLOUD\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"rs1/CAMERA\" }],\"outputParameters\": [ {  \"name\": \"CONTOURS\",  \"dataType\": 2,  \"key\": \"\" }, {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"ITEMS\",  \"dataType\": 3,  \"key\": \"\" }, {  \"name\": \"BLOB_COUNT\",  \"dataType\": 7,  \"key\": \"\" }],\"id\": \"blob1\",\"active\": true,\"render\": true,\"ordinal\": 4,\"pipeline\": 0,\"type\": \"Blob\",\"moduleState\": 0,\"stateText\": \"\",\"value0UpperBound\": 255,\"value0LowerBound\": 0,\"value1UpperBound\": 186,\"value1LowerBound\": 162,\"value2UpperBound\": 178,\"value2LowerBound\": 154,\"showRect\": false,\"rectColor\": { \"r\": 0, \"g\": 1, \"b\": 1, \"a\": 1},\"contourColor\": { \"r\": 0, \"g\": 0, \"b\": 1, \"a\": 1},\"contourThickness\": 1,\"trackerType\": 0,\"retrievalMode\": 0,\"colorPaletteType\": 0,\"invertMask\": false,\"dilateCount\": 0,\"blurAndReduceEnabled\": true,\"watershedEnabled\": false,\"erodeCount\": 0,\"erodeFirst\": false,\"minWidth\": 0,\"maxWidth\": 1,\"minHeight\": 0,\"maxHeight\": 1,\"kMeansCount\": 0,\"angleAnalysis\": 1,\"regionOfInterest\": { \"x\": 0, \"y\": 0, \"width\": 0, \"height\": 0},\"inferenceOnRoiImage\": false,\"extremePointsAnalysis\": 0,\"extremePointsDistanceFromCenterPoint\": 1,\"extremePointsFixedDistance\": 0,\"showRejected\": false,\"showRoi\": true,\"pointCloudFilters\": { \"holeFillingEnabled\": false, \"holeFillingResolution\": 1, \"holeFillingPasses\": 1},\"itemProducerOptions\": { \"graphicType\": 0, \"showPointCloud\": false, \"surface2PolygonMeshOpts\": {  \"searchRadius\": 0.02500000037252903,  \"mu\": 2.5,  \"maximumNearestNeighbors\": 100,  \"maximumSurfaceAngle\": 45,  \"minimumAngle\": 10,  \"maximumAngle\": 120,  \"normalConsistency\": false,  \"consistentVertexOrdering\": true,  \"kSearch\": 20 }},\"errors\": []}]}\"f\n\x13\x43reateModuleRequest\x12(\n\x07modules\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.ocellus.GlobalConfig\"\x9f\x02\n\x12PatchModuleRequest\x12\x10\n\x08moduleId\x18\x01 \x01(\t\x12L\n\noperations\x18\x02 \x03(\x0b\x32\x38.ocellus.api.v1.module.info.PatchModuleRequest.Operation\x1a\x34\n\tOperation\x12\n\n\x02op\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t:s\x92\x41p*#\n\nJSON Patch\x12\x15http://jsonpatch.com/2I\x12G{ \"operations\": [{ \"op\": \"replace\", \"path\": \"/baz\", \"value\": \"boo\" }] }\"M\n\x13\x44\x65leteModuleRequest\x12\x36\n\x08moduleId\x18\x01 \x01(\tB$\x92\x41!2\x14The module to delete\xd2\x01\x08moduleId\"\'\n\x18UpdateModuleOrderRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\"v\n\x17ModuleApiHandlerRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x10\n\x08moduleId\x18\x02 \x01(\t\x12\x11\n\tpathParam\x18\x03 \x01(\t\x12%\n\x04\x62ody\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xe7\x01\n\x18GetRemoteModulesResponse\x12V\n\x07modules\x18\x01 \x03(\x0b\x32\x45.ocellus.api.v1.module.info.GetRemoteModulesResponse.RemoteModuleInfo\x1as\n\x10RemoteModuleInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1f\n\x06inputs\x18\x02 \x03(\x0b\x32\x0f.ocellus.IOData\x12 \n\x07outputs\x18\x03 \x03(\x0b\x32\x0f.ocellus.IOData\x12\x0e\n\x06states\x18\x04 \x03(\t2\xfa\x12\n\x18OcellusModuleInfoService\x12\xb0\x01\n\rReloadModules\x12\x16.google.protobuf.Empty\x1a..ocellus.api.v1.module.info.GetModulesResponse\"W\x92\x41\x36\x1a\x34Will reload all modules from the configuration file.\x82\xd3\xe4\x93\x02\x18\x1a\x16/api/v1/modules/reload\x12\x9b\x01\n\x13UpdateModulesConfig\x12\x15.ocellus.GlobalConfig\x1a\x16.google.protobuf.Empty\"U\x92\x41\x34\x1a\x32Updates the global configuration, does not persist\x82\xd3\xe4\x93\x02\x18\x1a\x16/api/v1/modules/config\x12\x90\x01\n\x10GetModulesConfig\x12\x16.google.protobuf.Empty\x1a\x15.ocellus.GlobalConfig\"M\x92\x41,\x1a*Retreives the current global configuration\x82\xd3\xe4\x93\x02\x18\x12\x16/api/v1/modules/config\x12\xe4\x01\n\nGetModules\x12-.ocellus.api.v1.module.info.GetModulesRequest\x1a..ocellus.api.v1.module.info.GetModulesResponse\"w\x92\x41\x41\x1a?Returns all or the specified module\'s configuration information\x82\xd3\xe4\x93\x02-\x12\x19/api/v1/module/{moduleId}Z\x10\x12\x0e/api/v1/module\x12\xb2\x01\n\x0c\x43reateModule\x12/.ocellus.api.v1.module.info.CreateModuleRequest\x1a..ocellus.api.v1.module.info.GetModulesResponse\"A\x92\x41(\x1a&Creates a new module, does not persist\x82\xd3\xe4\x93\x02\x10\"\x0e/api/v1/module\x12\x89\x01\n\x0cUpdateModule\x12\x17.google.protobuf.Struct\x1a\x17.google.protobuf.Struct\"G\x92\x41.\x1a,Updates an existing module, does not persist\x82\xd3\xe4\x93\x02\x10\x1a\x0e/api/v1/module\x12\xaf\x02\n\x0bPatchModule\x12..ocellus.api.v1.module.info.PatchModuleRequest\x1a\x17.google.protobuf.Struct\"\xd6\x01\x92\x41\xae\x01\x1a\xab\x01Updates a specific field of an existing module, does not persist\nReplaces module fields with ops using jsonpatch. Only replace is supported\nReturns the updated module data\x82\xd3\xe4\x93\x02\x1e\x32\x19/api/v1/module/{moduleId}:\x01*\x12\xcb\x01\n\x0c\x44\x65leteModule\x12/.ocellus.api.v1.module.info.DeleteModuleRequest\x1a\x16.google.protobuf.Empty\"r\x92\x41<\x1a:Deletes a specific or all loaded modules, does not persist\x82\xd3\xe4\x93\x02-*\x19/api/v1/module/{moduleId}Z\x10*\x0e/api/v1/module\x12\xb8\x01\n\x11UpdateModuleOrder\x12\x34.ocellus.api.v1.module.info.UpdateModuleOrderRequest\x1a\x16.google.protobuf.Empty\"U\x92\x41\x36\x1a\x34\x43hanges the module execution order, does not persist\x82\xd3\xe4\x93\x02\x16\x1a\x14/api/v1/order/module\x12\xc2\x02\n\x10ModuleApiHandler\x12\x33.ocellus.api.v1.module.info.ModuleApiHandlerRequest\x1a\x17.google.protobuf.Struct\"\xdf\x01\x92\x41\x17\x1a\x15Module specific APIs.\x82\xd3\xe4\x93\x02\xbe\x01\x12,/api/{version}/module/{moduleId}/{pathParam}Z.*,/api/{version}/module/{moduleId}/{pathParam}Z.\",/api/{version}/module/{moduleId}/{pathParam}Z.\x1a,/api/{version}/module/{moduleId}/{pathParam}\x12\xed\x01\n\x10GetRemoteModules\x12\x16.google.protobuf.Empty\x1a\x34.ocellus.api.v1.module.info.GetRemoteModulesResponse\"\x8a\x01\x92\x41i\x1agReturns all the currently available remote modules connected using the ocellus.OcellusModuleService API\x82\xd3\xe4\x93\x02\x18\x12\x16/api/v1/modules/remote\x1a\x62\x92\x41_\x12]Service for interacting with the user configuration, module metadata, and module interactionsB\x81\x01\n\x1e\x63om.ocellus.api.v1.module.infoB\x18OcellusModuleInfoServiceP\x01Z\x1egithub.com/byte-motion/ocellus\xa2\x02\x05OAPMD\xaa\x02\x1aOcellus.Api.V1.Module.Infob\x06proto3')



_GETMODULESREQUEST = DESCRIPTOR.message_types_by_name['GetModulesRequest']
_GETMODULESRESPONSE = DESCRIPTOR.message_types_by_name['GetModulesResponse']
_CREATEMODULEREQUEST = DESCRIPTOR.message_types_by_name['CreateModuleRequest']
_PATCHMODULEREQUEST = DESCRIPTOR.message_types_by_name['PatchModuleRequest']
_PATCHMODULEREQUEST_OPERATION = _PATCHMODULEREQUEST.nested_types_by_name['Operation']
_DELETEMODULEREQUEST = DESCRIPTOR.message_types_by_name['DeleteModuleRequest']
_UPDATEMODULEORDERREQUEST = DESCRIPTOR.message_types_by_name['UpdateModuleOrderRequest']
_MODULEAPIHANDLERREQUEST = DESCRIPTOR.message_types_by_name['ModuleApiHandlerRequest']
_GETREMOTEMODULESRESPONSE = DESCRIPTOR.message_types_by_name['GetRemoteModulesResponse']
_GETREMOTEMODULESRESPONSE_REMOTEMODULEINFO = _GETREMOTEMODULESRESPONSE.nested_types_by_name['RemoteModuleInfo']
GetModulesRequest = _reflection.GeneratedProtocolMessageType('GetModulesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODULESREQUEST,
  '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.GetModulesRequest)
  })
_sym_db.RegisterMessage(GetModulesRequest)

GetModulesResponse = _reflection.GeneratedProtocolMessageType('GetModulesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODULESRESPONSE,
  '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.GetModulesResponse)
  })
_sym_db.RegisterMessage(GetModulesResponse)

CreateModuleRequest = _reflection.GeneratedProtocolMessageType('CreateModuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMODULEREQUEST,
  '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.CreateModuleRequest)
  })
_sym_db.RegisterMessage(CreateModuleRequest)

PatchModuleRequest = _reflection.GeneratedProtocolMessageType('PatchModuleRequest', (_message.Message,), {

  'Operation' : _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
    'DESCRIPTOR' : _PATCHMODULEREQUEST_OPERATION,
    '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
    # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.PatchModuleRequest.Operation)
    })
  ,
  'DESCRIPTOR' : _PATCHMODULEREQUEST,
  '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.PatchModuleRequest)
  })
_sym_db.RegisterMessage(PatchModuleRequest)
_sym_db.RegisterMessage(PatchModuleRequest.Operation)

DeleteModuleRequest = _reflection.GeneratedProtocolMessageType('DeleteModuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMODULEREQUEST,
  '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.DeleteModuleRequest)
  })
_sym_db.RegisterMessage(DeleteModuleRequest)

UpdateModuleOrderRequest = _reflection.GeneratedProtocolMessageType('UpdateModuleOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMODULEORDERREQUEST,
  '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.UpdateModuleOrderRequest)
  })
_sym_db.RegisterMessage(UpdateModuleOrderRequest)

ModuleApiHandlerRequest = _reflection.GeneratedProtocolMessageType('ModuleApiHandlerRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODULEAPIHANDLERREQUEST,
  '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.ModuleApiHandlerRequest)
  })
_sym_db.RegisterMessage(ModuleApiHandlerRequest)

GetRemoteModulesResponse = _reflection.GeneratedProtocolMessageType('GetRemoteModulesResponse', (_message.Message,), {

  'RemoteModuleInfo' : _reflection.GeneratedProtocolMessageType('RemoteModuleInfo', (_message.Message,), {
    'DESCRIPTOR' : _GETREMOTEMODULESRESPONSE_REMOTEMODULEINFO,
    '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
    # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.GetRemoteModulesResponse.RemoteModuleInfo)
    })
  ,
  'DESCRIPTOR' : _GETREMOTEMODULESRESPONSE,
  '__module__' : 'api.v1.ocellus_api_module_info_service_pb2'
  # @@protoc_insertion_point(class_scope:ocellus.api.v1.module.info.GetRemoteModulesResponse)
  })
_sym_db.RegisterMessage(GetRemoteModulesResponse)
_sym_db.RegisterMessage(GetRemoteModulesResponse.RemoteModuleInfo)

_OCELLUSMODULEINFOSERVICE = DESCRIPTOR.services_by_name['OcellusModuleInfoService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.ocellus.api.v1.module.infoB\030OcellusModuleInfoServiceP\001Z\036github.com/byte-motion/ocellus\242\002\005OAPMD\252\002\032Ocellus.Api.V1.Module.Info'
  _GETMODULESRESPONSE._options = None
  _GETMODULESRESPONSE._serialized_options = b'\222A\237O2\234O\022\231O{\"modules\": [{\"inputParameters\": [],\"outputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"\" }],\"id\": \"rs1\",\"active\": true,\"render\": true,\"ordinal\": 0,\"pipeline\": 0,\"type\": \"RealSense\",\"moduleState\": 1,\"stateText\": \"\",\"rsCamera\": { \"processingBlocks\": {  \"alignEnabled\": true,  \"alignTo\": 2,  \"decimationFilterEnabled\": true,  \"streamFilter\": 1,  \"formatFilter\": 1,  \"filterMagnitude\": 8,  \"thresholdFilterEnabled\": false,  \"thresholdMaxDistance\": 1.5,  \"thresholdMinDistance\": 0,  \"disparityMode02\": 0,  \"spatialFilterEnabled\": false,  \"spatialMagnitude\": 1,  \"spatialSmoothAlpha\": 0.72000002861022949,  \"spatialSmoothDelta\": 9,  \"holeFillingMode\": 0,  \"temporalFilterEnabled\": false,  \"temporalSmoothAlpha\": 0.079999998211860657,  \"temporalSmoothDelta\": 100,  \"temporalPersistance\": 6,  \"holeFillingFilterEnabled\": false,  \"holesFill\": 2,  \"colorizerEnabled\": true,  \"visualPreset\": 0,  \"colorScheme\": 5,  \"histogramEqualization\": true,  \"colorizerMinDistance\": 0,  \"colorizerMaxDistance\": 6,  \"pointCloudEnabled\": true,  \"occlusionRemoval\": 2,  \"textureStream\": 1,  \"textureFormat\": 5 }, \"cameraInfo\": {  \"name\": \"\",  \"serialNumber\": \"\",  \"firmwareVersion\": \"\",  \"recommendedFirmwareVersion\": \"\",  \"physicalPort\": \"\",  \"debugOpCode\": \"\",  \"advancedMode\": \"\",  \"productId\": \"\",  \"cameraLocked\": \"\",  \"usbTypeDescriptor\": \"\" }, \"depthResolution\": {  \"width\": 0,  \"height\": 0 }, \"colorResolution\": {  \"width\": 0,  \"height\": 0 }, \"depthFps\": 2, \"colorFps\": 2, \"serialNumber\": \"\", \"mode\": 1, \"playbackFile\": \"/home/kcarlson/Documents/test/longredtape.bag\", \"availableFps\": [  6,  15,  30,  60 ], \"availableDepthResolutions\": [  {   \"devicePrefix\": \"D\",   \"resolutions\": [    {     \"width\": 424,     \"height\": 240    },    {     \"width\": 640,     \"height\": 360    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 848,     \"height\": 100    },    {     \"width\": 848,     \"height\": 480    },    {     \"width\": 1280,     \"height\": 720    }   ]  },  {   \"devicePrefix\": \"L\",   \"resolutions\": [    {     \"width\": 240,     \"height\": 640    },    {     \"width\": 384,     \"height\": 1024    },    {     \"width\": 480,     \"height\": 640    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 768,     \"height\": 1024    },    {     \"width\": 1024,     \"height\": 768    }   ]  } ], \"availableColorResolutions\": [  {   \"devicePrefix\": \"D\",   \"resolutions\": [    {     \"width\": 424,     \"height\": 240    },    {     \"width\": 640,     \"height\": 360    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 848,     \"height\": 480    },    {     \"width\": 960,     \"height\": 540    },    {     \"width\": 1280,     \"height\": 720    }   ]  },  {   \"devicePrefix\": \"L\",   \"resolutions\": [    {     \"width\": 1280,     \"height\": 720    },    {     \"width\": 1920,     \"height\": 1080    }   ]  } ]},\"position\": { \"x\": 0.0052760359831154346, \"y\": 0.058778461068868637, \"z\": -0.00064044661121442914},\"orientation\": { \"x\": 5.0150761604309082, \"y\": 82.971817016601562, \"z\": 358.756103515625},\"showPointcloud\": false,\"depthImage\": false,\"imu\": false,\"errors\": []},{\"inputParameters\": [],\"outputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"\" }, {  \"name\": \"ITEMS\",  \"dataType\": 3,  \"key\": \"\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"\" }],\"id\": \"img\",\"active\": true,\"render\": true,\"ordinal\": 1,\"pipeline\": 0,\"type\": \"ImageSource\",\"moduleState\": 0,\"stateText\": \"\",\"flipImage\": false,\"undistort\": false,\"contourThickness\": 1,\"path\": \"/home/kcarlson/Documents/test/slideshow\",\"displayTimeSeconds\": 5,\"intrinsicsConfigName\": \"\",\"position\": { \"x\": 0, \"y\": 0, \"z\": 0},\"orientation\": { \"x\": 0, \"y\": 0, \"z\": 0},\"itemProducerOptions\": { \"graphicType\": 0, \"showPointCloud\": false, \"surface2PolygonMeshOpts\": {  \"searchRadius\": 0.02500000037252903,  \"mu\": 2.5,  \"maximumNearestNeighbors\": 100,  \"maximumSurfaceAngle\": 45,  \"minimumAngle\": 10,  \"maximumAngle\": 120,  \"normalConsistency\": false,  \"consistentVertexOrdering\": true,  \"kSearch\": 20 }},\"errors\": []},{\"inputParameters\": [],\"outputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"\" }],\"id\": \"rs2\",\"active\": true,\"render\": true,\"ordinal\": 2,\"pipeline\": 1,\"type\": \"RealSense\",\"moduleState\": 1,\"stateText\": \"\",\"rsCamera\": { \"processingBlocks\": {  \"alignEnabled\": true,  \"alignTo\": 2,  \"decimationFilterEnabled\": true,  \"streamFilter\": 1,  \"formatFilter\": 1,  \"filterMagnitude\": 8,  \"thresholdFilterEnabled\": false,  \"thresholdMaxDistance\": 1.5,  \"thresholdMinDistance\": 0,  \"disparityMode02\": 0,  \"spatialFilterEnabled\": false,  \"spatialMagnitude\": 1,  \"spatialSmoothAlpha\": 0.72000002861022949,  \"spatialSmoothDelta\": 9,  \"holeFillingMode\": 0,  \"temporalFilterEnabled\": false,  \"temporalSmoothAlpha\": 0.079999998211860657,  \"temporalSmoothDelta\": 100,  \"temporalPersistance\": 6,  \"holeFillingFilterEnabled\": false,  \"holesFill\": 2,  \"colorizerEnabled\": true,  \"visualPreset\": 0,  \"colorScheme\": 5,  \"histogramEqualization\": true,  \"colorizerMinDistance\": 0,  \"colorizerMaxDistance\": 6,  \"pointCloudEnabled\": true,  \"occlusionRemoval\": 2,  \"textureStream\": 1,  \"textureFormat\": 5 }, \"cameraInfo\": {  \"name\": \"\",  \"serialNumber\": \"\",  \"firmwareVersion\": \"\",  \"recommendedFirmwareVersion\": \"\",  \"physicalPort\": \"\",  \"debugOpCode\": \"\",  \"advancedMode\": \"\",  \"productId\": \"\",  \"cameraLocked\": \"\",  \"usbTypeDescriptor\": \"\" }, \"depthResolution\": {  \"width\": 0,  \"height\": 0 }, \"colorResolution\": {  \"width\": 0,  \"height\": 0 }, \"depthFps\": 2, \"colorFps\": 2, \"serialNumber\": \"\", \"mode\": 1, \"playbackFile\": \"/home/kcarlson/Documents/test/longredtape.bag\", \"availableFps\": [  6,  15,  30,  60 ], \"availableDepthResolutions\": [  {   \"devicePrefix\": \"D\",   \"resolutions\": [    {     \"width\": 424,     \"height\": 240    },    {     \"width\": 640,     \"height\": 360    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 848,     \"height\": 100    },    {     \"width\": 848,     \"height\": 480    },    {     \"width\": 1280,     \"height\": 720    }   ]  },  {   \"devicePrefix\": \"L\",   \"resolutions\": [    {     \"width\": 240,     \"height\": 640    },    {     \"width\": 384,     \"height\": 1024    },    {     \"width\": 480,     \"height\": 640    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 768,     \"height\": 1024    },    {     \"width\": 1024,     \"height\": 768    }   ]  } ], \"availableColorResolutions\": [  {   \"devicePrefix\": \"D\",   \"resolutions\": [    {     \"width\": 424,     \"height\": 240    },    {     \"width\": 640,     \"height\": 360    },    {     \"width\": 640,     \"height\": 480    },    {     \"width\": 848,     \"height\": 480    },    {     \"width\": 960,     \"height\": 540    },    {     \"width\": 1280,     \"height\": 720    }   ]  },  {   \"devicePrefix\": \"L\",   \"resolutions\": [    {     \"width\": 1280,     \"height\": 720    },    {     \"width\": 1920,     \"height\": 1080    }   ]  } ]},\"position\": { \"x\": 0.0052760359831154346, \"y\": 0.058778461068868637, \"z\": -0.00064044661121442914},\"orientation\": { \"x\": 5.0150761604309082, \"y\": 82.971817016601562, \"z\": 358.756103515625},\"showPointcloud\": false,\"depthImage\": false,\"imu\": false,\"errors\": []},{\"inputParameters\": [],\"outputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"\" }, {  \"name\": \"ITEMS\",  \"dataType\": 3,  \"key\": \"\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"\" }],\"id\": \"img2\",\"active\": true,\"render\": true,\"ordinal\": 3,\"pipeline\": 1,\"type\": \"ImageSource\",\"moduleState\": 0,\"stateText\": \"\",\"flipImage\": false,\"undistort\": false,\"contourThickness\": 1,\"path\": \"/home/kcarlson/Documents/test/slideshow\",\"displayTimeSeconds\": 5,\"intrinsicsConfigName\": \"\",\"position\": { \"x\": 0, \"y\": 0, \"z\": 0},\"orientation\": { \"x\": 0, \"y\": 0, \"z\": 0},\"itemProducerOptions\": { \"graphicType\": 0, \"showPointCloud\": false, \"surface2PolygonMeshOpts\": {  \"searchRadius\": 0.02500000037252903,  \"mu\": 2.5,  \"maximumNearestNeighbors\": 100,  \"maximumSurfaceAngle\": 45,  \"minimumAngle\": 10,  \"maximumAngle\": 120,  \"normalConsistency\": false,  \"consistentVertexOrdering\": true,  \"kSearch\": 20 }},\"errors\": []},{\"inputParameters\": [ {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"rs1/RGBA_IMAGE\" }, {  \"name\": \"POINTCLOUD\",  \"dataType\": 5,  \"key\": \"rs1/POINTCLOUD\" }, {  \"name\": \"CAMERA\",  \"dataType\": 1,  \"key\": \"rs1/CAMERA\" }],\"outputParameters\": [ {  \"name\": \"CONTOURS\",  \"dataType\": 2,  \"key\": \"\" }, {  \"name\": \"RGBA_IMAGE\",  \"dataType\": 4,  \"key\": \"\" }, {  \"name\": \"ITEMS\",  \"dataType\": 3,  \"key\": \"\" }, {  \"name\": \"BLOB_COUNT\",  \"dataType\": 7,  \"key\": \"\" }],\"id\": \"blob1\",\"active\": true,\"render\": true,\"ordinal\": 4,\"pipeline\": 0,\"type\": \"Blob\",\"moduleState\": 0,\"stateText\": \"\",\"value0UpperBound\": 255,\"value0LowerBound\": 0,\"value1UpperBound\": 186,\"value1LowerBound\": 162,\"value2UpperBound\": 178,\"value2LowerBound\": 154,\"showRect\": false,\"rectColor\": { \"r\": 0, \"g\": 1, \"b\": 1, \"a\": 1},\"contourColor\": { \"r\": 0, \"g\": 0, \"b\": 1, \"a\": 1},\"contourThickness\": 1,\"trackerType\": 0,\"retrievalMode\": 0,\"colorPaletteType\": 0,\"invertMask\": false,\"dilateCount\": 0,\"blurAndReduceEnabled\": true,\"watershedEnabled\": false,\"erodeCount\": 0,\"erodeFirst\": false,\"minWidth\": 0,\"maxWidth\": 1,\"minHeight\": 0,\"maxHeight\": 1,\"kMeansCount\": 0,\"angleAnalysis\": 1,\"regionOfInterest\": { \"x\": 0, \"y\": 0, \"width\": 0, \"height\": 0},\"inferenceOnRoiImage\": false,\"extremePointsAnalysis\": 0,\"extremePointsDistanceFromCenterPoint\": 1,\"extremePointsFixedDistance\": 0,\"showRejected\": false,\"showRoi\": true,\"pointCloudFilters\": { \"holeFillingEnabled\": false, \"holeFillingResolution\": 1, \"holeFillingPasses\": 1},\"itemProducerOptions\": { \"graphicType\": 0, \"showPointCloud\": false, \"surface2PolygonMeshOpts\": {  \"searchRadius\": 0.02500000037252903,  \"mu\": 2.5,  \"maximumNearestNeighbors\": 100,  \"maximumSurfaceAngle\": 45,  \"minimumAngle\": 10,  \"maximumAngle\": 120,  \"normalConsistency\": false,  \"consistentVertexOrdering\": true,  \"kSearch\": 20 }},\"errors\": []}]}'
  _PATCHMODULEREQUEST._options = None
  _PATCHMODULEREQUEST._serialized_options = b'\222Ap*#\n\nJSON Patch\022\025http://jsonpatch.com/2I\022G{ \"operations\": [{ \"op\": \"replace\", \"path\": \"/baz\", \"value\": \"boo\" }] }'
  _DELETEMODULEREQUEST.fields_by_name['moduleId']._options = None
  _DELETEMODULEREQUEST.fields_by_name['moduleId']._serialized_options = b'\222A!2\024The module to delete\322\001\010moduleId'
  _OCELLUSMODULEINFOSERVICE._options = None
  _OCELLUSMODULEINFOSERVICE._serialized_options = b'\222A_\022]Service for interacting with the user configuration, module metadata, and module interactions'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['ReloadModules']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['ReloadModules']._serialized_options = b'\222A6\0324Will reload all modules from the configuration file.\202\323\344\223\002\030\032\026/api/v1/modules/reload'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['UpdateModulesConfig']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['UpdateModulesConfig']._serialized_options = b'\222A4\0322Updates the global configuration, does not persist\202\323\344\223\002\030\032\026/api/v1/modules/config'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['GetModulesConfig']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['GetModulesConfig']._serialized_options = b'\222A,\032*Retreives the current global configuration\202\323\344\223\002\030\022\026/api/v1/modules/config'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['GetModules']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['GetModules']._serialized_options = b'\222AA\032?Returns all or the specified module\'s configuration information\202\323\344\223\002-\022\031/api/v1/module/{moduleId}Z\020\022\016/api/v1/module'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['CreateModule']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['CreateModule']._serialized_options = b'\222A(\032&Creates a new module, does not persist\202\323\344\223\002\020\"\016/api/v1/module'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['UpdateModule']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['UpdateModule']._serialized_options = b'\222A.\032,Updates an existing module, does not persist\202\323\344\223\002\020\032\016/api/v1/module'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['PatchModule']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['PatchModule']._serialized_options = b'\222A\256\001\032\253\001Updates a specific field of an existing module, does not persist\nReplaces module fields with ops using jsonpatch. Only replace is supported\nReturns the updated module data\202\323\344\223\002\0362\031/api/v1/module/{moduleId}:\001*'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['DeleteModule']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['DeleteModule']._serialized_options = b'\222A<\032:Deletes a specific or all loaded modules, does not persist\202\323\344\223\002-*\031/api/v1/module/{moduleId}Z\020*\016/api/v1/module'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['UpdateModuleOrder']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['UpdateModuleOrder']._serialized_options = b'\222A6\0324Changes the module execution order, does not persist\202\323\344\223\002\026\032\024/api/v1/order/module'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['ModuleApiHandler']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['ModuleApiHandler']._serialized_options = b'\222A\027\032\025Module specific APIs.\202\323\344\223\002\276\001\022,/api/{version}/module/{moduleId}/{pathParam}Z.*,/api/{version}/module/{moduleId}/{pathParam}Z.\",/api/{version}/module/{moduleId}/{pathParam}Z.\032,/api/{version}/module/{moduleId}/{pathParam}'
  _OCELLUSMODULEINFOSERVICE.methods_by_name['GetRemoteModules']._options = None
  _OCELLUSMODULEINFOSERVICE.methods_by_name['GetRemoteModules']._serialized_options = b'\222Ai\032gReturns all the currently available remote modules connected using the ocellus.OcellusModuleService API\202\323\344\223\002\030\022\026/api/v1/modules/remote'
  _GETMODULESREQUEST._serialized_start=262
  _GETMODULESREQUEST._serialized_end=299
  _GETMODULESRESPONSE._serialized_start=302
  _GETMODULESRESPONSE._serialized_end=10514
  _CREATEMODULEREQUEST._serialized_start=10516
  _CREATEMODULEREQUEST._serialized_end=10618
  _PATCHMODULEREQUEST._serialized_start=10621
  _PATCHMODULEREQUEST._serialized_end=10908
  _PATCHMODULEREQUEST_OPERATION._serialized_start=10739
  _PATCHMODULEREQUEST_OPERATION._serialized_end=10791
  _DELETEMODULEREQUEST._serialized_start=10910
  _DELETEMODULEREQUEST._serialized_end=10987
  _UPDATEMODULEORDERREQUEST._serialized_start=10989
  _UPDATEMODULEORDERREQUEST._serialized_end=11028
  _MODULEAPIHANDLERREQUEST._serialized_start=11030
  _MODULEAPIHANDLERREQUEST._serialized_end=11148
  _GETREMOTEMODULESRESPONSE._serialized_start=11151
  _GETREMOTEMODULESRESPONSE._serialized_end=11382
  _GETREMOTEMODULESRESPONSE_REMOTEMODULEINFO._serialized_start=11267
  _GETREMOTEMODULESRESPONSE_REMOTEMODULEINFO._serialized_end=11382
  _OCELLUSMODULEINFOSERVICE._serialized_start=11385
  _OCELLUSMODULEINFOSERVICE._serialized_end=13811
# @@protoc_insertion_point(module_scope)
