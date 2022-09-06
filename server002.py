import socket

mi_socket = socket.socket()
mi_socket.bind( ('localhost', 8768) )
mi_socket.listen(5)
Port = 8768 #Port to host server on
maxConnections = 999
nombre = socket.gethostname() #IP address of local machine
MiIP = socket.gethostbyname(nombre + ".local" )

while True:
    conexion, addr = mi_socket.accept()
    print("Nueva conexion establecida en " + MiIP)
    print(addr)