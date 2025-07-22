import tkinter as tk
from tkinter import messagebox

def sumar():
 # Obtener datos de los campos
    num1 = int(entrada_num1.get())
    num2 = int(entrada_num2.get())

    # Validar campos
    if not num1 or not num2:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    # Mostrar los datos en consola
    print(f"\nDatos ingresados:")
    print(f"Num 1: {num1}")
    print(f"Num 2: {num2}")
    print(f"Resultado: {num1 + num2}")

# Mostrar en la interfaz
    etiqueta_resultado.config(text=f"Resultado: {num1 + num2 }")

 # Limpiar campos
    entrada_num1.delete(0, tk.END)
    entrada_num2.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Suma")
ventana.geometry("400x300")
# Crear y posicionar widgets
tk.Label(ventana, text="Num 1:").pack(pady=5)
entrada_num1 = tk.Entry(ventana, width=20,font=('Arial', 24))
entrada_num1.pack(pady=5)
tk.Label(ventana, text="Num 2:").pack(pady=5)
entrada_num2 = tk.Entry(ventana, width=20,font=('Arial', 24))
entrada_num2.pack(pady=5)
boton_enviar = tk.Button(ventana, text="Enviar", command=sumar).pack(pady=10)


etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)
# Ejecutar la aplicación
ventana.mainloop()
