# doble corte de control
totalCompra = 0
totalGeneral = 0
contador = 0
contadorGeneral = 0

while True:
    print("1 - Nueva compra")
    print("0 - Terminar día\n")
    opcion = input("Ingrese un valor: ")
    if opcion == "0":
        break
    elif opcion == "1":
        print("*** Nueva compra ***")
        while True:
            entrada= input("Ingrese precio: (fin para terminar) ")
            if entrada.lower() == "fin":
                break
            totalCompra += float(entrada)
            contador+=1

        print(f"Cantidad de productos vendidos: {contador}")
        print(f"El total a pagar es: {totalCompra}")
        totalGeneral = totalGeneral + totalCompra
        contadorGeneral = contadorGeneral + contador
        totalCompra = 0
        contador = 0

print(f"Cantidad de productos vendidos: {contadorGeneral}")
print(f"Total facturado en el día: {totalGeneral}")