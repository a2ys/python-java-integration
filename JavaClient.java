import java.io.*;
import java.net.*;

public class JavaClient {
    public static void main(String[] args) {
        String hostName = "localhost";
        int portNumber = 12345;

        try (
            Socket socket = new Socket(hostName, portNumber);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        ) {
            // Send a message to the Python server
            out.println("Hello from Java");

            // Receive the response from the Python server
            String response = in.readLine();
            System.out.println("Received: " + response);
        } catch (UnknownHostException e) {
            System.err.println("Unknown host: " + hostName);
        } catch (IOException e) {
            System.err.println("I/O error: " + e.getMessage());
        }
    }
}
