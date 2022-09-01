import socket
import sys
import time

print("Welcome to python chat ")
print("")
print("Initiallsing....")
time.sleep(1)

s = socket.socket()
print("")
host = input(str("Please enter server adress : "))
print("")
name = input(str("Please enter your name : "))
port = 8080
print("")
time.sleep(1)
s.connect((host,port))
print("Connected...")

## Conection done ##

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print("")
print( s_name, "has joined the chat room ")

while 1:
    message = s.recv(1024)
    message = message.decode()
    print("")
    print(name,": ",message)
    print("")
    message = input(str("Please enter your enter message : "))
    print("")
    s.send(message.encode())