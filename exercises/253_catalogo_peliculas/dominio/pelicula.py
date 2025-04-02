# Classe que representa un objecto pelicula

class Pelicula:
    # Constructor
    def __init__(self, nombre):
        self._nombre = nombre

    # Encapsulamiento de _nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Overwrite de __str__
    def __str__(self):
        return self._nombre


if __name__ == "__main__":
    pelicula_1= Pelicula("Batman")
    pelicula_2 = Pelicula("Crepúsuclo")

    print(pelicula_1)
    print(pelicula_2)