import logging as log
import os

LOG_FILE_NAME = 'capa_datos.log'
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler(LOG_FILE_NAME),
                    log.StreamHandler()
                ])

def clear_log_file(log_file=LOG_FILE_NAME):
    with open(log_file, 'w') as f:
        f.truncate(0)  # Vacía el archivo

if __name__ == '__main__':
    #clear_log_file()
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')