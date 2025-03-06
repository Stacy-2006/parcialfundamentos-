import getpass

# Base de datos de usuarios simulada
usuarios = {"Stacy": {"pin": "1234", "saldo": 1000}}

def autenticar_usuario():
    usuario = input("Ingrese su usuario: ")
    pin = input("Ingrese su PIN: ")  # Oculta el input del PIN

    if usuario in usuarios and usuarios[usuario]["pin"] == pin:
        return usuario
    else:
        print("Usuario o PIN incorrecto.")
        return None

def consultar_saldo(usuario):
    print(f"Su saldo actual es: ${usuarios[usuario]['saldo']}")

def depositar(usuario):
    monto = float(input("Ingrese el monto a depositar: "))
    if monto > 0:
        usuarios[usuario]['saldo'] += monto
        print("Depósito exitoso.")
    else:
        print("Monto inválido.")

def retirar(usuario):
    monto = float(input("Ingrese el monto a retirar: "))
    if 0 < monto <= usuarios[usuario]['saldo']:
        usuarios[usuario]['saldo'] -= monto
        print("Retiro exitoso.")
    else:
        print("Fondos insuficientes o monto inválido.")

def cajero():
    usuario = autenticar_usuario()
    if not usuario:
        return

    while True:
        print("\n1. Consultar saldo\n2. Depositar\n3. Retirar\n4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo(usuario)
        elif opcion == "2":
            depositar(usuario)
        elif opcion == "3":
            retirar(usuario)
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción inválida.")

# Ejecutar el cajero automático
cajero()

