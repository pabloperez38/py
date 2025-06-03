""" import funciones as f

print(f.saludar("yo"))


from funciones import saludar
valor = saludar("Pablo")
print(valor) """



def calcular(cant):

    suma = 0 
    for i in range(cant):
        num = int(input("Ingrese un valor: "))
        suma = suma + num

    return suma/cant

cant = int(input("Ingrese una cantidad: "))
resultado = calcular(cant)
print(resultado)