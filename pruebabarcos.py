import tkinter
from functools import partial

ventana = tkinter.Tk()
tablero = []
largo = 5
sentido = True

def limpiar_tablero():
    for i in tablero:
        for j in i:
            j['background'] = 'gray85'
           
def cambiar_sentido(e):
    global sentido
    sentido = not sentido
    limpiar_tablero()

def apretar(i, j):
    global largo
    if sentido:
        for l in range(largo):
            print(l)
            tablero[i][j+l]['background'] = 'green'
            tablero[i][j+l]['text'] = ' '
    else:
        for l in range(largo):
            print(l)
            tablero[i+l][j]['background'] = 'green'
            tablero[i+l][j]['text'] = ' '
   
def on_enter(i, j, e):
    global largo
    if sentido:
        for l in range(largo):
            print(l)
            tablero[i][j+l]['background'] = 'green'
    else:
        for l in range(largo):
            print(l)
            tablero[i+l][j]['background'] = 'green'
   

def on_leave(i, j, e):
    global largo
    if sentido:
        for l in range(largo):
            if tablero[i][j+l]['text'] != ' ':
                tablero[i][j+l]['background'] = 'gray85'
    else:
        for l in range(largo):
            if tablero[i+l][j]['text'] != ' ':
                tablero[i+l][j]['background'] = 'gray85'
               
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