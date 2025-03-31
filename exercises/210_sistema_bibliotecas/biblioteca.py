
class Biblioteca:

    #No lo usamos porque hay overide del metodo __str__ de la clase libro
    @classmethod
    def mostrar_libro(cls, libro):
        print(f" Título = {libro.titulo}; Autor = {libro.autor}; Titulo = {libro.genero};")


    def __init__(self, nombre_biblioteca):
        self._nombre_biblioteca = nombre_biblioteca
        self._libros = []


    @property
    def nombre_biblioteca(self):
        return  self._nombre_biblioteca

    @property
    def libros(self):
        return  self._libros


    def agregar_libro (self, libro):
        self._libros.append(libro)

    def buscar_libros_por_autor(self, autor):
        return [print(libro) for libro in self._libros if libro.autor.lower() == autor.lower()]

    def buscar_libros_por_genero(self, genero):
        return [print(libro) for libro in self._libros if libro.genero == genero]

    def mostrar_todos_los_libros(self):
        for libro in self._libros:
            print(libro)


