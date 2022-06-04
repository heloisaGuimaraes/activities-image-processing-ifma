import cv2
img = cv2.imread('../files/logo-if.jpg')

# Acessando pedaços específicos da imagem, intervalos, pois está é uma matriz de pixels
roi = img[0:150, 0:150]  # region of interest (ROI)
cv2.imshow('Logo IF', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
