#Importación de modulos
from tkinter import Tk, Button, Label, Frame, SUNKEN
from functools import partial
from pyoservercliente import Cliente
from pyoserverserver import Servidor

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
    
    def __init__(self):
        self.ventana = Tk()
        self.tiros =[] #lista para guardar x,y de nuestros disparos
        self.sentido = True #herramienta para cambiar el sentido en la colocacion de los barcos
        self.ventana.title("Ordena tus barcos y dispara") #titulo a la ventana
        self.ventana.geometry("700x300") #proporciones de la ventana
        self.ventana.resizable(0,0) #ventana estatil
        self.ventana.mainloop() #mostrar ventana

if __name__ == '__main__':
    t = Tablero()