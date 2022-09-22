from tkinter import *
import socket

#Crea nueva instancia del socket
servidor = socket.socket()

def conectar():
    nombre_host = texto2.get()
    puerto = 8766 #Server Puerto
    servidor.connect((nombre_host,puerto)) #Conecta al servidor
    print("Conectado al servidor")

def enviar():
    mensaje = texto.get() #obtiene mensaje para ser enviado
    servidor.send(mensaje.encode()) #Codifica y envía mensajes
    print("Mensaje enviado")
    
ventana = Tk()
texto = Entry(ventana)
boton = Button(ventana, text="Enviar", command=enviar)
texto2 = Entry(ventana)
boton2 = Button(ventana, text="Conectar", command=conectar)
texto2.pack()
boton2.pack()
texto.pack()
boton.pack()
ventana.mainloop()