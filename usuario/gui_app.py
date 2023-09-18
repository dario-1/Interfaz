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
        self.etiquetas()
        self.options()
    
    def etiquetas(self):
        self.label_metodo=tk.Label(self,text='Seleccion de Metodo')
        self.label_metodo.config(font=('Arial',12,'bold'))
        self.label_metodo.grid(row=0,column=0,padx=10,pady=10)
        
        self.label_proceso=tk.Label(self,text='Seleccion de Proceso')
        self.label_proceso.config(font=('Arial',12,'bold'))
        self.label_proceso.grid(row=2,column=0,padx=20,pady=20)
    
    def options(self):
        style = tk.ttk.Style()
        style.configure('Menu.TButton', font=('Arial', 12, 'bold'))
        self.met = tk.StringVar(self.root)
        self.met.set("Seleccione un metodo")
        submenu = tk.OptionMenu(self, self.met, "Metodo 1", "Metodo 2")
        submenu.grid(row=1, column=0, padx=20, pady=20)
        self.proces = tk.StringVar(self.root)
        self.proces.set("Seleccione un Proceso")
        submenu1 = tk.OptionMenu(self, self.proces, "Proceso 1", "Proceso 2",
                                 "Proceso 3", "Proceso 4","Proceso 5", "Proceso 6",
                                 "Proceso 7", "Proceso 8","Proceso 9",
                                "Proceso 10","Proceso 11", "Proceso 12")
        submenu1.grid(row=3, column=0, padx=20, pady=20)
        
        
       
        


