saldo = 2000


contrasena_correcta = "225125"


intentos_maximos = 3
intentos = 0


def ingresar_contrasena():
    global intentos
    contrasena = input("Ingresa tu contraseña: ")
    if contrasena == contrasena_correcta:
        return True
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intentos restantes: {intentos_maximos - intentos}")
        return False


def mostrar_menu():
    print("\nMenú:")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar fondos")
    print("4. Transferir fondos")
    print("5. Salir")


def consultar_saldo():
    print(f"Saldo disponible: Q{saldo}")


def retirar_dinero():
    global saldo
    monto = int(input("cuanto quieres retirar ( billetes de 100 o 50): "))
    if monto % 50 == 0 and monto <= saldo:
        saldo -= monto
        print(f"Retiraste Q{monto}. Te queda: Q{saldo}")
    else:
        print("Monto inválido o saldo insuficiente.")


def depositar_fondos():
    global saldo
    monto = int(input("I monto a depositar (entre 50 y 2000): "))
    if 50 <= monto <= 2000:
        saldo += monto
        print(f"Depósito exitoso. Te queda: Q{saldo}")
    else:
        print("no esta permitido jejeje.")


def transferir_fondos():
    global saldo
    cuenta_destino = input("Ingresa el número de cuenta destino (XXXX-XX-XXXX): ")
    if cuenta_destino.count("-") == 2 and cuenta_destino.replace("-", "").isdigit():
        monto = int(input("Ingresa el monto a transferir: "))
        if monto <= saldo:
            saldo -= monto
            print(f"Transferencia exitosa. Saldo restante: ${saldo}")
        else:
            print("Saldo insuficiente para realizar la transferencia.")
    else:
        print("Número de cuenta inválido.")


while intentos < intentos_maximos:
    if ingresar_contrasena():
        while True:
            mostrar_menu()
            opcion = input("Selecciona una opción (1-5): ")
            if opcion == "1":
                consultar_saldo()
            elif opcion == "2":
                retirar_dinero()
            elif opcion == "3":
                depositar_fondos()
            elif opcion == "4":
                transferir_fondos()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.")
else:
    print("Sin intentos salgase de aqui😫")