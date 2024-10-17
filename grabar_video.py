import cv2 as cv


def capturar_video():
    cap = cv.VideoCapture(0)
    print('Abrio camara')
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 30.0, (1280, 720))
    while True:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv.imshow('Captura de video', frame)
            if cv.waitKey(1) & 0XFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()


capturar_video()
