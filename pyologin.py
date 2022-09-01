from tkinter import *
import sqlite3
import bcrypt


def encriptar(password):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    return hashed.decode('utf-8')

def chechPas(password, hashed):
    if bcrypt.checkpw(password, hashed):
        return True
    else:
        return False

class Base:
    def __init__(self):
        self.db = sqlite3.connect("usuarios.db")
        self.c = self.db.cursor()
        self.respuestas_login = ["login ok", "Contraseña incorrecta", "No existe usuario"]
        self.respuestas_contrasenia = ["cambio ok", "error old passw"]

    def alta_usuario(self, nom, passw, nusr):
        passw = encriptar(passw)
        
        if not self.existe_usuario(nusr):
            self.c.execute(f'INSERT INTO USUARIOS (NUSUARIO, CONTRASENIA, NOMBRE) VALUES ("{nusr}", "{passw}", "{nom}");')
            self.db.commit()
            return 0
        else:
            return 1

    def login(self, passw, nusr):
        self.c.execute(f'SELECT * FROM USUARIOS WHERE NUSUARIO ="{nusr}";')
        resp = self.c.fetchall()
        p = resp[0][2].strip("'(),")
        password = bytes(p, 'utf-8')
        if resp:
            if chechPas(bytes(passw, 'utf-8'), password):
                return 0
            else:
                return 1
        else:
            return 2

    def existe_usuario(self, nusr):
        self.c.execute(f'SELECT * FROM USUARIOS WHERE NUSUARIO ="{nusr}";')
        resp = self.c.fetchall()
        if resp:
            return True
        return False

    def cambiar_contrasenia(self, old_passw, new_passw, nusr):
        if self.login(old_passw, nusr) == 0:
            new_passw = encriptar(new_passw)
            self.c.execute(f'UPDATE USUARIOS SET CONTRASENIA = {new_passw} WHERE NUSUARIO ="{nusr}";')
            self.db.commit()
        else:
            return 1
        return 0