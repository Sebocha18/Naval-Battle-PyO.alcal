from tkinter import *
from functools import partial

def mostrar(num):
    v1=Toplevel(v0)
    v1.title('Tipo de Registro')
    v1.protocol('WM_DELETE_WINDOW', 'onexit')
    v1.geometry('700x350')
    v1.config(cursor="dotbox")
    if num==1:
        hola=Canvas(v1, width=300, height=210)
        hola.pack(expand=YES, fill=BOTH)
        b3=Button(hola, text='Cerrar', command=lambda: ejecutar(ocultar(v1)))
        b3.grid(row=1, column=1)
        for c in range(3):
            cajaTexto1 = Entry(v1)
            cajaTexto1.pack()
        def guardar():
            valor_fab = cajaTexto1.get()
            c.execute('INSERT INTO FABRICANTES(NOMBRE) VALUES ("{}");'.format(valor_fab))
            bd.commit()
            c.delete(0, END)
        boton = Button(v1, text = "Guardar", command = guardar)
        boton.pack()
        l = Label(v1, text = "Nombre") 
        l.config(font =("Courier", 11))
        l.config(width=0, height=0)
        l.pack()
        Label_middle = Label(v1, text ='Left')
    elif num==2:
        hola = Canvas(v1, width=300, height=210)
        hola.pack(expand=YES, fill=BOTH)
        b3 = Button(hola, text='Cerrar', command=lambda: ejecutar(ocultar(v1)))
        b3.grid(row=1, column=1)
    elif num==3:
        hola = Canvas(v1, width=300, height=210)
        hola.pack(expand=YES, fill=BOTH)
        b3 = Button(hola, text='Cerrar', command=lambda: ejecutar(ocultar(v1)))
        b3.grid(row=1, column=1)
        f1 = Frame(v1, width=775,height=320)
        f1.config(bg="lightblue")
        f1.config(bd=3)
        f1.config(relief="ridge")
        f1.pack(side="top")

        f2 = Frame(v1, width=775,height=50)
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
        alto1 = 8
        ancho1 = 8
        tiros = []

        def pulsar(a,b):
            if [a,b] not in tiros:
                tiros.append([a,b])
                tabla1[a][b].config(relief = SUNKEN)
                tabla1[a][b].config(text = ' ')
                print(b,a)
            else:
                print("Ya ejecutaste esta casilla")

        for i in range(alto1):
            fila1 = []
            for j in range(ancho1):
                boton = Button(listframe3[1], text = ' ', bg = "snow", command = partial(pulsar, i, j))
                boton.grid(column = i,row = j)
                fila1.append(boton)
            tabla1.append(fila1)
        
def ocultar(ventana):
    ventana.destroy()

def ejecutar(f):
    v0.after(200,f)

v0=Tk()
v0.title("Pantalla de Inicio")
v0.geometry('500x500')

b01=Button(v0, text='Crear Usuario', command=lambda: ejecutar(mostrar(1)))
b01.place(x=150,y=250)

b02=Button(v0, text='Acceder al Usuario', command=lambda: ejecutar(mostrar(2)))
b02.place(x=150,y=300)

b03=Button(v0, text='Cerrar', command=lambda: ejecutar(ocultar(v0)))
b03.place(x=150,y=350)

b04=Button(v0, text='Juego', command=lambda: ejecutar(mostrar(3)))
b04.place(x=150,y=400)

v0.mainloop()

class barcos:
    barco_fila = barco_aleatoria(tablero)