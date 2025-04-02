

class Orden:
    contador_ordenes = 0

    def __init__(self, comptuadoras):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes

        self.computadoras = comptuadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        to_string_orden = f"Orden {self.id_orden}\n"
        for c in self.computadoras:
            to_string_orden+=c.__str__()+"\n"

        return to_string_orden
