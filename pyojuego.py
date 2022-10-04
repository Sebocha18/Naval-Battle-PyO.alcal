from tkinter import *
from functools import partial
import json
import socket
from pyoservercliente import Cliente
from pyoserverserver import Servidor

class Tablero:
   
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
            self.jugador = Servidor()
            self.jugador.abrir_conexion()
            print(self.jugador.MiIP)
        else:
            self.jugador = Cliente()
            print("cliente")
        self.tabla1 = []
        self.alto1 = 8
        self.ancho1 = 8
        self.tiros = []
        self.listframe3 = []
        self.fila1 = []
        print("Iniciando Tablero")
        self.v1 = Tk()
        self.v1.title('Batalla Naval')
        self.v1.geometry('700x350')
        self.v1.config(cursor="dotbox")
        self.tablero = []
        self.largo = 5
        self.lista = []
        self.sentido = True
       
        f1 = Frame(self.v1, width=1575, height=820)
        f1.config(bg="lightblue")
        f1.config(bd=3)
        f1.config(relief="ridge")
        f1.pack(side="top")
        self.f2 = Frame(self.v1, width=775, height=50)
        self.texto = ""
        self.consola = Label(self.f2, text = self.texto)
        self.consola.pack()
        self.f2.config(bg="snow")
        self.f2.config(bd=2)
        self.f2.config(relief="ridge")
        self.f2.pack(side="top")
        print("creando frames")
        
        
        for f in range(2):
            f3 = Frame(f1, width=1550, height=1000)
            f3.config(bg = "lightblue")
            f3.config(bd = 1)
            f3.config(relief = "groove")
            f3.pack(side = "right")
            self.listframe3.append(f3)
            print("tablero tiros")
        
    
        
        for i in range(self.alto1):
            self.fila1 = []
            for j in range(self.ancho1):
                boton = Button(self.listframe3[0], text=' ', bg = "lightblue", command = partial(self.pulsar, i, j))
                boton.grid(column = j, row = i)
                self.fila1.append(boton)
            self.tabla1.append(self.fila1)
        print("tablero barcos")
        
        
        for x in range(self.ancho1):
            self.lista = []
            for y in range(self.alto1):
                boton18 = Button(self.listframe3[1], text = "", bg = "lightblue", command = partial(self.apretar, x,y))
                boton18.bind("<Enter>", partial(self.on_enter, x, y))
                boton18.bind("<Leave>", partial(self.on_leave, x, y))
                boton18.bind("<Button-3>", partial(self.cambiar_sentido, x, y))
                self.lista.append(boton18)
                boton18.grid(column=y, row=x)
            self.tablero.append(self.lista)
        print("Iniciando ventana")
        self.v1.mainloop()
    def transformar(self, campo1):
        self.campo1 = tablero_str
        tablero_str.json(type(tablero_str))
    
    def pulsar(self, j, i):
        print(self.campo2[j][i])
        if [j, i] not in self.tiros:
            self.tiros.append([j, i])
            print("tiro: " + str(j),str(i))
            self.tabla1[j][i].config(relief = SUNKEN)
            if(self.campo2[j][i] == "barco"):
                self.tabla1[j][i].config(bg="black")
            self.tabla1[j][i].config(text = ' ')
            self.texto = self.consola.cget("text") + "[" + str(j) + "," + str(i) + "] - "
            print(self.texto)
            self.consola.config(text = self.texto)
        else:
            print("Ya ejecutaste esta casilla")
    
    def limpiar_tablero(self,x,y,e):
        for a in self.tablero:
            for b in a:
                i=self.tablero.index(a)
                j=a.index(b)
                if(self.campo1[i][j] == "agua"):
                    b['background'] = 'lightblue'
        self.on_enter(x,y,e)
           
    def cambiar_sentido(self,x, y, e):
        self.sentido = not self.sentido
        self.limpiar_tablero(x,y,e)

    def apretar(self, x, y):
        if self.largo>0:
            self.campo1[x][y] = "barco"
            if self.sentido:
                for ll in range(self.largo):
                    if(y+ll <= 7):
                        self.tablero[x][y+ll]['background'] = 'green'
                        self.tablero[x][y+ll]['text'] = ' '
                        self.campo1[x][y+ll] = "barco"
            else:
                for ll in range(self.largo):
                    if(x+ll <= 7):
                        self.tablero[x+ll][y]['background'] = 'green'
                        self.tablero[x+ll][y]['text'] = ' '
                        self.campo1[x+ll][y] = "barco"
            print(self.campo1)
            self.largo-=1
       
    def on_enter(self, x, y, e):
        if self.sentido:
            for ll in range(self.largo):
                if(y+ll <= 7):
                    self.tablero[x][y+ll]['background'] = 'green'
        else:
            for ll in range(self.largo):
                if(x+ll <= 7):
                    self.tablero[x+ll][y]['background'] = 'green'
       

    def on_leave(self, x, y, e):
        if self.sentido:
            for ll in range(self.largo):
                if(y+ll <= 7):
                    if self.tablero[x][y+ll]['text'] != ' ':
                        self.tablero[x][y+ll]['background'] = 'lightblue'
        else:
            for ll in range(self.largo):
                if(x+ll <= 7):
                    if self.tablero[x+ll][y]['text'] != ' ':
                        self.tablero[x+ll][y]['background'] = 'lightblue'


        
        
if __name__ == '__main__':
    t = Tablero(False)
    print("HOLA")