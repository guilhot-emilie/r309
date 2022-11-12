import socket

client_socket = socket.socket()
client_socket.connect((host, port))
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print("bonsoir")
client_socket.close()