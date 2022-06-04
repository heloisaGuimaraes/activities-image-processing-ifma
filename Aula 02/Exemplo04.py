import cv2
# Especificando a escala em que se deseja ler a imagem
img = cv2.imread('../files/logo-if.jpg', cv2.IMREAD_COLOR)
# img = cv2.imread('logo-if.jpg',cv2.IMREAD_GRAYSCALE)


print(img.shape)  # returns(height, width, channels)
print(img.size)  # returns (height * width * channels)

cv2.imshow('Logo IF', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
