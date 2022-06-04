import cv2
img = cv2.imread('../files/opencv_low.png')

# Mostrando os valores de BGR, pois estamos acessando o valor dos pixels
print(img[0, 0])
print(img[0, 8])
