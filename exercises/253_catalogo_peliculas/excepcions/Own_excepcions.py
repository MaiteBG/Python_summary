# Classe de excepcion para indicar que el mensaje esta fuera del rango de opciones permitidas
class OutOfRangeOptionException(Exception):
    def __init__(self, ini_range, fin_range, message = ""):
        self.message = f"OutOfRangeOptionException: Opcion fuera del rango de opciones [{ini_range}-{fin_range}] {message}"