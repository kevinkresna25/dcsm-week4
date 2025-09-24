package thelol.hello;

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Server implements Hello {
    public Server() {}

    public String sayHello() {
        return "Hello, world from RMI!";
    }

    public static void main(String[] args) {
        try {
            Server obj = new Server();
            Hello stub = (Hello) UnicastRemoteObject.exportObject(obj, 0);

            // PORT DEFAULT 1099
            int port = 50051;
            Registry registry = LocateRegistry.createRegistry(port);
            registry.rebind("Hello", stub);

            System.out.println("RMI Server ready on port " + port);
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
