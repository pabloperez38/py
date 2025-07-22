import tkinter as tk

def saludo1():
    print("¡Botón presionado 1!")
def saludo2():
    print("¡Botón presionado 2!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Título de la ventana")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="Etiqueta", background='blue')
etiqueta.pack()

boton = tk.Button(ventana, text="Presióname", command=saludo1)
boton.pack()
boton2 = tk.Button(ventana, text="Presióname 2", command=saludo2)
boton2.pack()

nombre = tk.Entry(ventana)
nombre.pack()

ventana.mainloop()