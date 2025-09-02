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

# Palabras clave a buscar en noticias
PALABRAS_CLAVE = ["salario", "colapinto", "milei"]

def crear_carpeta():
    fecha = datetime.now().strftime("%Y-%m-%d")
    global base_path
    base_path = os.path.join("./AutomatizacionHosting", fecha)
    os.makedirs(base_path, exist_ok=True)

def scrapear_noticias():
    url = "https://www.infobae.com"
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, "html.parser")

    titulos = sopa.find_all("h2")
    titulos_extraidos = [titulo.get_text().strip() for titulo in titulos]

    # Filtrar por palabras clave
    titulos_filtrados = [t for t in titulos_extraidos if any(palabra.lower() in t.lower() for palabra in PALABRAS_CLAVE)]

    archivo_titulos = os.path.join(base_path, "titulos_filtrados.txt")
    with open(archivo_titulos, "w", encoding="utf-8") as f:
        if titulos_filtrados:
            for titulo in titulos_filtrados:
                f.write(titulo + "\n")
        else:
            f.write("No se encontraron coincidencias con las palabras clave.\n")

def enviar_correo():
    fecha = datetime.now().strftime("%Y-%m-%d")
    asunto = f"Noticias filtradas {fecha}"

    archivo_titulos = os.path.join(base_path, "titulos_filtrados.txt")
    if os.path.exists(archivo_titulos):
        with open(archivo_titulos, "r", encoding="utf-8") as f:
            titulos = f.read()
    else:
        titulos = "No se extrajeron títulos."

    cuerpo = f"Hola, aquí están las noticias que contienen tus palabras clave:\n\n{titulos}"

    mensaje = MIMEMultipart()
    mensaje["From"] = REMITENTE
    mensaje["To"] = DESTINATARIO
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(cuerpo, "plain"))

    # Adjuntar archivo con resultados
    if os.path.exists(archivo_titulos):
        with open(archivo_titulos, "rb") as f:
            adjunto = MIMEApplication(f.read(), Name="titulos_filtrados.txt")
            adjunto['Content-Disposition'] = 'attachment; filename="titulos_filtrados.txt"'
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
            enviar_correo()
        except Exception as e:
            print(f"Error general: {e}")
        print("Esperando 60 segundos...\n")
        time.sleep(60)
 