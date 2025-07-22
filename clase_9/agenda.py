import json
import os
def cargar_agenda():
    if os.path.exists('agenda.json'):
        with open('agenda.json', 'r') as archivo:
            return json.load(archivo)
    return {}
def guardar_agenda(agenda):
    with open('agenda.json', 'w') as archivo:
        json.dump(agenda, archivo, indent=4)
def agregar_contacto(agenda):
    nombre = input("Nombre del contacto: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    agenda[nombre] = {'telefono': telefono, 'email': email}
    guardar_agenda(agenda)
    print("Contacto agregado!")
def mostrar_agenda(agenda):
    for nombre, datos in agenda.items():
        print(f"\nNombre: {nombre}")
        print(f"Teléfono: {datos['telefono']}")
        print(f"Email: {datos['email']}")
# Uso
agenda = cargar_agenda()
while True:
    print("\n1. Agregar contacto")
    print("2. Ver agenda")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_contacto(agenda)
    elif opcion == '2':
        mostrar_agenda(agenda)
    elif opcion == '3':
        break
    else:
        print("Opción no válida")
