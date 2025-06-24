""" try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"El resultado es: {resultado}")
except ValueError:
   print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.") 


numero = int(input("Ingresa un número: "))
resultado = 10 / numero
print(f"El resultado es: {resultado}")
"""
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error: {e}")
