import socket
import json
import threading

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 49664)
sock.bind(server_address)

# Set socket to non-blocking
sock.setblocking(False)

def receive_data():
    while True:
        try:
            data, address = sock.recvfrom(65535)
            deserialized_data = json.loads(data.decode('utf-8'))
            print(f"Received data from {address}: {deserialized_data}")
        except BlockingIOError:
            pass

# Create a thread for receiving data
threading.Thread(target=receive_data).start()

# Keep the main thread alive
while True:
    pass