import cv2
import numpy as np

print('Voy abrir la camara.')
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('http://172.16.11.251:8081')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
print(f'Ancho:{cap.get(cv2.CAP_PROP_FRAME_WIDTH)} Alto:{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
print(f'{cap.get(cv2.CAP_PROP_FOURCC)} fps: {cap.get(cv2.CAP_PROP_FPS)}')
# print('Se abrio la camara')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Dibujamos un rectangulo en el frame para señalar el estado
    # del area en analisis (novimiento detectado o no detectado)
    # cv2.rectangle(frame, (0, 0), (frame.shape[1], 790), (0, 0, 0), -1)
    cv2.rectangle(frame, (0, 950), (230, 1000), (0, 0, 0), -1)
    color = (0, 255, 0)
    texto_estado = "No grabando"

    # Especificamos los puntos extremos del area a analizar
    # area_pts = np.array([[240, 320], [480, 320], [620, frame.shape[0]], [50, frame.shape[0]]])
    # area_pts = np.array([[20, 5], [1900, 5], [1900, 70], [20, 70]])
    area_pts = np.array([[550, 1], [600, 1], [600, 1079], [550, 1079]])

    # Con ayuda de una imagen auxiliar, determinamos el area
    # sobre la cual actura el detector de movimeitno
    imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1, (255), -1)
    image_area = cv2.bitwise_and(gray, gray, mask=imAux)
    cv2.imshow('image_area', image_area)

    # Obetendremos la imagen binaria donde la region en blanco representa
    # la existencia de movimiento
    fgmask = fgbg.apply(image_area)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, None, iterations=2)

    # Encontramos los contorno presentes de fgmask, para luego basandonos
    # es su area poder determinar si existe movimiento
    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    print(f'cnts: {cnts}')
    for cnt in cnts:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        texto_estado = "Grabando"
        color = (0, 0, 255)

    # Visualizamos el estado de la deteccion en movimiento
    cv2.drawContours(frame, [area_pts], -1, color, 2)
    cv2.putText(frame, texto_estado, (10, 985), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
