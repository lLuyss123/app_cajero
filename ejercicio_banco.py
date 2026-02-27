
saldo_inicial=1000
canti_operaciones=0
#Variable bool que me va a permitir verificar los datos ingresados por el usuario
validacion=True

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
        while validacion:
            if op==2:
                cantidad= int(input("Ingrese la cantidad a retirar: "))
                if cantidad>saldo_inicial:
                    print("Tu saldo es insuficiente para realizar la transacción.")
                    validacion=False
                elif cantidad <0:
                    print("No puedes retirar una cantidad negativa.")
                else:
                    saldo_inicial= saldo_inicial-cantidad
                    print("Transacción exitosa. Su nuevo saldo es: ", saldo_inicial)
                    validacion=False
except:
    print("Error: Debe ingresar un número entero para la cantidad de operaciones.")