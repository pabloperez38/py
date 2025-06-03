"""frase = "HOla, estamos en el curso de Python"
contador = 0

for letra in frase:
    if letra == 'o' or letra == 'O':
        contador += 1
print(f"la letra o aparece {contador} veces")

 numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
contador_pares = 0 
contador_impares = 0 
suma = 0
suma_pares = 0
suma_impares = 0

for num in numeros:
    if num % 2 == 0:
        contador_pares += 1
        suma_pares += num
    else:
        contador_impares += 1
        suma_impares += num
    suma += num

print(f"Hay {contador_pares} números pares")
print(f"Hay {contador_impares} números impares")
print(f"Hay {contador_impares} números impares")
print(f"{suma} suma de valores") 

i = 1
valor = int(input("cuantas vueltas quiere dar? "))
while(i<= valor):
    print(i)
    i+= 2

while True: 
    opcion = (input("Elige una fruta para tu desayuno:
            1- Manzanas
            2- Bananas
            3- Salir
            "))
    if opcion == '1': #Condicionales según la opción que eligió!
        print ("Has seleccionado manzanas")
    elif opcion == '2':
        print ("Has seleccionado bananas")
    elif opcion == '3':
        print ("Saliendo")
        break
    else:
        print ("Debes seleccionar una opcion (1, 2 o 3)")

#n - 1
numero = int(input("ingrese "))
for i in range(numero+1):
    print(i)
    """
suma = 0
contador = 0
while True:
    valor = float(input("Ingrese una nota, -1 para salir"))

    if valor not in -1:
        suma += valor 100
        contador += 1 10
