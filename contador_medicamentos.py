import cv2 as cv


class Camara:
    def __init__(self):
        self.captura = cv.VideoCapture(0, 0)
        self.captura.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
        # self.captura.set(cv.CAP_PROP_SHARPNESS, 2.0)
        # self.captura.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
        # fps = 30.0
        # self.captura.set(cv.CAP_PROP_FPS, 120.0)
        print('Informacion de la captura de video')
        print(f'Width: {self.captura.get(cv.CAP_PROP_FRAME_WIDTH)} '
              f'Height: {self.captura.get(cv.CAP_PROP_FRAME_HEIGHT)}')
        print(f'FOURCC: {self.captura.get(cv.CAP_PROP_FOURCC)} FPS: {self.captura.get(cv.CAP_PROP_FPS)}')
        print(f'Nitidez de la imagen {self.captura.get(cv.CAP_PROP_SHARPNESS)}')

    def capturar(self):
        while True:
            ret, frame = self.captura.read()
            if ret:
                cv.imshow('frame', frame)
            else:
                print(' error')
            key = cv.waitKey(20) & 0xFF  # valor de referencia 20
            if key == ord('q'):
                break
        self.captura.release()
        cv.destroyAllWindows()


cam = Camara()
cam.capturar()
