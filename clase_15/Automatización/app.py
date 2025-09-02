
#FZwMCBQFd4HFeRrBqeU8

import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import messagebox

# =========================================
# Configuración de correo (SMTP directamente en el código)
# =========================================
SMTP_SERVER = "smtp.sistemadeventas.com.ar"  # Cambia por tu servidor SMTP
SMTP_PORT = 587                      # Puerto TLS
REMITENTE = "python@sistemadeventas.com.ar"  # Tu correo de hosting
CONTRASEÑA = "FZwMCBQFd4HFeRrBqeU8"  # Contraseña del correo
DESTINATARIO = "pablo.eluniversoweb@gmail.com"     # Correo que recibirá los resultados

# =========================================
# Funciones de automatización
# =========================================

def crear_carpeta():
    fecha = datetime.now().strftime("%Y-%m-%d")
    global base_path
    base_path = os.path.join("./AutomatizacionHosting", fecha)
    os.makedirs(base_path, exist_ok=True)
    messagebox.showinfo("Info", f"Carpeta creada: {base_path}")

def renombrar_archivos():
    if not base_path:
        messagebox.showwarning("Advertencia", "Primero crea la carpeta.")
        return
    for archivo in os.listdir(base_path):
        ruta_archivo = os.path.join(base_path, archivo)
        if os.path.isfile(ruta_archivo):
            nuevo_nombre = os.path.join(base_path, f"nuevo_{archivo}")
            os.rename(ruta_archivo, nuevo_nombre)
    messagebox.showinfo("Info", "Archivos renombrados correctamente.")

def scrapear_noticias():
    if not base_path:
        messagebox.showwarning("Advertencia", "Primero crea la carpeta.")
        return
    url = "https://infobae.com"
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, "html.parser")

    titulos = sopa.find_all("h2")
    titulos_extraidos = [titulo.get_text().strip() for titulo in titulos[:10]]

    archivo_titulos = os.path.join(base_path, "titulos_noticias.txt")
    with open(archivo_titulos, "w", encoding="utf-8") as f:
        for titulo in titulos_extraidos:
            f.write(titulo + "\n")

    # Descargar primeras 5 imágenes
    imagenes = sopa.find_all("img")[:5]
    for i, img in enumerate(imagenes, 1):
        src = img.get("src")
        if src and src.startswith("http"):
            img_respuesta = requests.get(src)
            nombre_img = os.path.join(base_path, f"imagen_{i}.jpg")
            with open(nombre_img, "wb") as file:
                file.write(img_respuesta.content)

    messagebox.showinfo("Info", "Scraping completado y archivos guardados.")

def enviar_correo():
    if not base_path:
        messagebox.showwarning("Advertencia", "Primero crea la carpeta.")
        return

    fecha = datetime.now().strftime("%Y-%m-%d")
    asunto = f"Noticias y archivos automáticos {fecha}"

    archivo_titulos = os.path.join(base_path, "titulos_noticias.txt")
    if os.path.exists(archivo_titulos):
        with open(archivo_titulos, "r", encoding="utf-8") as f:
            titulos = f.read()
    else:
        titulos = "No se extrajeron títulos."

    cuerpo = f"Hola, se han extraído automáticamente las últimas noticias y archivos.\n\nTitulos:\n{titulos}"

    mensaje = MIMEMultipart()
    mensaje["From"] = REMITENTE
    mensaje["To"] = DESTINATARIO
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(cuerpo, "plain"))

    # Adjuntar todos los archivos de la carpeta
    for archivo in os.listdir(base_path):
        ruta_archivo = os.path.join(base_path, archivo)
        if os.path.isfile(ruta_archivo):
            if archivo.endswith(".txt"):  # Archivos de texto
                with open(ruta_archivo, "r", encoding="utf-8") as f:
                    contenido = f.read()
                    adjunto = MIMEText(contenido, "plain", "utf-8")
                    adjunto.add_header('Content-Disposition', 'attachment', filename=archivo)
                    mensaje.attach(adjunto)
            else:  # Archivos binarios (imágenes)
                with open(ruta_archivo, "rb") as f:
                    adjunto = MIMEApplication(f.read(), Name=archivo)
                    adjunto['Content-Disposition'] = f'attachment; filename="{archivo}"'
                    mensaje.attach(adjunto)

    # Enviar correo
    try:
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        servidor.starttls()
        servidor.login(REMITENTE, CONTRASEÑA)
        servidor.send_message(mensaje)
        servidor.quit()
        messagebox.showinfo("Info", "Correo enviado correctamente con adjuntos")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo: {e}")

# =========================================
# Interfaz gráfica con Tkinter
# =========================================
base_path = ""

root = tk.Tk()
root.title("Automatización Python - Hosting SMTP")
root.geometry("500x400")

tk.Label(root, text="Automatización de tareas en Python", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Crear carpeta", width=30, command=crear_carpeta).pack(pady=5)
tk.Button(root, text="Renombrar archivos", width=30, command=renombrar_archivos).pack(pady=5)
tk.Button(root, text="Scraping de noticias", width=30, command=scrapear_noticias).pack(pady=5)
tk.Button(root, text="Enviar correo automáticamente", width=30, command=enviar_correo).pack(pady=5)

root.mainloop()