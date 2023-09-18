# -*- coding: utf-8 -*-
import tkinter as tk
import pandas as pd
from usuario.gui_app import Frame,barra_menu
from tkinter import font
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
import os

def font1(size):
     return font.Font(family="Times New Roman", size=size)
    

def seleccionar_opcion():
    seleccion = variable.get()
    if seleccion == "Maquina 1":
        etiqueta.config(text="Has seleccionado la M\u00e1quina 1")
    elif seleccion == "Maquina 2":
        etiqueta.config(text="Has seleccionado la Maquina 2")



def main():
    root = tk.Tk()
    root.title('Depurador de archivos')
    root.iconbitmap('icono.ico')
    root.resizable(1,1)
    barra_menu(root)
    app=Frame(root=root) 

    app.mainloop()
        
   
if __name__== '__main__':
    main()