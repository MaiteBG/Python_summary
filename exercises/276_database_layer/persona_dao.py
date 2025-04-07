from logger_base import log
from persona import Persona
from conexion import Conexion


# Classe que realiza las operaciones sobre la base de datos de entidad Persona

class PersonaDao:
    '''
    # Data Access Object (DAO)
     with Create, Read, Update, Delete (CRUD) operations
    '''
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"

    @classmethod
    def selecionar(cls):
        personas = []
        try:
            with Conexion.obtenerConexion() as conexion:  # Ensure connection is controlled
                with conexion.cursor() as cursor:  # Open a fresh cursor within the connection
                    cursor.execute(cls._SELECCIONAR)
                    registros = cursor.fetchall()
                    for registro in registros:
                        persona = Persona(registro[0], registro[1], registro[2], registro[3])
                        personas.append(persona)
        except Exception as e:
            log.error(f"Error while selecting personas: {e}")
            raise
        return personas

    @classmethod
    def insertar(cls, persona):
        try:
            with Conexion.obtenerConexion() as conexion:
                with conexion.cursor() as cursor:
                    valores = (persona.nombre, persona.apellido, persona.email)
                    cursor.execute(cls._INSERTAR, valores)
                    conexion.commit()  # Ensure changes are committed
                    log.debug(f"Persona insertada: {persona}")
                    return cursor.rowcount
        except Exception as e:
            log.error(f"Error while inserting persona: {e}")
            raise

    @classmethod
    def actualizar(cls, persona):
        try:
            with Conexion.obtenerConexion() as conexion:  # Transaction controlled
                with conexion.cursor() as cursor:
                    valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                    cursor.execute(cls._ACTUALIZAR, valores)
                    conexion.commit()  # Commit is essential for updates
                    log.debug(f"Persona actualizada: {persona}")
                    return cursor.rowcount
        except Exception as e:
            log.error(f"Error while updating persona: {e}")
            raise

    @classmethod
    def eliminar(cls, persona):
        try:
            with Conexion.obtenerConexion() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls._ELIMINAR, (persona.id_persona,))
                    conexion.commit()
                    log.debug(f"Persona eliminada: {persona}")
                    return cursor.rowcount
        except Exception as e:
            log.error(f"Error while deleting persona: {e}")
            raise


if __name__ == '__main__':
    # Insertar un registro
    persona1 = Persona(nombre='Juan', apellido='Perez', email='jperez@mail.com')
    personas_insertadas = PersonaDao.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}")

    # Seleccionar objetos
    personas = PersonaDao.selecionar()
    for persona in personas:
        log.debug(persona)


    # Acutalizar un registro
    persona1 = Persona(id_persona=1, nombre='Juan Carlos ', apellido='Perez', email='jperez@mail.com')
    personas_actualizadas = PersonaDao.actualizar(persona1)
    log.debug(f"Personas actualizadas: {personas_actualizadas}")

    # Seleccionar objetos
    personas = PersonaDao.selecionar()
    for persona in personas:
        log.debug(persona)

    # Eliminar un registro
    persona1 = Persona(id_persona=1)
    personas_eliminadas = PersonaDao.eliminar(persona1)
    log.debug(f"Personas actualizadas: {personas_eliminadas}")

    # Seleccionar objetos
    personas = PersonaDao.selecionar()
    for persona in personas:
        log.debug(persona)

