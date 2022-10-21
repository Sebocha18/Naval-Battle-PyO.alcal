from tkinter import *
import pyobd_utilsxav
import json
import random
from functools import partial
from pyojuego import Tablero

class ScreenLogin:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Login Usuario")
        mainFrame = Frame(self.ventana)
        mainFrame.pack()
        titulo = Label(mainFrame, text="Login de Usuario", font=("Arial 24"))
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        mainFrame.config(width=400, height=200) #bg= "#1AA1EE")
        iniciarSesion = Button(mainFrame, command=self.verificar_uc, text="Iniciar sesión")
        iniciarSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        registroUsuario = Button(mainFrame, command=self.registrar_usuario, text="Registrar")
        registroUsuario.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        nombreLabel = Label(mainFrame, text="Nombre: ")
        nombreLabel.grid(column=0, row=1)
        contrasenaLabel = Label(mainFrame, text="Contraseña: ")
        contrasenaLabel.grid(column=0, row=2)
        self.nombreUsuario= StringVar()
        nombreEntry = Entry(mainFrame, textvariable=self.nombreUsuario)
        nombreEntry.grid(column=1, row=1)
        self.contrasenaUsuario= StringVar()
        contrasenaEntry = Entry(mainFrame, textvariable=self.contrasenaUsuario, show="*")
        contrasenaEntry.grid(column=1, row=2)
        self.base = pyobd_utilsxav.Base()
    
    def registrar_usuario(self):
        nombre= self.nombreUsuario.get()
        contrasena= self.contrasenaUsuario.get()
        if nombre and contrasena:
            resp = self.base.registro_usuario(nombre, contrasena)
            print(self.base.respuestas_registrousuario[resp])
        else:
            print("Faltan datos")
    
    def verificar_uc(self):
        nombre= self.nombreUsuario.get()
        contrasena= self.contrasenaUsuario.get()
        if nombre and contrasena:
            resp = self.base.iniciar_sesion(nombre, contrasena)
            print(self.base.respuestas_login[resp])
            self.ventana.state(newstate='withdraw')
            sig= Tablero()
        else:
            print("Faltan datos")