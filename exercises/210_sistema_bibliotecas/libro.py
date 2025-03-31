
class Libro:
    '''
    Classe de define libro
    '''

    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero


    # Solo metodos get, ya no queremos modificar los atributos
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero


    def __str__(self):
        return f" Título = {self._titulo}; Autor = {self._autor}; Titulo = {self._genero};"