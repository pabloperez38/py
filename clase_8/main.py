diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
print(diccionario)
#valor = diccionario["clave1"]
#print(valor) # "valor1"

#Para evitar este error, puedes usar el método get(clave,valor_predeterminado) en su lugar, que devuelve el valor predeterminado si la clave no existe.

valor = diccionario.get("clave4", "valor predeterminado")
#print(valor) # "valor predeterminado

#actualizar valor

diccionario["clave1"] = "nuevo valor número 1"
print(diccionario)

#agregar valor
diccionario["clave4"] = "valor4"
print(diccionario)

#eliminar valor
del diccionario["clave2"]
print(diccionario)

valor = diccionario.pop("clave11", "No existe la clave a eliminar")
print(valor)
print(diccionario)