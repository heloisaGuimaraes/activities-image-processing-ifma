import cv2
import numpy as np
from matplotlib import pyplot as plt


ifma = cv2.imread('if.jpg')
mask = cv2.imread('mask.jpg', 0)

# ksize = 4
# mask = cv2.dilate(mask, cv2.getStructuringElement(
#     cv2.MORPH_ELLIPSE, (ksize, ksize)))

rows, cols = mask.shape[0:2]
local = ifma[:rows, :cols]

ret, mask2 = cv2.threshold(mask, 125, 255, cv2.THRESH_BINARY)

local[mask2 != 0] = [0, 0, 0]


telea = cv2.inpaint(local, mask2, 3, cv2.INPAINT_TELEA)
ns = cv2.inpaint(local, mask2, 3, cv2.INPAINT_NS)


img_TELEA = ifma.copy()
img_TELEA[:rows, :cols] = telea

img_NS = ifma.copy()
img_NS[:rows, :cols] = ns

plt.figure(1, figsize=(10, 10))
plt.subplot(221), plt.imshow(cv2.cvtColor(local, cv2.COLOR_BGR2RGB))
plt.title('Imagem')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('Máscara')
# plt.subplot(223), plt.imshow(cv2.cvtColor(telea, cv2.COLOR_BGR2RGB))
# plt.title('local_TELEA')
# plt.subplot(224), plt.imshow(cv2.cvtColor(ns, cv2.COLOR_BGR2RGB))
# plt.subplot(224), plt.imshow(m, 'gray')
# plt.title('local_NS')
plt.subplot(223), plt.imshow(cv2.cvtColor(img_TELEA, cv2.COLOR_BGR2RGB))
plt.title('ifma_TELEA')
plt.subplot(224), plt.imshow(cv2.cvtColor(img_NS, cv2.COLOR_BGR2RGB))
plt.title('ifma_NS')

plt.tight_layout()
plt.show()
