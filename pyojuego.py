from tkinter import *
from functools import partial


class Tablero:

    def __init__(self):
        self.tabla1 = []
        self.alto1 = 8
        self.ancho1 = 8
        self.tiros = []
        self.listframe3 = []
        self.fila1 = []
        print("Iniciando Tablero")
        self.v1 = Tk()
        self.v1.title('Batalla Naval')
        self.v1.geometry('700x350')
        self.v1.config(cursor="dotbox")
        hola = Canvas(self.v1, width=30, height=20)
        hola.pack(expand=YES, fill=BOTH)
        #b3 = Button(hola, text='Atras', bg="red", command=lambda: self.ejecutar(self.pulsar(1,2)))
        #b3.grid(row=1, column=1)
        f1 = Frame(self.v1, width=775, height=20)
        f1.config(bg="lightblue")
        f1.config(bd=3)
        f1.config(relief="ridge")
        f1.pack(side="top")
        f2 = Frame(self.v1, width=775, height=50)
        self.texto = ""
        self.consola = Label(f2, text = self.texto)
        self.consola.pack()
        f2.config(bg="snow")
        f2.config(bd=2)
        f2.config(relief="ridge")
        f2.pack(side="top")
        
        def pulsar(self, j, i):
            if [j, i] not in self.tiros:
                self.tiros.append([i, j])
                self.tabla1[j][i].config(relief = SUNKEN)
                self.tabla1[j][i].config(text = ' ')
                self.texto = self.consola.cget("text") + "[" + str(j) + "," + str(i) + "] - "
                print(self.texto)
                self.consola.config(text = self.texto)
            else:
                print("Ya ejecutaste esta casilla")
                
        for n in range(3):
            f3 = Frame(f1, width=250, height=250)
            f3.config(bg = "lightblue")
            f3.config(bd = 1)
            f3.config(relief = "groove")
            f3.pack(side = "right")
            self.listframe3.append(f3)
            self.tabla1.append(self.fila1)
            
        for i in range(self.alto1):
            self.fila1 = []
            for j in range(self.ancho1):
                boton = Button(self.listframe3[1], text=' ', bg = "lightblue", command = partial(pulsar, i, j))
                boton.grid(column = i, row = j)
                self.fila1.append(boton)
            self.tabla1.append(self.fila1)

        print("....")
        self.v1.mainloop()

if __name__ == '__main__':
    print("HOLA")
    t = Tablero()