from tkinter import *
#Imports library
import socket

#Creates instance of 'Socket'
s = socket.socket()

def conectar():
    hostname = texto2.get()
    port = 8766 #Server Port
    s.connect((hostname,port)) #Connects to server

def enviar():
    x = texto.get() #Gets the message to be sent
    s.send(x.encode()) #Encodes and sends message (x)

ventana = Tk()
texto = Entry(ventana)
boton = Button(ventana, text="Enviar", command=enviar)
texto2 = Entry(ventana)
boton2 = Button(ventana, text="Conectar", command=conectar)
texto.pack()
boton.pack()
texto2.pack()
boton2.pack()
ventana.mainloop()