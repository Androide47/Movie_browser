import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.pelicula_dao import crear_tabla, borra_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar
from model.data_insert import insert_data

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    
    menu_inicio.add_command(label='Añadir registro en DB', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar registro', command=borra_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)
    
    menu_consultas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
    menu_consultas.add_command(label='Hacer consulta')
    
    configuracion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuración', menu=configuracion)
    configuracion.add_command(label='Ajustes')
    configuracion.add_command(label='Conexión')
    configuracion.add_command(label='Modo de vista')
    configuracion.add_command(label='Datos de prueba', command=insert_data)


    ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=ayuda)
    ayuda.add_command(label='Conseguir ayuda')

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg='black')
        self.id_pelicula = None
        
        self.campo_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
        
    def campo_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre')
        self.label_nombre.config(font=('Arial', 15, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_duracion = tk.Label(self, text='Duración')
        self.label_duracion.config(font=('Arial', 15, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_genero = tk.Label(self, text='Genero')
        self.label_genero.config(font=('Arial', 15, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)
        
        # Campos
        self.nombre_campo = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.nombre_campo)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre.config(width=50)
        
        self.duracion_campo = tk.StringVar()       
        self.entry_duracion = tk.Entry(self, textvariable = self.duracion_campo)
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10)
        self.entry_duracion.config(width=50)

        self.genero_campo = tk.StringVar()       
        self.entry_genero = tk.Entry(self, textvariable = self.genero_campo)
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10)
        self.entry_genero.config(width=50)

        # Botones
        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='black', bg='#006400', cursor='hand', activebackground='green')
        self.button_nuevo.grid(row=3, column=0, padx=10, pady=10)
        
        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='black', bg='#8FBC8F', cursor='hand')
        self.button_guardar.grid(row=3, column=1, padx=10, pady=10)
        
        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='black', bg='#8FBC8F', cursor='hand')
        self.button_cancelar.grid(row=3, column=3, padx=10, pady=10)
        
    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')                        
            
            
        self.button_guardar.config(state='normal')
        self.button_cancelar.config(state='normal')
        
    def deshabilitar_campos(self):
        self.nombre_campo.set('')
        self.genero_campo.set('')
        self.duracion_campo.set('')
        
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')                          
            
        self.button_cancelar.config(state='disabled')
        self.button_guardar.config(state='disabled')

    def guardar_datos(self):
        pelicula = Pelicula(
            self.entry_nombre.get(),
            self.entry_duracion.get(),
            self.entry_genero.get()
        )
        if self.id_pelicula == None:
            guardar(pelicula)
        else:
            editar(pelicula, self.id_pelicula)
            
        self.tabla_peliculas()
        
        self.deshabilitar_campos()
        
    def tabla_peliculas(self):
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        self.tabla = ttk.Treeview(self, column=('Nombre', 'Duración', 'Genero'))
        self.tabla.grid(row=4, column=0, columnspan=4, pady=30, sticky='nse')
        
        #Scrollbar para más de 10 registros
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row = 4, column = 4, sticky= 'nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duración')
        self.tabla.heading('#3', text='Genero')
        
        for p in self.lista_peliculas:
             self.tabla.insert('', 0, text=p[0], value = (p[1], p[2], p[3]))
        
        #boton editar
        self.button_editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg='black', bg='#006400', cursor='hand', activebackground='green')
        self.button_editar.grid(row=5, column=0, padx=10, pady=30)
        
        #boton eliminar
        self.button_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.button_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='black', bg='red', cursor='hand')
        self.button_eliminar.grid(row=5, column=1, padx=10, pady=30)

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection()) ['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            
            self.habilitar_campos()
            self.entry_nombre.insert(0, self.nombre_pelicula)                
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)

        except:
            titulo = 'Edición datos'
            mensaje = 'No se pudo completar la edición'
            messagebox.showerror(titulo, mensaje)
            
        self.tabla_peliculas()
                
    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection()) ['text']
            eliminar(self.id_pelicula)
            titulo = 'Eliminar Pelicula'
            mensaje = 'Pelicula eliminada'
            messagebox.showwarning(titulo, mensaje)
        except:
            titulo = 'Eliminar Pelicula'
            mensaje = 'Error al eliminar pelicula'
            messagebox.showerror(titulo, mensaje)
        
        self.tabla_peliculas()