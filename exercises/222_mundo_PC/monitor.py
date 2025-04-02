
class Monitor():
    contador_monitores= 0

    def __init__(self, marca, tamanio):
        self.marca = marca
        self.tamanio = tamanio
        Monitor.contador_monitores+=1
        self.id_monitor = Monitor.contador_monitores


    def __str__(self):
        return f"Id = {self.id_monitor}, Marca = {self.marca}, Tamaño = {self.tamanio}"



if __name__ == '__main__':
    monitor1 = Monitor("HP",24)
    print(monitor1)
    monitor2 = Monitor("Dell", 26)
    print(monitor2)