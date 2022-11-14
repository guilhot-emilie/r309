import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 10000))
message = "bonsoir"
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print("Message reçu:",data)
client_socket.close()