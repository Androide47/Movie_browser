from .conection_db import ConectionDB
from tkinter import messagebox


def insert_data():
    conexion = ConectionDB()
    sql = '''
-- Assuming 'peliculas' table has columns: nombre, duracion, genero

INSERT INTO peliculas (nombre, duracion, genero)
VALUES
    ('Inception', 148, 'Sci-Fi'),
    ('The Shawshank Redemption', 142, 'Drama'),
    ('The Godfather', 175, 'Crime'),
    ('Pulp Fiction', 154, 'Crime'),
    ('The Dark Knight', 152, 'Action'),
    ('Forrest Gump', 142, 'Drama'),
    ('The Matrix', 136, 'Action'),
    ('Titanic', 195, 'Romance'),
    ('Avatar', 162, 'Action'),
    ('Jurassic Park', 127, 'Adventure'),
    ('The Silence of the Lambs', 118, 'Thriller'),
    ('The Lord of the Rings: The Fellowship of the Ring', 178, 'Adventure'),
    ('Fight Club', 139, 'Drama'),
    ('The Terminator', 107, 'Sci-Fi'),
    ('The Shawshank Redemption', 142, 'Drama'),
    ('Gladiator', 155, 'Action'),
    ('The Green Mile', 189, 'Crime'),
    ('Schindler''s List', 195, 'Biography'),
    ('The Lion King', 88, 'Animation'),
    ('Eternal Sunshine of the Spotless Mind', 108, 'Drama'),
    ('Inglourious Basterds', 153, 'Adventure'),
    ('The Departed', 151, 'Crime'),
    ('The Grand Budapest Hotel', 99, 'Comedy'),
    ('The Revenant', 156, 'Action'),
    ('Interstellar', 169, 'Adventure'),
    ('The Great Gatsby', 143, 'Drama'),
    ('Casablanca', 102, 'Drama'),
    ('The Wizard of Oz', 102, 'Adventure'),
    ('Incredibles 2', 118, 'Animation'),
    ('La La Land', 128, 'Drama');

    '''
    try:    
        conexion.cursor.execute(sql)
        conexion.close()
        titulo = 'Crear Registro'
        mensaje = 'Se crearon datos de prueba'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'Error al crear datos'
        messagebox.showwarning(titulo, mensaje)