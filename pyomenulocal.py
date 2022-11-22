from tkinter import *
import pyojuego
from functools import partial

class Menu:
    
    def __init__(self):
        print("iniciando Menu")
        self.v0 = Tk()
        self.v0.title("Pantalla de Inicio")
        self.v0.config(bg="snow")
        self.f1 = Frame(self.v0)
        self.f1.grid(column=0, row=0)
        
        self.img = PhotoImage(file = "barco.png", master=self.f1)
        self.men_img = Label(self.f1, bg="snow")
        self.men_img.config(image = self.img)
        self.men_img.pack()
        
        self.f2 = Frame(self.v0, bg ="snow")
        self.f2.grid(column=0,row=1)
        self.f3 = Frame(self.f2, bg ="snow")
        self.f4 = Frame(self.f2, bg ="snow")
        self.f3.grid(column=0, row=1)
        self.f4.grid(column=0, row=0)
        self.v0.resizable(0, 0)

        b03 = Button(self.f4, text="Crear Partida", font=("Times", 12), foreground = "gray85", bg="gray30", command=partial(self.mostrar, True))
        b03.grid(column=0, row=0)
        b04 = Button(self.f4, text="Conectar", font=("Times", 12), foreground = "gray85", bg="gray30", command=partial(self.mostrar,False))
        b04.grid(column=0, row=1)
        self.v0.mainloop()

    def ejecutar(self,f):
        self.v0.after(100, f)

    def mostrar(self, server):
            self.v0.destroy()
            self.v1 = pyojuegolocal.Tablero()

if __name__ == '__main__':
    m = Menu()