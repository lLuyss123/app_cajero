
es_vip=False
print("---- Bienvenid@ a Riwi Tech Store ----")
#string
nom_user=input("Ingrese el Nombre del Cliente: ")
#numero decimal
precio_produ=input("Ingrese el Precio del Producto: ")
#numero entero
cantidad_produ_cpmpra= input("Ingrese la Cantidad de producto Comprado: ")
#booleano
es_vip=input("¿El Cliente es VIP? Si es VIP Digite SI/S de lo contrario de enter: ")
#variables
subtotal=0
descuento="N.A"
total_pagar=float(0)
print("** VERICANDO DATOS INGRESADOS **")

#isdecimal no valida numeros decimales como tal
if (precio_produ.isdecimal()):
        precio_produ=float(precio_produ)
else:
        print("El Precio del Producto no es Valido")

if (cantidad_produ_cpmpra.isdigit()):
        cantidad_produ_cpmpra=float (cantidad_produ_cpmpra)
else:
        print("La cantidad de Producto no es Valida")

es_vip=bool(es_vip)
try:
    subtotal=precio_produ*cantidad_produ_cpmpra
    if(es_vip):
            descuento="10%"
            total_pagar=total_pagar-(subtotal*0.10)
    else:
            total_pagar=subtotal

            print(es_vip)

    print("---- Resuemn de la Compra ----")
    print("Nombre del Cliente: ",nom_user)
    print(f"SubTotal: {subtotal}")
    print("Descuento Aplicado: ",descuento)
    print("Total a Pagar: "+str((total_pagar)))

except:
    print("FIN DEL PROGRAMA")
    print("** Precio de producto ingresado anteriormente fue: " +str(precio_produ) )
    print("** Cantidad de producto ingresado anteriormente fue: " +str(cantidad_produ_cpmpra) )







