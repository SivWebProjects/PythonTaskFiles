from encodings import utf_8
import socket

client_object = socket.socket()

client_object.connect(("localhost", 9999)) #ip address, port number, bytes

name = input("Enter your name: ")

client_object.send(bytes(name, "utf_8"))

print(client_object.recv(1024).decode()) #here 1024 is bufsize, decode used to print in string format nt in byte

