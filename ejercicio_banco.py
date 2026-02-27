
saldo_inicial=1000
canti_operaciones=0

print("CAJERO AUTOMATICO")
canti_operaciones=input("Ingrese la cantidad de operaciones que desea realizar: ")
try:
    canti_operaciones=int(canti_operaciones)
    for i in range(canti_operaciones):
        print("------------------------------")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar saldo")
        op= int(input("Seleccione una opción: "))
        if op==1:
            cantidad_d=int(input("Ingrese la cantidad a depositar: "))
            saldo_inicial=saldo_inicial+cantidad_d
            print("Depósito exitoso. Saldo actual: ", saldo_inicial)
except:
    print("Error: Debe ingresar un número entero para la cantidad de operaciones.")