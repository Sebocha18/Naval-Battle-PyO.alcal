import sqlite3
import bcrypt

class Base:
    def __init__(self):
        self.conexion = sqlite3.connect("BDJuego.db")
        self.cursor = self.conexion.cursor()
        self.respuestas_registrousuario = ["El registro de usuario ha sido exitoso", "Ya existe usuario"]
        self.respuestas_login =  ["Inicio de sesión OK", "La contraseña es incorrecta", "El usuario no existe"]
    
    def encriptar(self, contrasena):
        contrasena = contrasena.encode('utf-8')
        hashed = bcrypt.hashpw(contrasena, bcrypt.gensalt(10))
        return hashed.decode('utf-8')

    def checkPas(self, contrasena, hashed):
        if bcrypt.checkpw(contrasena, hashed):
            return True
        else:
            return False

    def guardar_ps(self, id_imdb, nombre, nom_ac, nom_su, tipo, url):
        sql = '''insert into PELICULASYSERIES(ID_IMDB, Nombre, Nombre_aceptado, Nombre_sugerido, Tipo, URL)
    values ("{}", "{}", "{}", "{}", "{}", "{}");'''
        self.cursor.execute(sql.format(id_imdb, nombre, nom_ac, nom_su, tipo, url))
        self.conexion.commit()
        
    def existe_usuario(self, usuario):
        self.cursor.execute('SELECT * FROM USUARIOS WHERE Usuario ="{}";'.format(usuario))
        respuesta = self.cursor.fetchall()
        if respuesta:
            return True
        return False

    def registro_usuario(self, usuario, contrasena):
        contrasena = self.encriptar(contrasena)
        if not self.existe_usuario(usuario):
            sql = '''insert into USUARIOS(Usuario, Contrasena) values ("{}", "{}");'''
            self.cursor.execute(sql.format(usuario, contrasena))
            self.conexion.commit()
            return 0
        else:
            return 1
        
    def iniciar_sesion(self, usuario, contrasena):
        self.cursor.execute('SELECT * FROM USUARIOS WHERE Usuario ="{}";'.format(usuario))
        respuesta = self.cursor.fetchall()   
        if respuesta:
            p = respuesta[0][2].strip("'(),")
            contra = bytes(p, 'utf-8')
            if self.checkPas(bytes(contrasena, 'utf-8'), contra):
                return 0
            else:
                return 1
        else:
            return 2