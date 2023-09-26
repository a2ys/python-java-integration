import socket
import json

HOST = 'localhost'
PORT = 12345

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Java server
s.connect((HOST, PORT))


def send_request(request):
    # Convert the request to JSON
    json_request = json.dumps(request)

    # Send the JSON-encoded request to the Java server
    s.sendall(json_request.encode())


def receive_response():
    # Receive the response from the Java server
    data = s.recv(1024)

    # Decode the JSON-encoded response
    json_response = data.decode()
    response = json.loads(json_response)

    return response


# Example usage:
request = {"action": "make_move", "move": "e2e4"}
send_request(request)

response = receive_response()
print(response)
