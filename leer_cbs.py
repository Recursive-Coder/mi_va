import cv2
# importar la biblioteca para la lectura de codigos de barras

imagen = cv2.imread('codigos.jpeg')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# crear objeto
# aplica metodo de busque de codgigos de barras

# a los resultados devuelve la informacion de cada codigo de barra conseguido

cv2.imshow('fram', imagen)
cv2.imshow('blanco y negro', gris)
cv2.waitKey()
cv2.destroyAllWindows()
