import socket
import json

# Hard-coded dictionary to send
data_dict = {'slider1': True, 'slider2': False, 'slider3': True}

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('127.0.0.1', 49664)  # Replace with your desired port

# Serialize the dictionary to JSON
data = json.dumps(data_dict).encode('utf-8')

# Send the data to the server
sent = sock.sendto(data, server_address)

print(f"Sent {sent} bytes of data to {server_address}")