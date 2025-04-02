# Activity 107

print('*** Cajero automatico ***')

exit_op = False
saldo = 1300
MAX_RETIRAR = 500  # Maximo que se puede retirar
while not exit_op:
    print("---")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")
    print("---")
    select_op=input("Introduzca el numero de la opcion que quiera realizar:")

    if select_op == '1':
        print('* Opcion 1. Depositar seleccionada *')
        depost_cant = float((input("Cantidad depositada:")))
        saldo += depost_cant

    elif select_op == '2':
        print('* Opcion 2. Retirar seleccionada *')
        retir_cant = float(input("Cantidad depositada:"))
        if retir_cant <= MAX_RETIRAR:
            saldo -=retir_cant
        else: print(f'El maximo que se puede retirar es {MAX_RETIRAR}')

    elif select_op == '3':
        print('* Opcion 3. Consultar saldo seleccionada *')
        print(f'Tu saldo es de {saldo:.2f}')
    elif select_op == '4':
        print('* Opcion 4. Salir seleccionada *')
        exit_op = True
    else:
        print("Numero de operación invalida")
