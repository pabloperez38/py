diccionario = {"nombre": "Pablo", "edad": "45", "email": "pablo.eluniversoweb@gmail.com"}
print(len(diccionario)) # Imprime 3
for clave in diccionario:
    print(clave)
print("--------------------")
for valor in diccionario.values():
    print(valor)
print("--------------------")
for clave, valor in diccionario.items():
    print(clave, valor)
