#Importación de modulos
from tkinter import
from functools import partial
import socket
from 

#Creación de la Clase
class Tablero:
    #Colocación de agua en el mapa
    campo1 = [["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"]]
    
    campo2 = [["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"]]
    
    def __init__(self, server):
        if server:
            self.jugador