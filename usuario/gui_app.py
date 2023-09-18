import tkinter as tk
def barra_menu(root):
    barra_menu=tk.Menu(root)
    root.config(menu=barra_menu, width=420,height=200)
    
    menu_inicio=tk.Menu(barra_menu)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    
    menu_inicio.add_command(label='Analisis en Equipo1')
    menu_inicio.add_command(label='Analisis en Equipo2')
    menu_inicio.add_command(label='Salir',command=root.destroy)



class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=800,height=700)
        self.root=root
        self.pack()
        self.config(bg='green')
        self.seleccion_metodo()
    
    def seleccion_metodo(self):
        self.label_nombre=tk.Label(self,text='Seleccion de Metodo')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0)
        


