import socket
import sys

stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
 
# define la comunicacion del puerto
port = 8766
 
# Connect the socket to the port where the server is listening
server_address = ((host, port))
 
print("conectando")
 
stream_socket.connect(server_address)
 
# envia data
mensaje = 'mensaje'
stream_socket.sendall(mensaje)
 
# responde
data = stream_socket.recv(10)
print(data)
 
print('socket closed')
stream_socket.close()<zz