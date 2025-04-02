# Programa de test de las clases Pelicula y Catalogo_peliculas

from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as Catalogo
from excepcions.Own_excepcions import OutOfRangeOptionException
opciones= ["Agregar película", "Listar peliculas", "Eliminar catalogo", "Salir"]


current_option = None

while(current_option != 4):
    try:
        print("Opciones")
        for num_op, opcion in enumerate(opciones):
            print(f" {num_op + 1}. {opcion}")
        current_option = int(input(" Elige una opción [1-4]: "))
        if not 1<=current_option<=4:
            raise OutOfRangeOptionException(1, 4)
        print(f" Opcion {current_option}. {opciones[current_option-1]} seleccionada ".center(50,'#'))
        # Opcion 1 Agregar peliculas
        if current_option == 1:
            nombre_pelicula = input("Intorduce el nombre de la pelicula:")
            nueva_pelicula = Pelicula(nombre_pelicula)
            Catalogo.agregar_pelicula(nueva_pelicula)
            print(f"Pelicula {nombre_pelicula} añadida")
        # Opcion 2 Mostrar peliculas
        elif current_option == 2:
            Catalogo.listar_peliculas()
        # Opcion 3 eliminar peliculas
        elif current_option == 3:
            Catalogo.eliminar()
        # Opcion 4 salir
        elif current_option == 4:
            pass
    except OutOfRangeOptionException as e:
        print(e.message)
    except Exception as e:
        print(e)
else:
    print("Salimos del programa".center(50,'-'))


