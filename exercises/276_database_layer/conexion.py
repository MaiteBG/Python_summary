import os
import sys

import psycopg2  as bd  # Librería para conectarse a PostgreSQL con Python
from logger_base import log

from dotenv import load_dotenv  # para importar las varaibles del .env
# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Conexion:
    # Leer las variables de entorno del archivo .env
    _USERNAME = os.getenv('POSTGRE_USER')
    _PASSWORD = os.getenv('POSTGRE_PASSWORD')
    _HOST = os.getenv('POSTGRE_HOST')
    _DB_PORT = os.getenv('POSTGRE_PORT')
    _DATABASE = os.getenv('POSTGRE_DB')
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None: # Si no hay conexión extablecida
            try:
                cls._conexion = bd.connect(host = cls._HOST,
                                           user = cls._USERNAME,
                                           password = cls._PASSWORD,
                                           port = cls._DB_PORT,
                                           database = cls._DATABASE)
                log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error((f"Ocurrio una excepcion al obtener la conexion: {e}"))
                sys.exit() # Terminamos el programa

        return cls._conexion


    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f"Se abrio correctaemtne el cursor: {cls._cursor}")
            except Exception as e:
                log.error(f"Ocurrio una excepción al obtener el cursor: {e}")
                sys.exit()  # Terminamos el programa
        return cls._cursor

    @classmethod
    def cerrar(cls):
        ...




# Si quieres probar la conexión:
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
