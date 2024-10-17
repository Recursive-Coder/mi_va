import cv2 as cv
import threading
import queue
from leer_cb import leer_cb
from datetime import datetime

########################################################################################################################
# inicio
########################################################################################################################
cola = queue.Queue(maxsize=10)

# crea el hilo
leer_codigo = threading.Thread(target=leer_cb, args=(cola,))
leer_codigo.daemon = True
leer_codigo.start()

print('Voy abrir la camara')
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
fps = 30.0
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
heiht = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(f'Ancho:{cap.get(cv.CAP_PROP_FRAME_WIDTH)} Alto:{cap.get(cv.CAP_PROP_FRAME_HEIGHT)}')
print(f'{cap.get(cv.CAP_PROP_FOURCC)}{cap.get(cv.CAP_PROP_FRAME_COUNT)}')


grabando = False
while True:

    # trato de obetener el numero de cubeta
    try:
        codigo = cola.get_nowait()
        print(f'Cubeta leida:{codigo}')
    except queue.Empty:
        pass
    # fin del intento de leer la cubeta

    # Vision
    ret, frame = cap.read()
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        print('comenzar grabacion')
        fecha = datetime.now()
        salida = (f'{fecha.year}_{str(fecha.month).zfill(2)}_{str(fecha.day).zfill(2)}_{str(fecha.hour).zfill(2)}_'
                  f'{str(fecha.minute).zfill(2)}_{str(fecha.second).zfill(2)}')
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter(f'{salida}_{codigo}.avi', fourcc, fps, (width, heiht))
        out.write(frame)
        grabando = True
    elif key == ord('t'):
        out.write(frame)
        out.release()
        print(f'Terminar grabacion, archivo generado:{salida}_{codigo}.avi')
        grabando = False
    if grabando:
        out.write(frame)
    cv.imshow('frame', frame)

cap.release()
cv.destroyAllWindows()
