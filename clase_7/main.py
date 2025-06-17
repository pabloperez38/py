""" numeros = [1, 2, 3, 4, 5, 6]

print(numeros[0]) 
print(numeros[-1])


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0

for numero in numeros:
    suma += numero

print(suma)


nombres = ["Toni", "Alberto"]
nuevo_nombre = input("Ingresa otro nombre a la lista: ")
nombres.append(nuevo_nombre)
for nombre in nombres:
    print(nombre)

valor = nombres.pop(0)
print(nombres)

numeros = []
multiPares = 0
multiImPares = 0
contador = 0
while True:
    valor = input("Ingrese un número ('fin' para terminar): ")    
    if valor != "fin":
        numeros.append(int(valor))        
        #print("estoy del buble")     
    else:
        print("salí del buble")
        break

for num in numeros:   
    contador += 1
    if num % 2 == 0:
        multiPares += 1
    else:
        multiImPares += 1

print(numeros)
print(f"cantidad: {contador} ")
print(f"cantidad de pares:  {multiPares}")
print(f"cantidad de impares: {multiImPares}" )

lista = []

while True:
    print("\nLista actual:", lista)
    print("1. Agregar un elemento al final")
    print("2. Agregar un elemento al principio")
    print("3. Quitar un elemento al final")
    print("4. Quitar un elemento al principio")
    print("5. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        lista.append(elemento)
    elif opcion == "2":
        elemento = input("Ingrese el elemento a agregar: ")
        lista.insert(0, elemento)
    elif opcion == "3":
        if lista:
            lista.pop()
        else:
            print("La lista está vacía.")
    elif opcion == "4":
        if lista:
            lista.pop(0)
        else:
            print("La lista está vacía.")
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")
   

numeros = []
while True:
    entrada = input("Ingrese un número (o 'fin' para terminar): ")
    if entrada.lower() == "fin":
        break
    numeros.append(int(entrada))

if numeros: 
    mayor = numeros[0] 
    menor = numeros[0]

    for num in numeros: 
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

    print("Número mayor:", mayor)
    print("Número menor:", menor)
else:
    print("La lista está vacía.")

""" 

numeros = [7, 2, 9, 1, 6, 3, 8, 15]
print("Lista original:", numeros)
contador = 0
# Orden ascendente
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        print(f"i: {numeros[i]}")
        print(f"j: {numeros[j]}")
        contador += 1
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("Lista ordenada ascendente:", numeros)
print("cantidad:", contador)
""" # Orden descendente
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("Lista ordenada descendente:", numeros)
metodo burbuja o bubble sort
"""