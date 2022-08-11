import tkinter
from functools import partial

ventana = tkinter.Tk()
tablero = []
largo = 5
sentido = True

def limpiar_tablero():
    for ii in tablero:
        for jj in ii:
            jj['background'] = 'gray85'
           
def cambiar_sentido(e):
    global sentido
    sentido = not sentido
    limpiar_tablero()

def apretar(ii, jj):
    global largo
    if sentido:
        for ll in range(largo):
            print(ll)
            tablero[ii][jj+ll]['background'] = 'green'
            tablero[ii][jj+ll]['text'] = ' '
    else:
        for ll in range(largo):
            print(ll)
            tablero[ii+ll][jj]['background'] = 'green'
            tablero[ii+ll][jj]['text'] = ' '
   
def on_enter(ii, jj, e):
    global largo
    if sentido:
        for ll in range(largo):
            print(ll)
            tablero[ii][jj+ll]['background'] = 'green'
    else:
        for ll in range(largo):
            print(ll)
            tablero[ii+ll][jj]['background'] = 'green'
   

def on_leave(ii, jj, e):
    global largo
    if sentido:
        for ll in range(largo):
            if tablero[ii][jj+ll]['text'] != ' ':
                tablero[ii][jj+ll]['background'] = 'gray85'
    else:
        for ll in range(largo):
            if tablero[ii+ll][jj]['text'] != ' ':
                tablero[ii+ll][jj]['background'] = 'gray85'
               
for i in range(8):
    lista = []
    for j in range(8):
        boton = tkinter.Button(ventana, text="", command=partial(apretar, i,j))
        boton.bind("<Enter>", partial(on_enter, i, j))
        boton.bind("<Leave>", partial(on_leave, i, j))
        boton.bind("<Button-3>", cambiar_sentido)
        lista.append(boton)
        boton.grid(column=j, row=i)
    tablero.append(lista)

ventana.mainloop()