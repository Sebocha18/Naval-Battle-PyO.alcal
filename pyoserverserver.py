import socket
import json

class Servidor:
    def __init__(self):
        print("server creado")
        self.Port = 8765 #Puerto al servidor host en
        self.maxConnections = 999
        self.nombre = socket.gethostname() #IP de la computadora local
        self.MiIP = socket.gethostbyname(self.nombre + ".local" )
        self.clientsocket = None
        self.address = None
        self.data = "Hello Server!";
        self.running = True        
    
    def enviar(self):
        self.clientsocket.send(self.data.encode());
        pass
    
    def recibir(self):
        while self.running:
            message = self.clientsocket.recv(1024).decode() #Recibe el nuevo mensaje
            if not message == "":
                print(message)
                print(json.loads(message)[0])
                self.running = False
        self.running = True
    
    def abrir_conexion(self):
        servidor_abierto = socket.socket()
        servidor_abierto.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor_abierto.bind(('',self.Port))        
        servidor_abierto.listen(self.maxConnections)
        print("Server comenzado en: " + self.MiIP + " en el puerto " + str(self.Port))
        (self.clientsocket, self.address) = servidor_abierto.accept()
        print(self.clientsocket.getsockname())