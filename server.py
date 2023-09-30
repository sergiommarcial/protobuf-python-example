import grpc
from concurrent import futures
import example_pb2 as ProtoService
import example_pb2_grpc as ProtoServiceGrcp


class MyService():
    def GetData(self, request, context):
        return ProtoService.DataResponse(reply=f"Hello, {request.message}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ProtoServiceGrcp.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()


# python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. ./example.proto

# python3 -m pip3 install grpcio
# python3 -m pip3 install grpcio-tools
