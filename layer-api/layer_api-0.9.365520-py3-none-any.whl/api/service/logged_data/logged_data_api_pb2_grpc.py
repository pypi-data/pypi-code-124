# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from layerapi.api.service.logged_data import logged_data_api_pb2 as api_dot_service_dot_logged__data_dot_logged__data__api__pb2


class LoggedDataAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LogModelMetric = channel.unary_unary(
                '/api.LoggedDataAPI/LogModelMetric',
                request_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogModelMetricRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogModelMetricResponse.FromString,
                )
        self.LogData = channel.unary_unary(
                '/api.LoggedDataAPI/LogData',
                request_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogDataRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogDataResponse.FromString,
                )
        self.GetAllModelTrainMetrics = channel.unary_unary(
                '/api.LoggedDataAPI/GetAllModelTrainMetrics',
                request_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllModelTrainMetricsRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllModelTrainMetricsResponse.FromString,
                )
        self.GetModelTrainMetric = channel.unary_unary(
                '/api.LoggedDataAPI/GetModelTrainMetric',
                request_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetModelTrainMetricRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetModelTrainMetricResponse.FromString,
                )
        self.GetAllLoggedData = channel.unary_unary(
                '/api.LoggedDataAPI/GetAllLoggedData',
                request_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllLoggedDataRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllLoggedDataResponse.FromString,
                )
        self.GetLoggedData = channel.unary_unary(
                '/api.LoggedDataAPI/GetLoggedData',
                request_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetLoggedDataRequest.SerializeToString,
                response_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetLoggedDataResponse.FromString,
                )


class LoggedDataAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LogModelMetric(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LogData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllModelTrainMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetModelTrainMetric(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllLoggedData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoggedData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LoggedDataAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LogModelMetric': grpc.unary_unary_rpc_method_handler(
                    servicer.LogModelMetric,
                    request_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogModelMetricRequest.FromString,
                    response_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogModelMetricResponse.SerializeToString,
            ),
            'LogData': grpc.unary_unary_rpc_method_handler(
                    servicer.LogData,
                    request_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogDataRequest.FromString,
                    response_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogDataResponse.SerializeToString,
            ),
            'GetAllModelTrainMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllModelTrainMetrics,
                    request_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllModelTrainMetricsRequest.FromString,
                    response_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllModelTrainMetricsResponse.SerializeToString,
            ),
            'GetModelTrainMetric': grpc.unary_unary_rpc_method_handler(
                    servicer.GetModelTrainMetric,
                    request_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetModelTrainMetricRequest.FromString,
                    response_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetModelTrainMetricResponse.SerializeToString,
            ),
            'GetAllLoggedData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllLoggedData,
                    request_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllLoggedDataRequest.FromString,
                    response_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllLoggedDataResponse.SerializeToString,
            ),
            'GetLoggedData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoggedData,
                    request_deserializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetLoggedDataRequest.FromString,
                    response_serializer=api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetLoggedDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.LoggedDataAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LoggedDataAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LogModelMetric(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.LoggedDataAPI/LogModelMetric',
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogModelMetricRequest.SerializeToString,
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogModelMetricResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LogData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.LoggedDataAPI/LogData',
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogDataRequest.SerializeToString,
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.LogDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllModelTrainMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.LoggedDataAPI/GetAllModelTrainMetrics',
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllModelTrainMetricsRequest.SerializeToString,
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllModelTrainMetricsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetModelTrainMetric(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.LoggedDataAPI/GetModelTrainMetric',
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetModelTrainMetricRequest.SerializeToString,
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetModelTrainMetricResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllLoggedData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.LoggedDataAPI/GetAllLoggedData',
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllLoggedDataRequest.SerializeToString,
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetAllLoggedDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLoggedData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.LoggedDataAPI/GetLoggedData',
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetLoggedDataRequest.SerializeToString,
            api_dot_service_dot_logged__data_dot_logged__data__api__pb2.GetLoggedDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
