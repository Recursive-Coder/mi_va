import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('Raspberry_Pi_IP', 65432))

try:
    while True:
        data = client_socket.recv(1024)
        print(f"Estado del sensor: {data.decode()}")
except KeyboardInterrupt:
    client_socket.close()
