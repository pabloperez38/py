def calcular_promedio(cantidad):
    """Calcula el promedio de una cantidad dada de números."""
    suma = 0
    for i in range(cantidad):
        numero = float(input(f"Ingresa el número {i+1}: "))
        suma += numero
    return suma / cantidad

# Prueba la función
n = int(input("¿Cuántos números vas a ingresar? "))
print(f"El promedio es: {calcular_promedio(n)}")