import socket

server_object = socket.socket()
print("socket created")

# Passing IP address and port as a tuple
server_object.bind(("localhost", 9999))

# It will take 3 connections.
server_object.listen(3) 
print("Waiting for connections...")

# To connect one by one client continuously
while True:
    # accept() gives the client socket and address
    c, address = server_object.accept() 
    
    name = (c.recv(1024).decode())

    print("connected with ", address, name)

    # Here we need to send bytes format not in str fromat
    c.send(bytes("Welcome", "utf-8")) 

    c.close()
