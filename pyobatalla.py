from tkinter import *
import pyojuego
from functools import partial



class Menu:
    
    def __init__(self):
        print("iniciando Menu")
        self.v0 = Tk()
        self.v0.title("Pantalla de Inicio")
        #self.v0.config(bg="snow")
        self.f1 = Frame(self.v0)
        self.f1.grid(column=0, row=0)
        img = PhotoImage(file = "barco.png")
        men_img = Label(self.f1, image = img)
        men_img.pack()
        self.f2 = Frame(self.v0)
        self.f2.grid(column=0,row=1)
        self.f3 = Frame(self.f2)
        self.f4 = Frame(self.f2)
        self.f3.grid(column=0, row=0)
        self.f4.grid(column=1, row=0)

       
        b01 = Button(self.f3, text="Crear Usuario",  font=("Times", 11), foreground = "#ff0000", command=lambda: ejecutar(mostrar(1)))
        b01.grid(column=0,row=0)
        b02 = Button(self.f3, text="Acceder al Usuario", font=("Times", 11), foreground = "Steelblue", command=lambda: ejecutar(mostrar(2)))
        b02.grid(column=0,row=1)
        b03 = Button(self.f3, text="Cerrar", font=("Times", 11), foreground = "violet", command=lambda: ejecutar(ocultar(v0)))
        b03.grid(column=0,row=2)
        b05 = Button(self.f4, text="Crear Partida", font=("Times", 11), foreground = "violet", command=partial(self.mostrar, True))
        b05.grid(column=0, row=0)
        b06 = Button(self.f4, text="Conectar", font=("Times", 11), foreground = "violet", command=partial(self.mostrar,False))
        b06.grid(column=0, row=1)
        self.v0.mainloop()

    def ejecutar(self,f):
        self.v0.after(100, f)

    def mostrar(self, server):
            self.v0.destroy()
            self.v1 = pyojuego.Tablero(server)


if __name__ == '__main__':
    m = Menu()