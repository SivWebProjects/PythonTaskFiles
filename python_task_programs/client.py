from encodings import utf_8
import socket

client_object = socket.socket()

# IP address, port number, bytes
client_object.connect(("localhost", 9999)) 

name = input("Enter your name: ")

client_object.send(bytes(name, "utf_8"))

# Here 1024 is bufsize, decode used to print in string format not in byte
print(client_object.recv(1024).decode())
