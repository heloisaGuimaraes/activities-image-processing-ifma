import cv2
import numpy as np

logo = cv2.imread('logo-if.jpg')
ifma = cv2.imread('ifma-caxias.jpg')

# Redimensiona imagem
logo_if = cv2.resize(logo, (200, 100), interpolation=cv2.INTER_AREA)
rows, cols = logo_if.shape[:2]

# Onde Vamos trabalhar
local = ifma[:rows, :cols]

# Mascara
gray = cv2.cvtColor(logo_if, cv2.COLOR_BGR2GRAY)  # cinza
ret, mask_inv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)  # mascara fundo preto

local[mask != 0] = logo_if[mask != 0]
ifma[:rows, :cols] = local
cv2.imshow('IFMA', ifma)
cv2.imwrite('mask.jpg', mask)


cv2.waitKey(0)
cv2.destroyAllWindows()
