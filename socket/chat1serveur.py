import socket

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 10000))
server_socket.listen(1)
msg = ""
msgserv = ""
while msg !="arret" and msgserv !="arret" :
    conn, address = server_socket.accept()
    msgserv = msg = ""
    while msg !="bye" and msgserv !="bye" and msg !="arret" and msgserv !="arret" :
        msg= conn.recv(1024).decode()
        print("Message reçu:",msg)
        if msg == "bye":
            conn.send("bye".encode())
        else:
            msgserv = input("Entrez votre message:")
            conn.send(msgserv.encode())
    conn.close()
server_socket.close()

