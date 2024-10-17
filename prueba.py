import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Error: No se pudo abrir la camara.')

while True:
    ret, frame = cap.read()

    if not ret:
        cv2.imshow('Video', frame)
        key = cv2.waitKey(120) & 0xFF  # valor de referencia 20
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
