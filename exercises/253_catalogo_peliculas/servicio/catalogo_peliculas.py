# Realiza las operaciones sobre el archivo de peliculas.txt
import os

class CatalogoPeliculas:

    ruta_archivo = "peliculas.txt"

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print("Catalogo de películas".center(50,'-'))
            print(archivo.read())

    # Eliminar el fihcero en question (todas las peliculas)
    @classmethod
    def eliminar(cls):
        os.remove( cls.ruta_archivo)
        print(f'Archivo eliminado')


