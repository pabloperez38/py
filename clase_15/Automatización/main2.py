import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time

# Configuración SMTP
SMTP_SERVER = "smtp.sistemadeventas.com.ar"
SMTP_PORT = 587
REMITENTE = "python@sistemadeventas.com.ar"
CONTRASEÑA = "FZwMCBQFd4HFeRrBqeU8"
DESTINATARIO = "pablo.eluniversoweb@gmail.com"

def crear_carpeta():
    fecha = datetime.now().strftime("%Y-%m-%d")
    global base_path
    base_path = os.path.join("./AutomatizacionHosting", fecha)
    os.makedirs(base_path, exist_ok=True)

def renombrar_archivos():
    for archivo in os.listdir(base_path):
        ruta_archivo = os.path.join(base_path, archivo)
        if os.path.isfile(ruta_archivo):
            nuevo_nombre = os.path.join(base_path, f"{archivo}")
            os.rename(ruta_archivo, nuevo_nombre)

def scrapear_noticias():
    url = "https://www.bbc.com/news"
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, "html.parser")

    titulos = sopa.find_all("h2")
    titulos_extraidos = [titulo.get_text().strip() for titulo in titulos[:10]]

    archivo_titulos = os.path.join(base_path, "titulos_noticias.txt")
    with open(archivo_titulos, "w", encoding="utf-8") as f:
        for titulo in titulos_extraidos:
            f.write(titulo + "\n")

    imagenes = sopa.find_all("img")[:5]
    for i, img in enumerate(imagenes, 1):
        src = img.get("src")
        if src and src.startswith("http"):
            img_respuesta = requests.get(src)
            nombre_img = os.path.join(base_path, f"imagen_{i}.jpg")
            with open(nombre_img, "wb") as file:
                file.write(img_respuesta.content)

def enviar_correo():
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

    for archivo in os.listdir(base_path):
        ruta_archivo = os.path.join(base_path, archivo)
        if os.path.isfile(ruta_archivo):
            if archivo.endswith(".txt"):
                with open(ruta_archivo, "r", encoding="utf-8") as f:
                    contenido = f.read()
                    adjunto = MIMEText(contenido, "plain", "utf-8")
                    adjunto.add_header('Content-Disposition', 'attachment', filename=archivo)
                    mensaje.attach(adjunto)
            else:
                with open(ruta_archivo, "rb") as f:
                    adjunto = MIMEApplication(f.read(), Name=archivo)
                    adjunto['Content-Disposition'] = f'attachment; filename="{archivo}"'
                    mensaje.attach(adjunto)

    try:
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        servidor.starttls()
        servidor.login(REMITENTE, CONTRASEÑA)
        servidor.send_message(mensaje)
        servidor.quit()
        print("Correo enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Bucle de ejecución cada 1 minuto
if __name__ == "__main__":
    while True:
        try:
            print(f"[{datetime.now()}] Ejecutando tareas...")
            crear_carpeta()
            scrapear_noticias()
            renombrar_archivos()
            enviar_correo()
        except Exception as e:
            print(f"Error general: {e}")
        print("Esperando 60 segundos...\n")
        time.sleep(60)
