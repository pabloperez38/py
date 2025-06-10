""""def calculo_factorial(num):
    resultado = 1
    for numero in range (1, num + 1):
        resultado *= numero
    return resultado

result = 5
resultado = calculo_factorial(result)
print("El factorial de", result, "es:", resultado)


def tabla_multiplicar(numero):
    for i in range(1, 11): #Del 1 al 10
        resultado = numero * i 
        print(f"El {numero} multiplicado por {i} es: {resultado}")

valor = int(input("Ingrese un valor: ))
tabla_multiplicar(valor)


def suma_pares(numero):
    suma = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            suma += i
    print(suma)
    
suma_pares(22)



def numero_perfecto(numero):
    suma = 0
    for num in range(1, numero):
        if numero % num == 0:
            suma += num

        if numero == suma:
            return True
        else:
            return False
    
print(numero_perfecto(6))


def numero_perfecto(numero):
    suma = 0
    for num in range(1, numero):
        if numero % num == 0:
            suma += num

    print("Suma total de divisores:", suma)  # Verificamos cuánto da la suma

    if numero == suma:
        return True
    else:
        return False

print(numero_perfecto(6))



def numero_primos(numeros):
    for num in range(2, numeros + 1):
        es_primo = True
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)

numero_primos(20)



def calcular_potencia(base, exponente):
    resultado = base ** exponente
    return resultado

print(calcular_potencia(2, 3))


def numeros_impares(inicio, fin):
    for i in range(inicio, fin + 1):
        if i % 2 != 0:
            print(i)
numeros_impares(2,20)


def generar_secuencia(inicio, fin, incremento):
    for i in range(inicio, fin + 1, incremento):
        print(i)
generar_secuencia(2,40,2)
   

def calculadora_sencilla():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operador = input("Ingresa el operador (+, -, *, /): ")

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: No se puede dividir por cero.")
            return
    else:
        print("Operador no válido. Usa +, -, * o /.")
        return

    print("El resultado es:", resultado)
 

def calculadora_sencilla():

    nota = input("Ingrese una nota: ")
    suma = 0
    cantidad = 0

while nota != "fin":

    suma = suma + float(nota) 
    cantidad += 1
    nota = input("Ingrese una nota: ")

promedio = suma/cantidad

print(f"El promedio es {round(promedio, 2)}")

"""

def calcular_promedio(valor):
    nota = input("Ingrese un número (o Enter para terminar): ")
    suma = 0
    cantidad = 0

    while nota != "":
        suma += float(nota)
        cantidad += 1
        nota = input("Ingrese otro número (o Enter para terminar): ")

    if cantidad > 0:
        promedio = suma / cantidad
        print(f"El resultado es: {promedio}")
    else:
        print("No ingresaste ningún número.")

calcular_promedio()
