"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import flwr.proto.driver_pb2
import grpc

class DriverStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    GetNodes: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.GetNodesRequest,
        flwr.proto.driver_pb2.GetNodesResponse]
    """Return a set of nodes"""

    CreateTasks: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.CreateTasksRequest,
        flwr.proto.driver_pb2.CreateTasksResponse]
    """Create one or more tasks"""

    GetResults: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.GetResultsRequest,
        flwr.proto.driver_pb2.GetResultsResponse]
    """Get task results"""


class DriverServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetNodes(self,
        request: flwr.proto.driver_pb2.GetNodesRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.driver_pb2.GetNodesResponse:
        """Return a set of nodes"""
        pass

    @abc.abstractmethod
    def CreateTasks(self,
        request: flwr.proto.driver_pb2.CreateTasksRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.driver_pb2.CreateTasksResponse:
        """Create one or more tasks"""
        pass

    @abc.abstractmethod
    def GetResults(self,
        request: flwr.proto.driver_pb2.GetResultsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.driver_pb2.GetResultsResponse:
        """Get task results"""
        pass


def add_DriverServicer_to_server(servicer: DriverServicer, server: grpc.Server) -> None: ...
