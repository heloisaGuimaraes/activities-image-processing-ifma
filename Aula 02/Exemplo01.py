import cv2

# Carrega a image
img = cv2.imread('../files/logo-if.jpg')

b, g, r = cv2.split(img)  # Dividindo a imagem em BGR

# Comandos para exibir a imagem
cv2.imshow('BGR', img)
cv2.imshow('Red', r)
cv2.imshow('Green', g)
cv2.imshow('Blue', b)

# Juntando as três imagens
res = cv2.merge([r, g, b])
cv2.imshow('RGB', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
