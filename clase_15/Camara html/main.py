from ultralytics import YOLO
import cv2

# Cargar modelo preentrenado
model = YOLO("yolov8n.pt")  # modelo liviano

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Inferencia
    results = model(frame)

    # Dibujar resultados
    annotated_frame = results[0].plot()

    cv2.imshow("Detección de objetos", annotated_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
