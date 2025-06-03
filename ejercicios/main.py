""" Pide al usuario ingresar notas (números decimales) hasta que ingrese fin. Luego, calcula y muestra el promedio.  """

nota = input("Ingrese una nota: ")
suma = 0
cantidad = 0

while nota != "fin":

    suma = suma + float(nota) 
    cantidad += 1
    nota = input("Ingrese una nota: ")

promedio = suma/cantidad

print(f"El promedio es {round(promedio, 2)}")
