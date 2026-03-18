saldo_cajero = 1000

def consultar_saldo():
    print(f"\nSu saldo actual es: ${saldo_cajero:.2f}")

def retirar_dinero():
    global saldo_cajero
    try:
        cantidad_retiro = float(input("Ingrese la cantidad a retirar: $"))
        
        if cantidad_retiro <= 0:
            print("Ingrese una cantidad válida.")
        elif cantidad_retiro > saldo_cajero:
            print("No tienes suficientes fondos.")
        else:
            saldo_cajero -= cantidad_retiro
            print(f"Retiraste: ${cantidad_retiro:.2f}")
            print(f"Tu saldo actual es: ${saldo_cajero:.2f}")
    
    except ValueError:
        print("Error: Ingrese un número válido.")

def depositar_dinero():
    global saldo_cajero
    try:
        cantidad_depositar = float(input("Ingrese la cantidad a depositar: $"))
        
        if cantidad_depositar <= 0:
            print("Ingrese una cantidad válida.")
        else:
            saldo_cajero += cantidad_depositar
            print(f"Depositaste: ${cantidad_depositar:.2f}")
            print(f"Tu saldo actual es: ${saldo_cajero:.2f}")
    
    except ValueError:
        print("Error: Ingrese un número válido.")

def mostrar_menu():
    print("\n=== Cajero Automático ===")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

while True:
    mostrar_menu()
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue

    if opcion == 1:
        consultar_saldo()
    elif opcion == 2:
        retirar_dinero()
    elif opcion == 3:
        depositar_dinero()
    elif opcion == 4:
        print("Gracias por usar el cajero automático.")
        break
    else:
        print("Opción inválida.")

