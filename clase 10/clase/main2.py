import tkinter as tk
from tkinter import messagebox

def enviar_datos():
 # Obtener datos de los campos
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    # Validar campos
    if not nombre or not edad:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    # Mostrar los datos en consola
    print(f"\nDatos ingresados:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")

# Mostrar en la interfaz
    etiqueta_resultado.config(text=f"Nombre: {nombre}, Edad: {edad}")

 # Limpiar campos
    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Formulario de datos")
ventana.geometry("400x300")
# Crear y posicionar widgets
tk.Label(ventana, text="Nombre:").pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=20,font=('Arial', 24))
entrada_nombre.pack(pady=5)
tk.Label(ventana, text="Edad:").pack(pady=5)
entrada_edad = tk.Entry(ventana, width=40)
entrada_edad.pack(pady=5)
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos).pack(pady=10)


etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)
# Ejecutar la aplicación
ventana.mainloop()
