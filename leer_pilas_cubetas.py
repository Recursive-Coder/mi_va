import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
etiqueta = []
img = cv2.imread('prueba.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imshow('GaussianBlur', gray)
# canny = cv2.Canny(img, 150, 200)
canny = cv2.Canny(img, 170, 210)
# canny = cv2.dilate(canny, None, iterations=1)
cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cnts:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    epsilon = 0.03 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    # print(f'epilon {epsilon},approx{approx},len(approx) {len(approx)}')
    if len(approx) == 4 and (800 < area < 5400):
        # intenta leer el codigo de barra
        # etiqueta = gray[y:y + h, x:x + w]
        inicio = int((w * 33.5) / 100)
        print(f'inicio {inicio}')
        etiqueta = gray[y:y + h, x+inicio:x + w]
        text = pytesseract.image_to_string(etiqueta, config='--psm 6')
        print(f'Area: {area} x: {x} y: {y} Ancho: {w} Alto: {h} Aspect Ratio: {w / h}')
        print(f'Etiqueta: {text}')
        # funcion que enderesa la imagen para mejorar la lectura
        # obtener el ancho y el alto de la nueva imagen
        cv2.drawContours(img, [c], 0, (0, 255, 0), 2)
        # debe eliminar el porcentaje que estaria el codigo de barra
        cv2.imshow('etiqueta', etiqueta)
        cv2.waitKey(0)
        cv2.destroyWindow('etiqueta')


cv2.imshow('canny', canny)
cv2.imshow('img', img)
cv2.waitKey(0)
