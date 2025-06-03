""" numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero1} es menor que {numero2}")
elif numero1 == numero2:
    print(f"{numero1} es igual que {numero2}")
else:
    print("los números son cualquier cosa") 
x = 7
if x > 5 or x > 15:
    print("es verdad")
 4 Ingresar un número por teclado del 0 al 10, y mostrar en que rango se encuentra: de 0 a 5 y de 6 a 10

numero = int(input("Ingrese un número: "))

if numero >= 0 and numero <= 5:
    print(f"El número {numero} está entre 0 y 5")
else:
    print(f"El número {numero} está entre 6 y 10")
    """
numero = 1000
porcentaje = 10
multi = numero * porcentaje

resultado = (multi)/100

print(f"el {porcentaje}% de {numero} es {resultado}")