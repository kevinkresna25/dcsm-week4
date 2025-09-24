import grpc
from concurrent import futures
import calculator_pb2, calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return calculator_pb2.CalcReply(result=result)

    def Multiply(self, request, context):
        result = request.a * request.b
        return calculator_pb2.CalcReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    print("Calculator gRPC server running on port 50053")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
