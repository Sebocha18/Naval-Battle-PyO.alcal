from tkinter import *
from functools import partial
import socket


def mostrar(num):
    v1=Toplevel(v0)
    v1.title('Tipo de Registro')
    v1.protocol('WM_DELETE_WINDOW', 'onexit')
    v1.geometry('700x350')
    v1.config(cursor="dotbox")
    if num==1:
        hola=Canvas(v1, width=300, height=210)
        hola.pack(expand=YES, fill=BOTH)
        b3=Button(hola, text='Cerrar', bg="red", command=lambda: ejecutar(ocultar(v1)))
        b3.grid(row=1, column=1)
        texto1 = Label(v1, text="Nombre de Usuario", bg="white", anchor="center")
        texto1.pack(fill = X)
        cajaTexto01 = Entry(v1)
        cajaTexto01.config(insertbackground="SteelBlue")
        cajaTexto01.pack()
        texto2 = Label(v1, text="Correo Electronico", bg="white", anchor="center")
        texto2.pack(fill = X)
        cajaTexto02 = Entry(v1)
        cajaTexto02.config(insertbackground="SteelBlue")
        cajaTexto02.pack()
        texto3 = Label(v1, text="Contraseña de Usuario", bg="white", anchor="center")
        texto3.pack(fill = X)
        cajaTexto03 = Entry(v1)
        cajaTexto03.config(fg="white")
        cajaTexto03.pack()
        def textoCaja():
            text18 = cajaTexto01.get()
            text19 = cajaTexto02.get()
            text20 = cajaTexto03.get()
            print(cajaTexto01, cajaTexto02, cajaTexto03)
        boton = Button(v1, text = "Guardar", bg="green", command = textoCaja)
        boton.pack()
    elif num==2:
        hola = Canvas(v1, width=300, height=210)
        hola.pack(expand=YES, fill=BOTH)
        b3 = Button(hola, text='Atras', bg="red", command=lambda: ejecutar(ocultar(v1)))
        b3.grid(row=1, column=1)
       
    elif num==3:
        hola = Canvas(v1, width=300, height=210)
        hola.pack(expand=YES, fill=BOTH)
        b3 = Button(hola, text='Atras', bg="red", command=lambda: ejecutar(ocultar(v1)))
        b3.grid(row=1, column=1)
        f1 = Frame(v1, width=775,height=320)
        f1.config(bg="lightblue")
        f1.config(bd=3)
        f1.config(relief="ridge")
        f1.pack(side="top")

        f2 = Frame(v1, width=775,height=50)
        texto = ""
        consola= Label(f2,text =texto)
        consola.pack()
        f2.config(bg="snow")
        f2.config(bd=2)
        f2.config(relief="ridge")
        f2.pack(side="top")

        listframe3 = []
        for l in range(3):
            f3 = Frame(f1, width=250, height=250)
            f3.config(bg="lightblue")
            f3.config(bd=1)
            f3.config(relief="groove")
            f3.pack(side="right")
            listframe3.append(f3)
           
        tabla1 = []
        alto1 = 7
        ancho1 = 7
        tiros = []

        def pulsar(a,b):
            if [a,b] not in tiros:
                tiros.append([a,b])
                tabla1[a][b].config(relief = SUNKEN)
                tabla1[a][b].config(text = ' ')
                texto = consola.cget("text") + "[" + str(b) + "," + str(a) + "] - " 
                print(texto)
                consola.config(text = texto)

            else:
                print("Ya ejecutaste esta casilla")

        for i in range(alto1):
            fila1 = []
            for j in range(ancho1):
                boton = Button(listframe3[1], text = ' ', bg = "lightblue", command = partial(pulsar, i, j))
                boton.grid(column = i,row = j)
                fila1.append(boton)
            tabla1.append(fila1)
       
def ocultar(ventana):
    ventana.destroy()

def ejecutar(f):
    v0.after(100,f)

v0=Tk()
v0.title("Pantalla de Inicio")
#v0.config(bg="snow")
v0.geometry('500x500')
f20 = Frame(v0, width=450,height=200)
f20.config(bg="snow")
f20.config(bd=2)
f20.config(relief="ridge")
f20.pack(side="top")
img = PhotoImage(file = "barco.png")
men_img = Label(f20, image = img)
men_img.pack()

b04 = Button(v0, text='Juego', command=lambda: ejecutar(mostrar(3)))
b04.place(x=450,y=400)
b01 = Button(v0, text="Crear Usuario",  font=("Times", 11), foreground = "#ff0000", command=lambda: ejecutar(mostrar(1)))
b01.place(x=150, y=350)
b02 = Button(v0, text="Acceder al Usuario", font=("Times", 11), foreground = "Steelblue", command=lambda: ejecutar(mostrar(2)))
b02.place(x=150, y=400)
b03 = Button(v0, text="Cerrar", font=("Times", 11), foreground = "violet", command=lambda: ejecutar(ocultar(v0)))
b03.place(x=150, y=450)

v0.mainloop()