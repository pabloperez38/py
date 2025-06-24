# Diccionario inicial
mi_diccionario = {}

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar elemento")
    print("2. Actualizar elemento")
    print("3. Eliminar elemento")
    print("4. Mostrar diccionario")
    print("5. Salir")

def agregar_elemento():
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    mi_diccionario[clave] = valor
    print(f"Elemento '{clave}: {valor}' agregado correctamente.")

def actualizar_elemento():
    clave = input("Ingrese la clave del elemento a actualizar: ")
    if clave in mi_diccionario:
        nuevo_valor = input(f"Ingrese el nuevo valor para '{clave}': ")
        mi_diccionario[clave] = nuevo_valor
        print(f"Elemento '{clave}' actualizado correctamente.")
    else:
        print(f"Error: La clave '{clave}' no existe en el diccionario.")

def eliminar_elemento():
    clave = input("Ingrese la clave del elemento a eliminar: ")
    if clave in mi_diccionario:
        del mi_diccionario[clave]
        print(f"Elemento '{clave}' eliminado correctamente.")
    else:
        print(f"Error: La clave '{clave}' no existe en el diccionario.")

def mostrar_diccionario():
    if not mi_diccionario:
        print("El diccionario está vacío.")
    else:
        print("\nContenido del diccionario:")
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")

# Programa principal
def main():
    print("Bienvenido al Gestor de Diccionarios")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_elemento()
        elif opcion == "2":
            actualizar_elemento()
        elif opcion == "3":
            eliminar_elemento()
        elif opcion == "4":
            mostrar_diccionario()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()