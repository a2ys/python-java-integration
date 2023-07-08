import socket

HOST = 'localhost'
PORT = 12345

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen(1)

# Accept a connection
conn, addr = s.accept()
print('Connected by', addr)

# Receive data from the Java client
data = conn.recv(1024)
print('Received:', data.decode())

# Send a response back to the Java client
response = 'Hello from Python'
conn.sendall(response.encode())

# Close the connection
conn.close()
