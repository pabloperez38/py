import tkinter as tk
def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacion = operacion_var.get()

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2

        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Entrada inválida")
    except ZeroDivisionError:
        etiqueta_resultado.config(text="Error: División por cero")
# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora Simple")
# Widgets
entrada_num1 = tk.Entry(ventana, width=10)
entrada_num1.grid(row=0, column=0, padx=5, pady=5)
operacion_var = tk.StringVar(value="+")
tk.OptionMenu(ventana, operacion_var, "+", "-", "*", "/").grid(row=0, column=1,padx=5, pady=5)
entrada_num2 = tk.Entry(ventana, width=10)
entrada_num2.grid(row=0, column=2, padx=5, pady=5)
tk.Button(ventana, text="=", command=calcular).grid(row=0, column=3, padx=5,pady=5)
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=1, columnspan=4, pady=10)
# Ejecutar aplicación
ventana.mainloop()