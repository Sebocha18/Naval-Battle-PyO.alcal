from tkinter import *
import pyojuego
import pyologin


class Menu:
    
    def __init__(self):
        print("iniciando Menu")
        self.v0 = Tk()
        self.v0.title("Pantalla de Inicio")
        #self.v0.config(bg="snow")
        self.v0.geometry('500x500')
        f20 = Frame(self.v0, width=450,height=200)
        f20.config(bg="snow")
        f20.config(bd=2)
        f20.config(relief="ridge")
        f20.pack(side="top")
        img = PhotoImage(file = "barco.png")
        men_img = Label(f20, image = img)
        men_img.pack()

        b04 = Button(self.v0, text='Juego', command= self.mostrar)
        b04.place(x=450,y=400)
        b01 = Button(self.v0, text="Crear Usuario",  font=("Times", 11), foreground = "#ff0000", command=lambda: ejecutar(mostrar(1)))
        b01.place(x=150, y=350)
        b02 = Button(self.v0, text="Acceder al Usuario", font=("Times", 11), foreground = "Steelblue", command=lambda: ejecutar(mostrar(2)))
        b02.place(x=150, y=400)
        b03 = Button(self.v0, text="Cerrar", font=("Times", 11), foreground = "violet", command=lambda: ejecutar(ocultar(v0)))
        b03.place(x=150, y=450)
        self.v0.mainloop()

    def ejecutar(self,f):
        self.v0.after(100, f)

    def mostrar(self):
            self.v0.destroy()
            self.v1 = pyojuego.Tablero()


if __name__ == '__main__':
    m = Menu()