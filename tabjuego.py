from tkinter import *
from functools import partial


class Tablero:

    def __init__(self):
        self.tabla1 = []
        self.alto1 = 7
        self.ancho1 = 7
        self.tiros = []
        self.listframe3 = []
        print("Iniciando Tablero")
        self.v1 = Tk()
        self.v1.title('Batalla Naval')
        self.v1.geometry('700x350')
        self.v1.config(cursor="dotbox")
        hola = Canvas(self.v1, width=300, height=210)
        hola.pack(expand=YES, fill=BOTH)
        #b3 = Button(hola, text='Atras', bg="red", command=lambda: self.ejecutar(self.pulsar(1,2)))
        #b3.grid(row=1, column=1)
        f1 = Frame(self.v1, width=775, height=320)
        f1.config(bg="lightblue")
        f1.config(bd=3)
        f1.config(relief="ridge")
        f1.pack(side="top")
        f2 = Frame(self.v1, width=775, height=50)
        texto = ""
        self.consola = Label(f2, text=texto)
        self.consola.pack()
        f2.config(bg="snow")
        f2.config(bd=2)
        f2.config(relief="ridge")
        f2.pack(side="top")
        for l in range(3):
            f3 = Frame(f1, width=250, height=250)
            f3.config(bg="lightblue")
            f3.config(bd=1)
            f3.config(relief="groove")
            f3.pack(side="right")
            self.listframe3.append(f3)

            self.tabla1.append(self.fila1)



        print("....")
        self.v1.mainloop()


    def pulsar(self, a, b):
        if [a, b] not in self.tiros:
            self.tiros.append([a, b])
            self.tabla1[a][b].config(relief=SUNKEN)
            self.tabla1[a][b].config(text=' ')
            texto = self.consola.cget("text") + "[" + str(b) + "," + str(a) + "] - "
            print(texto)
            self.consola.config(text=texto)

        else:
            print("Ya ejecutaste esta casilla")



if __name__ == '__main__':
    print("HOLA")
    t = Tablero()

