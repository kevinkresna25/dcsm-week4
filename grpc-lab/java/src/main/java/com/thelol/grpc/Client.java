package com.thelol.grpc;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class Client {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder.forAddress("hello-java-server", 50051)
                .usePlaintext()
                .build();

        GreeterGrpc.GreeterBlockingStub stub = GreeterGrpc.newBlockingStub(channel);

        HelloReply response = stub.sayHello(
                HelloRequest.newBuilder().setName("Mahasiswa").build()
        );

        System.out.println("Response: " + response.getMessage());
        channel.shutdown();
    }
}
