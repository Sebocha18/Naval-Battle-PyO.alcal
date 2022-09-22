from tkinter import *
import socket

class Servidor:
    def __init__(self):
        self.admin = socket.socket
        self.pantalla = Tk()
        print("pantalla creada")
        self.pantalla.title("Servidor")
        self.pantalla.geometry('200x250')
        self.listframe = []
        self.Port = 8768
        self.max_conect = 10
        self.computadora_nombre = socket.gethostname()
        print(self.computadora_nombre)
        self.computadora_IP = socket.gethostbyname(self.computadora_nombre + ".local")
        print(self.computadora_IP)
        for q in range(5):
            frames = Frame(self.pantalla, width=200, height=50)
            frames.config(bg = "black")
            self.listframe.append(frames)
            print("frames creados")
        self.pantalla.mainloop()

'''
    def mandar_tiros(self):
        
        
    def recibir_tiros(self):
        
        
    def enviar_barcos:(self):
        
        
    def rebicir_barcos(self):
        
        
'''

if __name__ == '__main__':
    s = Servidor()
    print("Ejecutado")