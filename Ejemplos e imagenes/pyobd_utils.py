import sqlite3
import random

bd = sqlite3.connect('/home/alcal/Documentos/clashroluby/ClashRoluby/Juego/BDCLash.db')
c = bd.cursor()

def traer_carta_random():
    c.execute("SELECT ID FROM CARTAS")
    ids = c.fetchall()
    pos = random.randint(0,len(ids)-1)
    #print(ids[pos][0])
    id_busqueda = ids[pos][0]
    c.execute(f"SELECT URLFOTO, VIDA, DANIO, VELOCIDAD, NOMBRE FROM CARTAS WHERE ID = {id_busqueda} ")
    resp = c.fetchall()
    url = resp[0][0]
    vida = resp[0][1]
    danio = resp[0][2]
    velocidad = resp[0][3]
    nombre = resp[0][4]
    lista = url.split("/")
    pre = 'https://www.deckshop.pro/img/card_ed/'
    post = '.png'
    url_foto = pre + lista[len(lista)-1] + post
    return (url_foto, vida, danio, velocidad, nombre)


def traer_url_foto_por_id(id_busqueda):
    c.execute(f"SELECT URLFOTO FROM CARTAS WHERE ID = {id_busqueda} ")
    resp = c.fetchall()
    url = resp[0][0]
    lista = url.split("/")
    pre = 'https://www.deckshop.pro/img/card_ed/'
    post = '.png'
    url_foto = pre + lista[len(lista)-1] + post
    return url_foto

def crear_usuario(nombre, usr, passw):
    #tomo usr y passw y lo guardo en la base de datos
    c.execute(f'INSERT INTO USUARIOS (NOMBRE, USUARIO, CONTRASENIA) VALUES("{nombre}", "{usr}","{passw}")' )
    bd.commit()

def buscar_usuario(usr):
    c.execute(f'SELECT USUARIO WHERE "{usr}" = "{usr}"')
    usr_bd = resp[1][1]
   # if usr_bd == "{usr}":
        #print("Ese nombre de usuario ya existe")

def loguear(usr, passw):
    #tomo usr y passw y me fijo si existe en la base de datos y si coincide con la pass
    #devuelvo true o false según si coincide la passw
    #return True/False
    c.execute(f'SELECT * FROM USUARIOS WHERE USUARIO = "{usr}";')
    resp = self.c.fetchall()
    if resp[0][2] == passw:
        return True
    return False

'''def existe_usuario():
    c.execute(f'SELECT * FROM USUARIOS WHERE USUARIO = "{usr}";')
    resp = self.c.fetchall()
    if resp:
        return True
    return False
if not self.existe_usuario'''
