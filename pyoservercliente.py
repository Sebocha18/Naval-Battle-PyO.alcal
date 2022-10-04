from tkinter import *
import socket
import json

class Cliente:
    def __init__(self, ):
        self.servidor = socket.socket()
        self.nombre_host = ""
        self.puerto = ""
        self.data = [["agua","agua","barco","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"]]
            

    def conectar(self,ip = '192.168.68.200', port = 8765):
        self.nombre_host = ip
        self.puerto = port
        self.servidor.connect((self.nombre_host, self.puerto)) #Conecta al servidor
        print("Conectado al servidor")

    def enviar(self, mensaje = ""):
        mensaje = self.data
        mensJson = json.dumps(mensaje)
        self.servidor.send(mensJson.encode()) #Codifica y envía mensajes
        print("Mensaje enviado")
        
    def recibir(self):
        data = self.servidor.recv(1024).decode()
        print(data)