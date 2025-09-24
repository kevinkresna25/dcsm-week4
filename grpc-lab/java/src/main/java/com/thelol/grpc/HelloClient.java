package com.thelol.grpc;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import com.thelol.grpc.GreeterGrpc;
import com.thelol.grpc.HelloRequest;
import com.thelol.grpc.HelloReply;


public class HelloClient {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder.forAddress("grpc-java-server", 50052)
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
