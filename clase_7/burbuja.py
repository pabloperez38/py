nombres = ["Carmen","Ana", "Pedro", "Carlos", "Carlitos", "Pablo", "Diego"]
contador = 0
n = len(nombres)
# Recorrer toda la lista de nombres
for i in range(n):
    # Últimos elementos ya están ordenados, así que no es necesario verificarlos
    for j in range(0, n-i-1):
        contador += 1
        # Comparar los elementos adyacentes
        if nombres[j] > nombres[j+1]:
            print(f"Vuelta: {contador} ")
            print("Verdad:")
            print(nombres[j])
            print(nombres[j+1])
            print("--------")
            # Si están en el orden incorrecto, intercambiarlos
            nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
            print(nombres[j])
            print(nombres[j+1])
            print("--------")
        print(f"Vuelta: {contador} ")
        print("Falso:")
        print(nombres[j])
        print(nombres[j+1])
        print("--------")
# Mostrar la lista ordenada
print(nombres)
print(contador)
