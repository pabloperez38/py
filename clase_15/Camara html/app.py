from flask import Flask, render_template, Response, request
import cv2
import os
from datetime import datetime
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

app = Flask(__name__)

# Carpeta para capturas
carpeta_capturas = "Capturas"
os.makedirs(carpeta_capturas, exist_ok=True)

# Clasificador de rostros
ruta_haar = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
detector_rostros = cv2.CascadeClassifier(ruta_haar)

# Configuración de correo
SMTP_SERVER = "smtp.sistemadeventas.com.ar"  # Cambia por tu servidor SMTP
SMTP_PORT = 587                      # Puerto TLS
REMITENTE = "python@sistemadeventas.com.ar"  # Tu correo de hosting
CONTRASEÑA = "FZwMCBQFd4HFeRrBqeU8"  # Contraseña del correo
DESTINATARIO = "pablo.eluniversoweb@gmail.com"     # Correo que recibirá los resultados

# Variables globales
camara = cv2.VideoCapture(0)
frame_anterior_gray = None
sensibilidad = 5000  # Umbral de detección de movimiento

# Función para enviar correo
def enviar_correo(ruta_archivo):
    mensaje = MIMEMultipart()
    mensaje["From"] = REMITENTE
    mensaje["To"] = DESTINATARIO
    mensaje["Subject"] = f"Evento especial {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    mensaje.attach(MIMEText("Se ha detectado un movimiento especial. Archivo adjunto.", "plain"))

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

# Generador de frames para streaming
def generar_frames():
    global frame_anterior_gray, sensibilidad

    while True:
        ret, frame = camara.read()
        if not ret:
            continue

        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gris_actual = cv2.GaussianBlur(gris, (21, 21), 0)

        if frame_anterior_gray is None:
            frame_anterior_gray = gris_actual.copy()
            continue

        # =========================
        # Detección de movimiento
        # =========================
        diferencia = cv2.absdiff(frame_anterior_gray, gris_actual)
        _, umbral = cv2.threshold(diferencia, 25, 255, cv2.THRESH_BINARY)
        umbral = cv2.dilate(umbral, None, iterations=2)
        contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        movimiento_especial_detectado = False

        for contorno in contornos:
            area = cv2.contourArea(contorno)
            if area > sensibilidad:
                (x, y, w, h) = cv2.boundingRect(contorno)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
                # Movimiento especial: derecha del frame y area grande
                if x > frame.shape[1] // 2 and area > 8000:
                    movimiento_especial_detectado = True

        # =========================
        # Detección de rostros
        # =========================
        rostros = detector_rostros.detectMultiScale(gris, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in rostros:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Rostro detectado", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
            # Combinar con movimiento especial
            if movimiento_especial_detectado:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                ruta_archivo = os.path.join(carpeta_capturas, f"evento_especial_{timestamp}.jpg")
                cv2.imwrite(ruta_archivo, frame)
                threading.Thread(target=enviar_correo, args=(ruta_archivo,)).start()

        frame_anterior_gray = gris_actual.copy()

        # Codificar frame para streaming
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Rutas Flask
@app.route("/")
def index():
    return render_template("index.html", sensibilidad=sensibilidad)

@app.route("/video_feed")
def video_feed():
    return Response(generar_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/set_sensibilidad", methods=["POST"])
def set_sensibilidad():
    global sensibilidad
    valor = request.form.get("valor")
    if valor:
        sensibilidad = int(valor)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
