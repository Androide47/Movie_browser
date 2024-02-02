from .conection_db import ConectionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConectionDB()
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:    
        conexion.cursor.execute(sql)
        conexion.close()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya existe'
        messagebox.showwarning(titulo, mensaje)
        
        
def borra_tabla(): 
    conexion = ConectionDB()
    sql = 'DROP TABLE peliculas'
    
    try:
        conexion.cursor.execute(sql)
        conexion.close()
        titulo = 'Borrar tabla'
        mensaje = 'Tabla eliminada'
        messagebox.showinfo(titulo, mensaje)
    except:
        conexion.cursor.execute(sql)
        conexion.close()
        titulo = 'Borrar tabla'
        mensaje = 'La tabla no existe'
        messagebox.showerror(titulo, mensaje)
    
    
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero    
    
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'
    
def guardar(pelicula):
    conexion = ConectionDB()
    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    Values('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.close()
        titulo = 'Conexion al Registro'
        mensaje = '¡Resgitro Guardado con éxito!'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Error al actualizar la base de datos'
        messagebox.showerror(titulo, mensaje)
        
def listar():
    conexion = ConectionDB()
    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'
    
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.close()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Error al actualizar la base de datos'
        messagebox.showerror(titulo, mensaje)
        
    return lista_peliculas   

def editar(pelicula, id_pelicula):
    conexion = ConectionDB()
    sql = f""" UPDATE peliculas
    SET nombre = '{pelicula.nombre}', 
    duracion = '{pelicula.duracion}', 
    genero = '{pelicula.genero}'
    
    WHERE id_pelicula = '{id_pelicula}'
    """
    
    try:
        conexion.cursor.execute(sql)
        conexion.close()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Error al actualizar la base de datos'
        messagebox.WARNING(titulo, mensaje)
        
def eliminar(id_pelicula):
    conexion = ConectionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'
    try:
        conexion.cursor.execute(sql)
        conexion.close()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Error al eliminar pelicula'
        messagebox.WARNING(titulo, mensaje)