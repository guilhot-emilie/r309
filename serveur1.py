import socket

host = socket.gethostname()
server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 10000))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
print ("Message reçu:",data)
reply = "bonjour"
conn.send(reply.encode())
conn.close()