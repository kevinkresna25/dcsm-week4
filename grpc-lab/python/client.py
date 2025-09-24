import grpc
import calculator_pb2, calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel("grpc-python-server:50053")
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    add_response = stub.Add(calculator_pb2.CalcRequest(a=3, b=5))
    print("Add:", add_response.result)

    mul_response = stub.Multiply(calculator_pb2.CalcRequest(a=4, b=6))
    print("Multiply:", mul_response.result)

if __name__ == "__main__":
    run()
