import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 10000))
msg = ""
msgserv = ""
while msg !="bye" and msgserv !="bye" and msg !="arret" and msgserv !="arret" :
    msg = input("Entrez votre message:")
    client_socket.send(msg.encode())
    msgserv = client_socket.recv(1024).decode()
    print("Message reçu:",msgserv)
client_socket.close()

def reception(client_socket):
    msg = ""
    while msg !="bye" and msgserv !="bye" and msg !="arret" and msgserv !="arret" :
        msg = client_socket.recv(1024).decode()
        print("Message reçu:",msgserv)
