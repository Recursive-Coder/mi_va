import cv2

# Crear un objeto de captura de video
cap = cv2.VideoCapture(0)

# Lista de propiedades a verificar
propiedades = [
    ("CAP_PROP_FRAME_WIDTH", cv2.CAP_PROP_FRAME_WIDTH),
    ("CAP_PROP_FRAME_HEIGHT", cv2.CAP_PROP_FRAME_HEIGHT),
    ("CAP_PROP_FPS", cv2.CAP_PROP_FPS),
    ("CAP_PROP_FOURCC", cv2.CAP_PROP_FOURCC),
    ("CAP_PROP_FRAME_COUNT", cv2.CAP_PROP_FRAME_COUNT),
    ("CAP_PROP_BRIGHTNESS", cv2.CAP_PROP_BRIGHTNESS),
    ("CAP_PROP_CONTRAST", cv2.CAP_PROP_CONTRAST),
    ("CAP_PROP_SATURATION", cv2.CAP_PROP_SATURATION),
    ("CAP_PROP_HUE", cv2.CAP_PROP_HUE),
    ("CAP_PROP_GAIN", cv2.CAP_PROP_GAIN),
    ("CAP_PROP_EXPOSURE", cv2.CAP_PROP_EXPOSURE),
    ("CAP_PROP_CONVERT_RGB", cv2.CAP_PROP_CONVERT_RGB),
    ("CAP_PROP_RECTIFICATION", cv2.CAP_PROP_RECTIFICATION),
    ("CAP_PROP_BUFFERSIZE", cv2.CAP_PROP_BUFFERSIZE),
    ("CAP_PROP_AUTOFOCUS", cv2.CAP_PROP_AUTOFOCUS),
    ("CAP_PROP_ZOOM", cv2.CAP_PROP_ZOOM),
    ("CAP_PROP_FOCUS", cv2.CAP_PROP_FOCUS),
    ("CAP_PROP_ISO_SPEED", cv2.CAP_PROP_ISO_SPEED),
    ("CAP_PROP_BACKLIGHT", cv2.CAP_PROP_BACKLIGHT),
    ("CAP_PROP_SHARPNESS", cv2.CAP_PROP_SHARPNESS)
]

# Verificar las propiedades
for (nombre, codigo) in propiedades:
    valor = cap.get(codigo)
    if valor == -1:
        print(f"{nombre} no está soportada.")
    else:
        print(f"{nombre}: {valor}")

# Liberar el objeto de captura de video

