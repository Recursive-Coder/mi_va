import cv2

url = 'https://admin:alarmas118@192.168.2.110:443/640x480'
cap = cv2.VideoCapture('base.mp4')

winName = 'IP_CAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

while (1):

    cap.open(url)
    ret, frame = cap.read()

    if ret:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(winName, frame)
        tecla = cv2.waitKey(1) & 0xFF

    if TypeError == 27:
        break

cv2.destroyAllWindows()
