from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden

print("*** Mundo PC ***")


raton1 = Raton("HP", "USB")
raton2 = Raton("Acer", "Bluetooth")
teclado1 = Teclado("HP" ,"USB")
teclado2 = Teclado("Dell", "Bluetooth")
monitor1 = Monitor("HP", 24)
monitor2 = Monitor("Dell", 26)

computadora1 = Computadora("HP computer" ,monitor1 ,teclado2 ,raton1)
computadora2 = Computadora("Gamer computer", monitor2, teclado1, raton1)
computadora3 = Computadora("New computer", monitor1, teclado2, raton2)
computadora4 = Computadora("Old computer", monitor2, teclado1, raton1)




orden1 = Orden([computadora1,computadora2] )

orden1.agregar_computadora(computadora3)
print(orden1)
