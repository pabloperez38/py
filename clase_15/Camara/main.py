import cv2
#pip install opencv-python

import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# =========================================
# Carpeta para capturas
# =========================================
carpeta_capturas = "Capturas"
os.makedirs(carpeta_capturas, exist_ok=True)

# =========================================
# Clasificador de rostros
# =========================================
ruta_haar = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
detector_rostros = cv2.CascadeClassifier(ruta_haar)

# =========================================
# Configuración de correo
# =========================================
SMTP_SERVER = "smtp.midominio.com"      # Cambia a tu servidor
SMTP_PORT = 587
REMITENTE = "tucorreo@midominio.com"
CONTRASEÑA = "TU_CONTRASEÑA_DEL_CORREO"
DESTINATARIO = "destino@correo.com"

# =========================================
# Variables globales
# =========================================
camara = None
capturando = False
frame_anterior_gray = None
sensibilidad = 5000

# =========================================
# Funciones
# =========================================
def enviar_correo(ruta_archivo):
    """Envía un archivo adjunto por correo automáticamente."""
    mensaje = MIMEMultipart()
    mensaje["From"] = REMITENTE
    mensaje["To"] = DESTINATARIO
    mensaje["Subject"] = f"Captura automática {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    cuerpo = "Se ha detectado un movimiento o rostro. Archivo adjunto."
    mensaje.attach(MIMEText(cuerpo, "plain"))

    # Adjuntar el archivo
    if ruta_archivo.endswith(".txt"):
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            adjunto = MIMEText(f.read(), "plain", "utf-8")
            adjunto.add_header('Content-Disposition', 'attachment', filename=os.path.basename(ruta_archivo))
            mensaje.attach(adjunto)
    else:
        with open(ruta_archivo, "rb") as f:
            adjunto = MIMEApplication(f.read(), Name=os.path.basename(ruta_archivo))
            adjunto['Content-Disposition'] = f'attachment; filename="{os.path.basename(ruta_archivo)}"'
            mensaje.attach(adjunto)

    try:
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        servidor.starttls()
        servidor.login(REMITENTE, CONTRASEÑA)
        servidor.send_message(mensaje)
        servidor.quit()
        print(f"Correo enviado: {os.path.basename(ruta_archivo)}")
    except Exception as e:
        print(f"Error enviando correo: {e}")

def iniciar_camara():
    global camara, capturando, frame_anterior_gray
    if capturando:
        messagebox.showinfo("Info", "La cámara ya está corriendo.")
        return

    camara = cv2.VideoCapture(0)
    ret, frame = camara.read()
    if not ret:
        messagebox.showerror("Error", "No se pudo acceder a la cámara.")
        return

    frame_anterior_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_anterior_gray = cv2.GaussianBlur(frame_anterior_gray, (21, 21), 0)
    capturando = True
    mostrar_frame()

def detener_camara():
    global camara, capturando
    capturando = False
    if camara:
        camara.release()
        camara = None
    video_label.config(image="")  # Limpiar la etiqueta
    messagebox.showinfo("Info", "Cámara detenida.")

def mostrar_frame():
    global camara, capturando, frame_anterior_gray, sensibilidad

    if not capturando:
        return

    ret, frame = camara.read()
    if not ret:
        detener_camara()
        return

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # =========================
    # Detección de rostros
    # =========================
    rostros = detector_rostros.detectMultiScale(gris, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in rostros:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Rostro detectado", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        # Guardar captura
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta_archivo = os.path.join(carpeta_capturas, f"rostro_{timestamp}.jpg")
        cv2.imwrite(ruta_archivo, frame)
        enviar_correo(ruta_archivo)

    # =========================
    # Detección de movimiento
    # =========================
    gris_actual = cv2.GaussianBlur(gris, (21, 21), 0)
    diferencia = cv2.absdiff(frame_anterior_gray, gris_actual)
    _, umbral = cv2.threshold(diferencia, 25, 255, cv2.THRESH_BINARY)
    umbral = cv2.dilate(umbral, None, iterations=2)
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    movimiento_detectado = False
    for contorno in contornos:
        if cv2.contourArea(contorno) > sensibilidad:
            (x, y, w, h) = cv2.boundingRect(contorno)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            movimiento_detectado = True
    if movimiento_detectado:
        cv2.putText(frame, "Movimiento detectado", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta_archivo = os.path.join(carpeta_capturas, f"movimiento_{timestamp}.jpg")
        cv2.imwrite(ruta_archivo, frame)
        enviar_correo(ruta_archivo)

    frame_anterior_gray = gris_actual.copy()

    # =========================
    # Convertir a imagen para Tkinter
    # =========================
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    # Llamar a sí mismo cada 10ms
    video_label.after(10, mostrar_frame)

def actualizar_sensibilidad(valor):
    global sensibilidad
    sensibilidad = int(valor)

# =========================================
# Interfaz gráfica
# =========================================
root = tk.Tk()
root.title("Detección y correo automático")
root.geometry("800x600")

tk.Label(root, text="Cámara en tiempo real con OpenCV y envío de correo", font=("Arial", 14)).pack(pady=10)

# Video
video_label = tk.Label(root)
video_label.pack()

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)
tk.Button(frame_botones, text="Iniciar cámara", command=iniciar_camara, width=20).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Detener cámara", command=detener_camara, width=20).grid(row=0, column=1, padx=5)

# Slider para sensibilidad
tk.Label(root, text="Sensibilidad de movimiento:").pack(pady=5)
slider = tk.Scale(root, from_=1000, to=20000, orient=tk.HORIZONTAL, length=400, command=actualizar_sensibilidad)
slider.set(sensibilidad)
slider.pack()

root.mainloop()
