import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('morphological_car.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

s_krnl = 10
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (s_krnl, s_krnl))

w_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
b_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)



plt.figure(1, figsize=(8, 8))
plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagem')
plt.subplot(222), plt.imshow(cv2.cvtColor(w_hat, cv2.COLOR_BGR2RGB))
plt.title('White hat')
plt.subplot(223), plt.imshow(cv2.cvtColor(b_hat, cv2.COLOR_BGR2RGB))
plt.title('Black hat')
# plt.subplot(224), plt.imshow(cv2.cvtColor(test, cv2.COLOR_BGR2RGB))
# plt.title('test')

plt.tight_layout()
plt.show()
