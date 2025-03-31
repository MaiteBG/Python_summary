from dispositivoEntrada import DispositivoEntrada


class Computadora(DispositivoEntrada):
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
        Computadora.contador_computadoras+=1
        self.id_monitor= Computadora.contador_computadoras


    def __str__(self):
        return f'''{self.nombre}: {self.id_monitor},
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}
        '''


from raton import Raton
from teclado import Teclado
from monitor import Monitor

if __name__ == '__main__':
    raton1 = Raton("HP", "USB")
    raton2 = Raton("Acer", "Bluetooth")
    teclado1 = Teclado("HP","USB")
    teclado2 = Teclado("Dell", "Bluetooth")
    monitor1 = Monitor("HP", 24)
    monitor2 = Monitor("Dell", 26)

    computadora1 = Computadora("HP computer",monitor1,teclado2,raton1)
    computadora2 = Computadora("Gamer computer", monitor2, teclado1, raton1)
    computadora3 = Computadora("New computer", monitor1, teclado2, raton2)
    computadora4 = Computadora("Old computer", monitor2, teclado1, raton1)

    print(computadora1)
    print(computadora2)
    print(computadora3)
    print(computadora4)
