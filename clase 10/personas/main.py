import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

# Obtener ruta del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "personas.db")

# ---------- FUNCIONES DE BASE DE DATOS ----------
def crear_tabla():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

def agregar_persona(nombre, edad):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO personas (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conexion.commit()
    conexion.close()

def obtener_personas():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM personas")
    datos = cursor.fetchall()
    conexion.close()
    return datos

# ---------- FUNCIONES DE INTERFAZ ----------
def mostrar_formulario_agregar():
    limpiar_frame()
    tk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
    entry_edad = tk.Entry(frame)
    entry_edad.grid(row=1, column=1, padx=5, pady=5)

    def guardar():
        nombre = entry_nombre.get()
        edad = entry_edad.get()
        if nombre and edad.isdigit():
            agregar_persona(nombre, int(edad))
            messagebox.showinfo("Éxito", "Persona guardada")
            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Complete los campos correctamente")

    btn_guardar = tk.Button(frame, text="Guardar", command=guardar)
    btn_guardar.grid(row=2, column=0, columnspan=2, pady=10)

def mostrar_personas():
    limpiar_frame()
    tabla = ttk.Treeview(frame, columns=("ID", "Nombre", "Edad"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Edad", text="Edad")
    tabla.pack(fill="both", expand=True)

    personas = obtener_personas()
    for p in personas:
        tabla.insert("", "end", values=p)

def limpiar_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def salir():
    ventana.quit()

# ---------- INTERFAZ PRINCIPAL ----------
ventana = tk.Tk()
ventana.title("Gestor de Personas")
ventana.geometry("400x300")

# Crear barra de menú
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

menu_personas = tk.Menu(menu_principal, tearoff=0)
menu_personas.add_command(label="Agregar Persona", command=mostrar_formulario_agregar)
menu_personas.add_command(label="Ver Personas", command=mostrar_personas)
menu_personas.add_separator()
menu_personas.add_command(label="Salir", command=salir)

menu_principal.add_cascade(label="Personas", menu=menu_personas)

# Frame principal para cambiar contenido dinámicamente
frame = tk.Frame(ventana)
frame.pack(fill="both", expand=True)

# Crear la tabla si no existe
crear_tabla()

# Mostrar pantalla por defecto
mostrar_personas()

ventana.mainloop()