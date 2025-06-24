diccionario = {} # Diccionario vacío
while True:
    clave = input("Ingresa una clave (o 'fin' para terminar): ")
    if clave == 'fin':
        break # Salir del bucle si se ingresa 'fin'
    valor = input("Ingrese el valor para la clave '{}': ".format(clave))
    diccionario[clave] = valor
print(diccionario)