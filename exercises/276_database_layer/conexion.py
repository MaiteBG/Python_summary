import psycopg2 as db

# Clase que adminsitra la conexión a la base de datos
class Conexion:
    _DATABASE = ... #String
    _USERNAME = ... #String
    _PASSWORD = ... #String
    _DB_PORT = ... ##String
    _HOST = ... #String
    _conexion = ... #Connection
    _cursor = ... #Cursonr

    @classmethod
    def obtenerConexion(cls):
        ...
        return ...  #Connection

    @classmethod
    def obtenerCursor(cls):
        ...
        return ...  # Cursor

    @classmethod
    def cerrar(cls):
        ...
