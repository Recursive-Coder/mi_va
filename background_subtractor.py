import cv2

bg_subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        fbmask = bg_subtractor.apply(frame)
        cnts = cv2.findContours(fbmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        for cnt in cnts:
            if cv2.contourArea(cnt) > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            # texto_estado = "Grabando"
            color = (0, 255, 0)
        cv2.imshow('frame', frame)
        cv2.imshow('BackgroundSubtractorMOG', fbmask)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
