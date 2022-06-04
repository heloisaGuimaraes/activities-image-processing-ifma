import cv2
import numpy as np
from matplotlib import pyplot as plt

ifma = cv2.imread('ifma-caxias.jpg')
logo = cv2.imread('logo-if.jpg')

# Redimensiona imagem da logo
logo_if = cv2.resize(logo, (200, 100), interpolation=cv2.INTER_AREA)
rows, cols = logo_if.shape[:2]

# Onde Vamos trabalhar
local = ifma[:rows, :cols]

# Mascara
gray = cv2.cvtColor(logo_if, cv2.COLOR_BGR2GRAY)  # cinza
ret, mask_inv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)  # mascara fundo preto

local[mask != 0] = logo_if[mask != 0]
ifma_logo = ifma.copy()
# =====================================
local[mask != 0] = [0,0,0]

telea = cv2.inpaint(local, mask, 3, cv2.INPAINT_TELEA)
ns = cv2.inpaint(local, mask, 3, cv2.INPAINT_NS)

img_TELEA = ifma.copy()
img_TELEA[:rows, :cols] = telea

img_NS = ifma.copy()
img_NS[:rows, :cols] = ns

plt.figure(1, figsize=(8, 8))
plt.subplot(221), plt.imshow(cv2.cvtColor(ifma_logo, cv2.COLOR_BGR2RGB))
plt.title('Imagem')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('Máscara')
plt.subplot(223), plt.imshow(cv2.cvtColor(img_TELEA, cv2.COLOR_BGR2RGB))
plt.title('ifma_TELEA')
plt.subplot(224), plt.imshow(cv2.cvtColor(img_NS, cv2.COLOR_BGR2RGB))
plt.title('ifma_NS')

plt.tight_layout()
plt.show()