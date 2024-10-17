from datetime import datetime
from my_serial import read_serial_variable
import cv2
import estado
import numpy as np
import threading


# Crea el hilo
leer_serial = threading.Thread(target=read_serial_variable)
leer_serial.daemon = True
leer_serial.start()

cap = cv2.VideoCapture(0)
print('Se abrio la camara')

########

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
fps = 30.0
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
heiht = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f'Ancho:{cap.get(cv2.CAP_PROP_FRAME_WIDTH)} Alto:{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
print(f'{cap.get(cv2.CAP_PROP_FOURCC)}fps: {cap.get(cv2.CAP_PROP_FRAME_COUNT)}')

######

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Dibuja la cruz central
    cv2.line(frame, (int(width / 2), 0), (int(width / 2), heiht), (255, 255, 255), 1)
    cv2.line(frame, (0, int(heiht / 2)), (width, int(heiht / 2)), (255, 255, 255), 1)
    # Muestra numero de cubeta leida, la fecha y hora en el frame
    cv2.putText(frame, f'{estado.cubeta}', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")[:-2]}', (10, 140),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Inicialia mensaje
    color = (0, 255, 0)
    # texto_estado = "No grabando"

    # Especificamos los puntos extremos del area a analizar
    # Area horizontal
    area_pts = np.array([[1, 1], [width - 1, 1], [width - 1, 50], [1, 50]])
    # Area vertical
    # area_pts = np.array([[300, 1], [400, 1], [400, 1079], [300, 1079]])

    # Con ayuda de una imagen auxiliar, determinamos el area
    # sobre la cual actura el detector de movimeitno
    imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1, 255, -1)
    image_area = cv2.bitwise_and(gray, gray, mask=imAux)

    # Obetendremos la imagen binaria donde la region en blanco representa
    # la existencia de movimiento
    fgmask = fgbg.apply(image_area)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, None, iterations=2)

    # Encontramos los contorno presentes de fgmask, para luego basandonos
    # es su area poder determinar si existe movimiento
    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    if cnts:
        if not estado.grabando:
            estado.grabando = True
            fecha = datetime.now()
            salida = (f'{fecha.year}_{str(fecha.month).zfill(2)}_{str(fecha.day).zfill(2)}_{str(fecha.hour).zfill(2)}_'
                      f'{str(fecha.minute).zfill(2)}_{str(fecha.second).zfill(2)}')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(f'capturas/{salida}_{estado.cubeta}.avi', fourcc, fps, (width, heiht))
            out.write(frame)
        else:
            out.write(frame)
            fecha = datetime.now()
    else:
        if estado.grabando:
            diferencia = datetime.now() - fecha
            if diferencia.total_seconds() >= 1.3:
                out.write(frame)
                out.release()
                estado.grabando = False
            else:
                out.write(frame)
    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
        # texto_estado = "Grabando"
        color = (0, 0, 255)

    # Visualizamos el estado de la deteccion en movimiento
    cv2.drawContours(frame, [area_pts], -1, color, 2)
    frame = cv2.resize(frame, (int(frame.shape[1] * 0.5), int(frame.shape[0] * 0.5)), interpolation=cv2.INTER_AREA)
    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
