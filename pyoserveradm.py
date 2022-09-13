from tkinter import *

class Servidor:
    
    def __init__(self):
        self.pantalla = Tk()
        print("pantalla creada")
        self.pantalla.title("Servidor")
        self.pantalla.geometry('200x250')
        self.listframe = []
        for q in range(5):
            frames = Frame(self.pantalla, width=200, height=50)
            frames.config(bg = "black")
            self.listframe.append(frames)
        self.pantalla.mainloop()
