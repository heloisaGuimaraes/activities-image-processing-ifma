import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('atividade_aula11.png', 0)
img = cv2.resize(img, (200, 200), interpolation=cv2.INTER_AREA)

# Gradient
n = 3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (n, n))
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Question 1
l = 3
c = 7
kernel = np.zeros((l, c), np.uint8)
line = [1, 1, 1, 0, 0, 0, 0]
for i in range(l):
    kernel[i] = line
erosion = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations=5)

kernel = kernel.T
erosion = cv2.morphologyEx(erosion, cv2.MORPH_ERODE, kernel, iterations=5)

img_moved = cv2.add(gradient, erosion)


# Question 2
l = 11
c = 7
kernel = np.ones((l, c), np.uint8)
erosion = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations=7)

l = 25
c = 9
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (c, l))
dilation = cv2.morphologyEx(erosion, cv2.MORPH_DILATE, kernel, iterations=2)
img_sliced = cv2.add(gradient, dilation)

# Question 3
l = 21
c = 21
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (c, l))
dilation = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=2)

l = 11
c = 11
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (c, l))
erosion = cv2.morphologyEx(dilation, cv2.MORPH_ERODE, kernel, iterations=3)

erosion = cv2.morphologyEx(erosion, cv2.MORPH_DILATE, kernel, iterations=1)
img_rounded = cv2.subtract(erosion, gradient)

plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Image')
plt.subplot(222), plt.imshow(cv2.cvtColor(img_moved, cv2.COLOR_BGR2RGB))
plt.title('Question 1')
plt.subplot(223), plt.imshow(cv2.cvtColor(img_sliced, cv2.COLOR_BGR2RGB))
plt.title('Question 2')
plt.subplot(224), plt.imshow(cv2.cvtColor(img_rounded, cv2.COLOR_BGR2RGB))
plt.title('Question 3')

plt.tight_layout()
plt.show()