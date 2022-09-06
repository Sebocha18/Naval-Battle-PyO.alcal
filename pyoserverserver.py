import socket

servidor_abierto = socket.socket() #Crea una nueva instancia en el modulo
Port = 8768 #Puerto al servidor host en
maxConnections = 999
nombre = socket.gethostname() #IP de la computadora local
MiIP = socket.gethostbyname(nombre + ".local" )
#MiIP = socket.getsockname()
servidor_abierto.bind(('',Port))
servidor_abierto.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Comienza el servidor
servidor_abierto.listen(maxConnections)
print("Server comenzado en: " + MiIP + " en el puerto " + str(Port))
#Acepta una nueva conexion
(clientsocket, address) = servidor_abierto.accept()
data = "Hello Server!";
clientSocket.send(data.encode());
print("Nueva conexion de: ")

running = True

def funcion1():
    print("funcion1")

def funcion2():
    print("funcion2")
    
funciones_dic = {'f1':funcion1, 'f2':funcion2}

while running:
    message = clientsocket.recv(1024).decode() #Recibe el nuevo mensaje
    if not message == "":
        funciones_dic[message]()