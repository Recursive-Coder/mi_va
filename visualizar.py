import cv2 as cv

# captura = cv.VideoCapture('http://192.168.2.110/prueba.jpg')
# captura = cv.VideoCapture('rtsp://admin:alarmas118@172.16.11.97/video')
captura = cv.VideoCapture('2024_07_17_13_41_21_526323.avi')
while True:
    ret, frame = captura.read()
    if ret:
        cv.imshow('frame', frame)
    else:
        print(' error')
    key = cv.waitKey(120) & 0xFF # valor de referencia 20
    if key == ord('q'):
        break
captura.release()
cv.destroyAllWindows()
