#Importación de modulos
from tkinter import Tk, Button, Label, Frame, SUNKEN
from functools import partial

#Creación de la Clase
class Tablero:
    #Colocación de agua en el mapa
    campo1 = [["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"],
              ["agua","agua","agua","agua","agua","agua","agua","agua"]]
    
    def __init__(self):
        self.ventana = Tk()
        self.tiros = [] #lista para guardar x,y de nuestros disparos
        self.listatablero = []
        self.tablero = []
        self.texto = ""
        self.largo = 5
        self.sentido = True #herramienta para cambiar el sentido en la colocacion de los barcos
        self.ventana.title("Ordena tus barcos") #titulo a la ventana
        self.ventana.geometry("700x300") #proporciones de la ventana
        self.ventana.config(bg = "SteelBlue4")
        self.ventana.resizable(0, 0) #ventana estatil
        self.framemenu = Frame(self.ventana, width = 700, height = 300)
        self.framemenu.config(bg = "SteelBlue4")
        self.framemenu.pack(side = "top")
        self.frametablero = Frame(self.framemenu, width = 700, height = 200)
        self.frametablero.config(bg = "SteelBlue3")
        self.frametablero.grid(column = 0, row = 0)
        self.filatab = []
        self.tabtab = []
        self.tab = Tk()
        self.tab.title("Disparale al enemigo") #titulo a la ventana
        self.tab.geometry("700x300") #proporciones de la ventana
        self.tab.config(bg = "SteelBlue4")
        self.tab.resizable(0, 0) #ventana estatil
        self.frametiros = Frame(self.tab, width = 700, height = 300)
        self.frametiros.pack(side = "top")
        self.frameconsola = Frame(self.tab, width = 700, height = 100)
        self.frameconsola.pack(side = "bottom")
        self.consola = Label(self.frameconsola, text = self.texto)
        self.consola.pack(side = "bottom")
        
        for i in range(8):
            self.filatab = []
            for j in range(8):
                botontir = Button(self.frametiros, text=' ', bg = "SteelBlue3", command = partial(self.pulsar, i, j))
                botontir.grid(column = j, row = i)
                self.filatab.append(botontir)
            self.tabtab.append(self.filatab)
        
        for x in range(8):
            self.filatablero = []
            for y in range(8):
                boton = Button(self.frametablero, text = "", bg = "SteelBlue3", command = partial(self.apretar, x, y))
                boton.bind("<Enter>", partial(self.on_enter, x, y))
                boton.bind("<Leave>", partial(self.on_leave, x, y))
                boton.bind("<Button-3>", partial(self.cambiar_sentido, x, y))
                self.filatablero.append(boton)
                boton.grid(column = y, row = x)
            self.tablero.append(self.filatablero)
            
        self.botonsiguiente = Button(self.framemenu, text = "Ocultar Ventana", bg = "dark olive green", command = self.ventana.iconify)
        self.botonsiguiente.grid(column = 0, row = 12)
        
        self.tab.mainloop()
        self.ventana.mainloop() #mostrar ventana
            
    def apretar(self, x, y):
        if self.largo>0:
            self.campo1[x][y] = "barco"
            if self.sentido:
                for i in range(self.largo):
                    if(y+i <= 7):
                        self.tablero[x][y+i]['background'] = 'green'
                        self.tablero[x][y+i]['text'] = ' '
                        self.campo1[x][y+i] = "barco"
            else:
                for i in range(self.largo):
                    if(x+i <= 7):
                        self.tablero[x+i][y]['background'] = 'green'
                        self.tablero[x+i][y]['text'] = ' '
                        self.campo1[x+i][y] = "barco"
        self.largo-=1
        print("Te quedan colocar {0} barcos".format(self.largo))
        if self.largo == 0:
            print("Has colocado todos los barcos. Apreta en 'Ocultar Ventana' ahora ¡llama a un amigo para bombardearte!")
        
    def limpiar_tablero(self,x,y,e):
        for a in self.tablero:
            for b in a:
                i=self.tablero.index(a)
                j=a.index(b)
                if(self.campo1[i][j] == "agua"):
                    b['background'] = 'SteelBlue3'
        self.on_enter(x,y,e)
       
       
    def cambiar_sentido(self,x, y, e):
        self.sentido = not self.sentido
        self.limpiar_tablero(x,y,e)
       
       
    def on_enter(self, x, y, e):
        if self.sentido:
            for i in range(self.largo):
                if(y+i <= 7):
                    self.tablero[x][y+i]['background'] = 'green'
        else:
            for i in range(self.largo):
                if(x+i <= 7):
                    self.tablero[x+i][y]['background'] = 'green'
       

    def on_leave(self, x, y, e):
        if self.sentido:
            for i in range(self.largo):
                if(y+i <= 7):
                    if self.tablero[x][y+i]['text'] != ' ':
                        self.tablero[x][y+i]['background'] = 'SteelBlue3'
        else:
            for i in range(self.largo):
                if(x+i <= 7):
                    if self.tablero[x+i][y]['text'] != ' ':
                        self.tablero[x+i][y]['background'] = 'SteelBlue3'

    '''def tirar(self):
        '''
            
    def pulsar(self, j, i):
        if [j, i] not in self.tiros:
            self.tiros.append([j, i])
            print("-----")
            print("Tu tiro fue a la cordenada: " + str(j) + "," + str(i) + " y resulto ser: " + self.campo1[j][i])
            self.tabtab[j][i].config(relief = SUNKEN)
            if(self.campo1[j][i] == "barco"):
                self.tabtab[j][i].config(bg="black")
            self.tabtab[j][i].config(text = ' ')
            self.texto = self.consola.cget("text") + "[" + str(j) + "," + str(i) + "] - "
            self.consola.config(text = self.texto)
        else:
            print("Ya ejecutaste esta casilla")
        print(self.campo1)
                
    '''def hundir():
        '''
        
if __name__ == '__main__':
    t = Tablero()