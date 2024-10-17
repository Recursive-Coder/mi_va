import cv2

# Nombre del archivo de video
video_file = 'pedido.mp4'

# Crear un objeto VideoCapture para leer el archivo de video
cap = cv2.VideoCapture(video_file)

# Comprobar si el archivo de video se abrió correctamente
if not cap.isOpened():
    print("Error al abrir el archivo de video")
    exit()

# Definir el número del frame que queremos ver
frame_number = 60

# Establecer la posición del frame a leer
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# Leer el frame
ret, frame = cap.read()

# Comprobar si el frame fue leído correctamente
if not ret:
    print("No se pudo leer el frame")
else:
    # Mostrar el frame
    cv2.imshow(f'Frame {frame_number}', frame)

    # Esperar hasta que se presione una tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Liberar el objeto de captura
cap.release()
