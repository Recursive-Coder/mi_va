import pytesseract
from PIL import Image
import cv2
import numpy as np
import re


img = cv2.imread('ejemplos/imagencortada.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_white = np.array([0, 0, 60])
upper_white = np.array([180, 50, 200])

mask = cv2.inRange(hsv,lower_white, upper_white)
cv2.imshow('mask',mask)

contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cts in contours:
    if cv2.contourArea(cts) > 300:
        cv2.drawContours(img, contours, -1, (255, 0, 0), 2)

cv2.imshow('gris',hsv)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
texto = pytesseract.image_to_string(img)
lista = re.split(r'\s+', texto)
print(f'texto leido {lista}')
cv2.imshow('a analizar ', img)
cv2.waitKey(0)
