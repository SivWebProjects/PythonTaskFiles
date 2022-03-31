import socket

server_object = socket.socket()
print("socket created")

server_object.bind(("localhost", 9999))# pass ip address and port as tuple

server_object.listen(3) #it will take 3 connections
print("waiting for connections")

#to connect one by one clients continuously we used while loop
while True:
    c, addr = server_object.accept() #accept gives the client socket and address
    
    name = (c.recv(1024).decode())

    #print(name)

    print("connected with ", addr, name)

    c.send(bytes("Welcome", "utf-8")) # here we need to send bytes format not in str fromat

    c.close()



