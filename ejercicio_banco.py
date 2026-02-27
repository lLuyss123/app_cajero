
saldo_inicial=1000
canti_operaciones=0

print("CAJERO AUTOMATICO")
canti_operaciones=input("Ingrese la cantidad de operaciones que desea realizar: ")
try:
    canti_operaciones=int(canti_operaciones)
    for i in range(canti_operaciones):
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar saldo")
        op= int(input("Seleccione una opción: "))
        if op ==3:
            print("Su saldo es: ", saldo_inicial)
except:
    print("Error: Debe ingresar un número entero para la cantidad de operaciones.")