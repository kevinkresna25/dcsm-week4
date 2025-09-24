FROM python:3.10

WORKDIR /app
COPY . /app

ENV PYTHONUNBUFFERED=1

RUN pip install grpcio grpcio-tools

# Generate code from proto
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

CMD ["python", "server.py"]
