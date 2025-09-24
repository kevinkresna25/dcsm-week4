import grpc
import calculator_pb2, calculator_pb2_grpc

def run():
    with grpc.insecure_channel("grpc-python-server:50053") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        print("--- Memanggil Metode Kalkulator gRPC ---")

        # Memanggil Add
        add_response = stub.Add(calculator_pb2.CalcRequest(a=10, b=5))
        print(f"Add(10, 5) = {add_response.result}")

        # Memanggil Multiply
        mul_response = stub.Multiply(calculator_pb2.CalcRequest(a=10, b=5))
        print(f"Multiply(10, 5) = {mul_response.result}")

        # Memanggil Subtract
        sub_response = stub.Subtract(calculator_pb2.CalcRequest(a=10, b=5))
        print(f"Subtract(10, 5) = {sub_response.result}")

        # Memanggil Divide
        div_response = stub.Divide(calculator_pb2.CalcRequest(a=10, b=5))
        print(f"Divide(10, 5) = {div_response.result}")

        print("\n--- Menguji Penanganan Error (Pembagian dengan Nol) ---")
        try:
            stub.Divide(calculator_pb2.CalcRequest(a=10, b=0))
        except grpc.RpcError as e:
            print(f"Berhasil menangkap error yang diharapkan dari server:")
            print(f"  Status Code: {e.code()}")
            print(f"  Detail Pesan: {e.details()}")

if __name__ == "__main__":
    run()
