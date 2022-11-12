import socket

host = socket.gethostname()
server_socket = socket.socket()
server_socket.bind((host, 10000))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
print("bonjour")
conn.send(reply.encode())
conn.close()