import grpc
from concurrent import futures
import calculator_pb2, calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        print(f"Received Add request: a={request.a}, b={request.b}")
        result = request.a + request.b
        return calculator_pb2.CalcReply(result=result)

    def Multiply(self, request, context):
        print(f"Received Multiply request: a={request.a}, b={request.b}")
        result = request.a * request.b
        return calculator_pb2.CalcReply(result=result)

    def Subtract(self, request, context):
        print(f"Received Subtract request: a={request.a}, b={request.b}")
        result = request.a - request.b
        return calculator_pb2.CalcReply(result=result)

    def Divide(self, request, context):
        print(f"Received Divide request: a={request.a}, b={request.b}")
        if request.b == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Pembagian dengan nol tidak diizinkan!')
            return calculator_pb2.CalcReply()
        
        result = int(request.a / request.b)
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
