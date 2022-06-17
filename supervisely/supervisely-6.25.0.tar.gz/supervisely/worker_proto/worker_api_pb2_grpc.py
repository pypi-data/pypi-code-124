# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import worker_api_pb2 as worker__api__pb2


class GeneralAPIStub(object):
  """package supervisely;

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateProject = channel.unary_unary(
        '/GeneralAPI/CreateProject',
        request_serializer=worker__api__pb2.Project.SerializeToString,
        response_deserializer=worker__api__pb2.Id.FromString,
        )
    self.CreateDataset = channel.unary_unary(
        '/GeneralAPI/CreateDataset',
        request_serializer=worker__api__pb2.ProjectDataset.SerializeToString,
        response_deserializer=worker__api__pb2.Id.FromString,
        )
    self.GetProjectByName = channel.unary_unary(
        '/GeneralAPI/GetProjectByName',
        request_serializer=worker__api__pb2.Project.SerializeToString,
        response_deserializer=worker__api__pb2.Project.FromString,
        )
    self.GetDatasetByName = channel.unary_unary(
        '/GeneralAPI/GetDatasetByName',
        request_serializer=worker__api__pb2.ProjectDataset.SerializeToString,
        response_deserializer=worker__api__pb2.Dataset.FromString,
        )
    self.GetModelByName = channel.unary_unary(
        '/GeneralAPI/GetModelByName',
        request_serializer=worker__api__pb2.ModelName.SerializeToString,
        response_deserializer=worker__api__pb2.ModelInfo.FromString,
        )
    self.GetProjectMeta = channel.unary_unary(
        '/GeneralAPI/GetProjectMeta',
        request_serializer=worker__api__pb2.Id.SerializeToString,
        response_deserializer=worker__api__pb2.Project.FromString,
        )
    self.GetProjectDatasets = channel.unary_unary(
        '/GeneralAPI/GetProjectDatasets',
        request_serializer=worker__api__pb2.Id.SerializeToString,
        response_deserializer=worker__api__pb2.DatasetArray.FromString,
        )
    self.GetDatasetImages = channel.unary_unary(
        '/GeneralAPI/GetDatasetImages',
        request_serializer=worker__api__pb2.Id.SerializeToString,
        response_deserializer=worker__api__pb2.ImageArray.FromString,
        )
    self.GetImagesInfo = channel.unary_unary(
        '/GeneralAPI/GetImagesInfo',
        request_serializer=worker__api__pb2.ImageArray.SerializeToString,
        response_deserializer=worker__api__pb2.ImagesInfo.FromString,
        )
    self.DownloadImages = channel.unary_stream(
        '/GeneralAPI/DownloadImages',
        request_serializer=worker__api__pb2.ImagesHashes.SerializeToString,
        response_deserializer=worker__api__pb2.ChunkImage.FromString,
        )
    self.DownloadAnnotations = channel.unary_stream(
        '/GeneralAPI/DownloadAnnotations',
        request_serializer=worker__api__pb2.ImageArray.SerializeToString,
        response_deserializer=worker__api__pb2.ChunkImage.FromString,
        )
    self.FindImagesExist = channel.unary_unary(
        '/GeneralAPI/FindImagesExist',
        request_serializer=worker__api__pb2.ImagesHashes.SerializeToString,
        response_deserializer=worker__api__pb2.ImagesHashes.FromString,
        )
    self.AddExistingImagesToDataset = channel.unary_unary(
        '/GeneralAPI/AddExistingImagesToDataset',
        request_serializer=worker__api__pb2.ImagesToAdd.SerializeToString,
        response_deserializer=worker__api__pb2.ImageArray.FromString,
        )
    self.UploadAnnotations = channel.stream_unary(
        '/GeneralAPI/UploadAnnotations',
        request_serializer=worker__api__pb2.ChunkImage.SerializeToString,
        response_deserializer=worker__api__pb2.ImageArray.FromString,
        )
    self.UploadArchive = channel.stream_unary(
        '/GeneralAPI/UploadArchive',
        request_serializer=worker__api__pb2.Chunk.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )
    self.GetProjectStats = channel.unary_unary(
        '/GeneralAPI/GetProjectStats',
        request_serializer=worker__api__pb2.Id.SerializeToString,
        response_deserializer=worker__api__pb2.ProjectStats.FromString,
        )
    self.SetProjectFinished = channel.unary_unary(
        '/GeneralAPI/SetProjectFinished',
        request_serializer=worker__api__pb2.Id.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )
    self.Log = channel.unary_unary(
        '/GeneralAPI/Log',
        request_serializer=worker__api__pb2.LogLines.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )
    self.GetImportStructure = channel.unary_unary(
        '/GeneralAPI/GetImportStructure',
        request_serializer=worker__api__pb2.Id.SerializeToString,
        response_deserializer=worker__api__pb2.ListFiles.FromString,
        )
    self.GetImportFiles = channel.unary_stream(
        '/GeneralAPI/GetImportFiles',
        request_serializer=worker__api__pb2.ImportRequest.SerializeToString,
        response_deserializer=worker__api__pb2.ChunkFile.FromString,
        )
    self.GetNewTask = channel.unary_stream(
        '/GeneralAPI/GetNewTask',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.Task.FromString,
        )
    self.GetStopTask = channel.unary_stream(
        '/GeneralAPI/GetStopTask',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.Id.FromString,
        )
    self.AgentConnected = channel.unary_unary(
        '/GeneralAPI/AgentConnected',
        request_serializer=worker__api__pb2.AgentInfo.SerializeToString,
        response_deserializer=worker__api__pb2.ServerInfo.FromString,
        )
    self.AgentPing = channel.unary_unary(
        '/GeneralAPI/AgentPing',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )
    self.UploadModel = channel.stream_unary(
        '/GeneralAPI/UploadModel',
        request_serializer=worker__api__pb2.ChunkModel.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )
    self.DownloadModel = channel.unary_stream(
        '/GeneralAPI/DownloadModel',
        request_serializer=worker__api__pb2.ModelDescription.SerializeToString,
        response_deserializer=worker__api__pb2.Chunk.FromString,
        )
    self.GenerateNewModelId = channel.unary_unary(
        '/GeneralAPI/GenerateNewModelId',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.ModelDescription.FromString,
        )
    self.GetTelemetryTask = channel.unary_stream(
        '/GeneralAPI/GetTelemetryTask',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.Task.FromString,
        )
    self.UpdateTelemetry = channel.unary_unary(
        '/GeneralAPI/UpdateTelemetry',
        request_serializer=worker__api__pb2.AgentInfo.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )
    self.AddImages = channel.unary_unary(
        '/GeneralAPI/AddImages',
        request_serializer=worker__api__pb2.ImagesInfo.SerializeToString,
        response_deserializer=worker__api__pb2.ImageArray.FromString,
        )
    self.UploadImages = channel.stream_unary(
        '/GeneralAPI/UploadImages',
        request_serializer=worker__api__pb2.ChunkImage.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )
    self.GetUsedImageList = channel.unary_stream(
        '/GeneralAPI/GetUsedImageList',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.NodeObjectHash.FromString,
        )
    self.GetUsedModelList = channel.unary_stream(
        '/GeneralAPI/GetUsedModelList',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.NodeObjectHash.FromString,
        )
    self.GetGeneralEventsStream = channel.unary_stream(
        '/GeneralAPI/GetGeneralEventsStream',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.GeneralEvent.FromString,
        )
    self.GetGeneralEventData = channel.unary_stream(
        '/GeneralAPI/GetGeneralEventData',
        request_serializer=worker__api__pb2.Empty.SerializeToString,
        response_deserializer=worker__api__pb2.Chunk.FromString,
        )
    self.SendGeneralEventData = channel.stream_unary(
        '/GeneralAPI/SendGeneralEventData',
        request_serializer=worker__api__pb2.Chunk.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )
    self.AddMetaToProject = channel.unary_unary(
        '/GeneralAPI/AddMetaToProject',
        request_serializer=worker__api__pb2.Project.SerializeToString,
        response_deserializer=worker__api__pb2.Empty.FromString,
        )


class GeneralAPIServicer(object):
  """package supervisely;

  """

  def CreateProject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateDataset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProjectByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDatasetByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModelByName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProjectMeta(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProjectDatasets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDatasetImages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetImagesInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadImages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadAnnotations(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindImagesExist(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddExistingImagesToDataset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadAnnotations(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadArchive(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProjectStats(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetProjectFinished(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Log(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetImportStructure(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetImportFiles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNewTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStopTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AgentConnected(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AgentPing(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadModel(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateNewModelId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTelemetryTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTelemetry(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddImages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadImages(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUsedImageList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUsedModelList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGeneralEventsStream(self, request, context):
    """AgentRPC
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGeneralEventData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendGeneralEventData(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddMetaToProject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GeneralAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateProject': grpc.unary_unary_rpc_method_handler(
          servicer.CreateProject,
          request_deserializer=worker__api__pb2.Project.FromString,
          response_serializer=worker__api__pb2.Id.SerializeToString,
      ),
      'CreateDataset': grpc.unary_unary_rpc_method_handler(
          servicer.CreateDataset,
          request_deserializer=worker__api__pb2.ProjectDataset.FromString,
          response_serializer=worker__api__pb2.Id.SerializeToString,
      ),
      'GetProjectByName': grpc.unary_unary_rpc_method_handler(
          servicer.GetProjectByName,
          request_deserializer=worker__api__pb2.Project.FromString,
          response_serializer=worker__api__pb2.Project.SerializeToString,
      ),
      'GetDatasetByName': grpc.unary_unary_rpc_method_handler(
          servicer.GetDatasetByName,
          request_deserializer=worker__api__pb2.ProjectDataset.FromString,
          response_serializer=worker__api__pb2.Dataset.SerializeToString,
      ),
      'GetModelByName': grpc.unary_unary_rpc_method_handler(
          servicer.GetModelByName,
          request_deserializer=worker__api__pb2.ModelName.FromString,
          response_serializer=worker__api__pb2.ModelInfo.SerializeToString,
      ),
      'GetProjectMeta': grpc.unary_unary_rpc_method_handler(
          servicer.GetProjectMeta,
          request_deserializer=worker__api__pb2.Id.FromString,
          response_serializer=worker__api__pb2.Project.SerializeToString,
      ),
      'GetProjectDatasets': grpc.unary_unary_rpc_method_handler(
          servicer.GetProjectDatasets,
          request_deserializer=worker__api__pb2.Id.FromString,
          response_serializer=worker__api__pb2.DatasetArray.SerializeToString,
      ),
      'GetDatasetImages': grpc.unary_unary_rpc_method_handler(
          servicer.GetDatasetImages,
          request_deserializer=worker__api__pb2.Id.FromString,
          response_serializer=worker__api__pb2.ImageArray.SerializeToString,
      ),
      'GetImagesInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetImagesInfo,
          request_deserializer=worker__api__pb2.ImageArray.FromString,
          response_serializer=worker__api__pb2.ImagesInfo.SerializeToString,
      ),
      'DownloadImages': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadImages,
          request_deserializer=worker__api__pb2.ImagesHashes.FromString,
          response_serializer=worker__api__pb2.ChunkImage.SerializeToString,
      ),
      'DownloadAnnotations': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadAnnotations,
          request_deserializer=worker__api__pb2.ImageArray.FromString,
          response_serializer=worker__api__pb2.ChunkImage.SerializeToString,
      ),
      'FindImagesExist': grpc.unary_unary_rpc_method_handler(
          servicer.FindImagesExist,
          request_deserializer=worker__api__pb2.ImagesHashes.FromString,
          response_serializer=worker__api__pb2.ImagesHashes.SerializeToString,
      ),
      'AddExistingImagesToDataset': grpc.unary_unary_rpc_method_handler(
          servicer.AddExistingImagesToDataset,
          request_deserializer=worker__api__pb2.ImagesToAdd.FromString,
          response_serializer=worker__api__pb2.ImageArray.SerializeToString,
      ),
      'UploadAnnotations': grpc.stream_unary_rpc_method_handler(
          servicer.UploadAnnotations,
          request_deserializer=worker__api__pb2.ChunkImage.FromString,
          response_serializer=worker__api__pb2.ImageArray.SerializeToString,
      ),
      'UploadArchive': grpc.stream_unary_rpc_method_handler(
          servicer.UploadArchive,
          request_deserializer=worker__api__pb2.Chunk.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
      'GetProjectStats': grpc.unary_unary_rpc_method_handler(
          servicer.GetProjectStats,
          request_deserializer=worker__api__pb2.Id.FromString,
          response_serializer=worker__api__pb2.ProjectStats.SerializeToString,
      ),
      'SetProjectFinished': grpc.unary_unary_rpc_method_handler(
          servicer.SetProjectFinished,
          request_deserializer=worker__api__pb2.Id.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
      'Log': grpc.unary_unary_rpc_method_handler(
          servicer.Log,
          request_deserializer=worker__api__pb2.LogLines.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
      'GetImportStructure': grpc.unary_unary_rpc_method_handler(
          servicer.GetImportStructure,
          request_deserializer=worker__api__pb2.Id.FromString,
          response_serializer=worker__api__pb2.ListFiles.SerializeToString,
      ),
      'GetImportFiles': grpc.unary_stream_rpc_method_handler(
          servicer.GetImportFiles,
          request_deserializer=worker__api__pb2.ImportRequest.FromString,
          response_serializer=worker__api__pb2.ChunkFile.SerializeToString,
      ),
      'GetNewTask': grpc.unary_stream_rpc_method_handler(
          servicer.GetNewTask,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.Task.SerializeToString,
      ),
      'GetStopTask': grpc.unary_stream_rpc_method_handler(
          servicer.GetStopTask,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.Id.SerializeToString,
      ),
      'AgentConnected': grpc.unary_unary_rpc_method_handler(
          servicer.AgentConnected,
          request_deserializer=worker__api__pb2.AgentInfo.FromString,
          response_serializer=worker__api__pb2.ServerInfo.SerializeToString,
      ),
      'AgentPing': grpc.unary_unary_rpc_method_handler(
          servicer.AgentPing,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
      'UploadModel': grpc.stream_unary_rpc_method_handler(
          servicer.UploadModel,
          request_deserializer=worker__api__pb2.ChunkModel.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
      'DownloadModel': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadModel,
          request_deserializer=worker__api__pb2.ModelDescription.FromString,
          response_serializer=worker__api__pb2.Chunk.SerializeToString,
      ),
      'GenerateNewModelId': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateNewModelId,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.ModelDescription.SerializeToString,
      ),
      'GetTelemetryTask': grpc.unary_stream_rpc_method_handler(
          servicer.GetTelemetryTask,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.Task.SerializeToString,
      ),
      'UpdateTelemetry': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTelemetry,
          request_deserializer=worker__api__pb2.AgentInfo.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
      'AddImages': grpc.unary_unary_rpc_method_handler(
          servicer.AddImages,
          request_deserializer=worker__api__pb2.ImagesInfo.FromString,
          response_serializer=worker__api__pb2.ImageArray.SerializeToString,
      ),
      'UploadImages': grpc.stream_unary_rpc_method_handler(
          servicer.UploadImages,
          request_deserializer=worker__api__pb2.ChunkImage.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
      'GetUsedImageList': grpc.unary_stream_rpc_method_handler(
          servicer.GetUsedImageList,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.NodeObjectHash.SerializeToString,
      ),
      'GetUsedModelList': grpc.unary_stream_rpc_method_handler(
          servicer.GetUsedModelList,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.NodeObjectHash.SerializeToString,
      ),
      'GetGeneralEventsStream': grpc.unary_stream_rpc_method_handler(
          servicer.GetGeneralEventsStream,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.GeneralEvent.SerializeToString,
      ),
      'GetGeneralEventData': grpc.unary_stream_rpc_method_handler(
          servicer.GetGeneralEventData,
          request_deserializer=worker__api__pb2.Empty.FromString,
          response_serializer=worker__api__pb2.Chunk.SerializeToString,
      ),
      'SendGeneralEventData': grpc.stream_unary_rpc_method_handler(
          servicer.SendGeneralEventData,
          request_deserializer=worker__api__pb2.Chunk.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
      'AddMetaToProject': grpc.unary_unary_rpc_method_handler(
          servicer.AddMetaToProject,
          request_deserializer=worker__api__pb2.Project.FromString,
          response_serializer=worker__api__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'GeneralAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
