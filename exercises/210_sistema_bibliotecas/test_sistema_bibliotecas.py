from exercises.sistema_bibliotecas_210.biblioteca import Biblioteca
from exercises.sistema_bibliotecas_210.libro import Libro

biblioteca_nacional = Biblioteca("Biblioteca Nacional")

print(f"*** Bienvenidos a {biblioteca_nacional.nombre_biblioteca}")


# Definir libros
libro1 = Libro("Cien años de soledad", "Gabriel", "Ficcion")
libro2 = Libro("quijote", "Miguel", "Comedia")
libro3 = Libro("Amor colera", "Gabriel", "Ficcion")
libro4 = Libro("Pedro Paramos", "Juan", "Ficcion")

# agregar libros
biblioteca_nacional.agregar_libro(libro1)
biblioteca_nacional.agregar_libro(libro2)
biblioteca_nacional.agregar_libro(libro3)
biblioteca_nacional.agregar_libro(libro4)


# Buscar libro autor
autor = "Gabriel"
print(f"Libros de {autor}")
biblioteca_nacional.buscar_libros_por_autor(autor)
print()
# Buscar libros genero
genero = "Ficcion"
print(f"Libro del genero {genero}")
biblioteca_nacional.buscar_libros_por_genero(genero)
print()