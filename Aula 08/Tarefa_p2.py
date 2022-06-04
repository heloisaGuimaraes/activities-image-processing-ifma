# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('cars.png')

mask_bckground = np.zeros(img.shape, np.uint8)  # Máscara para o fundo
cv2.circle(mask_bckground, (950, 285), 280, [255, 255, 255], -1)
ksize = 101
mask_bckground = cv2.GaussianBlur(mask_bckground, (ksize, ksize), 0)
mask_face = cv2.bitwise_not(mask_bckground)  # Máscara para o rosto

img_blur = cv2.GaussianBlur(img, (ksize, ksize), 0)

img_face = cv2.add(img, mask_face)
img_face = cv2.subtract(img_face, mask_face)

img_bckground = cv2.add(img_blur, mask_bckground)
img_bckground = cv2.subtract(img_bckground, mask_bckground)

img_final = cv2.add(img_face, img_bckground)

cv2.imshow('Img', img)
# cv2.imshow('inv', img_face)
# cv2.imshow('inv2', img_bckground)
cv2.imshow('final', img_final)

cv2.waitKey(0)
cv2.destroyAllWindows()
