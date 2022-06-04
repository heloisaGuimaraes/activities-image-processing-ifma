import cv2
import numpy as np

img = cv2.imread('noise.jpg')

ksize = 5
output = cv2.medianBlur(img, ksize)

cv2.imshow('Original', img)
cv2.imshow('Output', output)

cv2.waitKey(0)
cv2.destroyAllWindows()


