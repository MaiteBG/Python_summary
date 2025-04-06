
class Persona:

    def __init__(self, nombre, apellido, id_persona=None, email = None):
        self._id_persona = ...
        self._nombre = nombre
        self._apellido = apellido
        self._email = ...

    def __str__(self):
        ...

    # get/set id_persona
    @property
    def id_persona(self):
        return  self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    # get/set nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # get/set apellido
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # get/set email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


