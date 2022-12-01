from tkinter import *
import pyobasededatos
from tkinter import messagebox as MessageBox
import json
import random
from functools import partial
from pyomenulocal import Menu
#from pyomenu import Menu

class ScreenLogin:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Inicia o Crea tu Usuario")
        self.ventana.resizable(0, 0)
        mainFrame = Frame(self.ventana)
        mainFrame.pack()
        titulo = Label(mainFrame, text="Login de Usuario", font=("Arial 24"), bg ="lightblue")
        titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        mainFrame.config(width=400, height=200, bg= "lightblue")
        iniciarSesion = Button(mainFrame, command=self.verificar_uc, text="Iniciar sesión", bg = "steelblue")
        iniciarSesion.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        registroUsuario = Button(mainFrame, command=self.registrar_usuario, text="Registrar", bg = "steelblue")
        registroUsuario.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
        nombreLabel = Label(mainFrame, text="Nombre: ", bg = "lightblue")
        nombreLabel.grid(column=0, row=1)
        contrasenaLabel = Label(mainFrame, text="Contraseña: ", bg = "lightblue")
        contrasenaLabel.grid(column=0, row=2)
        self.nombreUsuario= StringVar()
        nombreEntry = Entry(mainFrame, textvariable=self.nombreUsuario)
        nombreEntry.grid(column=1, row=1)
        self.contrasenaUsuario= StringVar()
        contrasenaEntry = Entry(mainFrame, textvariable=self.contrasenaUsuario, show="*")
        contrasenaEntry.grid(column=1, row=2)
        self.base = pyobasededatos.Base()
        self.ventana.mainloop()
    
    def registrar_usuario(self):
        nombre= self.nombreUsuario.get()
        contrasena= self.contrasenaUsuario.get()
        if nombre and contrasena:
            resp = self.base.registro_usuario(nombre, contrasena)
            print(self.base.respuestas_registrousuario[resp])
        else:
            print("Faltan datos")
    
    def verificar_uc(self):
        nombre = self.nombreUsuario.get()
        contrasena = self.contrasenaUsuario.get()
        if nombre and contrasena:
            resp = self.base.iniciar_sesion(nombre, contrasena)
            print(self.base.respuestas_login[resp])
            self.ventana.state(newstate='withdraw')
            if resp == 0:
                MessageBox.showinfo("Sesion Iniciada", "El Usuario se a iniciado de forma exitosa.")
                sig = Menu()
            if resp == 1:
                MessageBox.showerror("Error #1", "La contraseña del usuario es incorrecta.")
                sig2 = ScreenLogin()
        else:
            MessageBox.showerror("Error #2", "No se a encontrado el usuario en la Base de Datos.")
            sig2 = ScreenLogin()

if __name__ == '__main__':
    s = ScreenLogin()