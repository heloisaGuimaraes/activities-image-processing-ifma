from cmath import pi
import cv2
import numpy as np

img = cv2.imread('../files/logo-if.jpg')
weight, height = img.shape[0:2]


limite = [255, 255, 255]


def aplicar_brilho(img):
    br = np.array([brilho, brilho, brilho])
    output = np.zeros(img.shape, np.uint8)
    for i in range(0, weight):
        for j in range(0, height):
            output[i][j] = np.minimum(img[i, j]+br, limite)
    return output


def aplicar_contraste(img):
    output = np.zeros(img.shape, np.uint8)
    for i in range(0, weight):
        for j in range(0, height):
            output[i][j] = np.minimum(img[i, j]*contraste, limite)
    return output


def aplicar_negativo(img):
    output = np.zeros(img.shape, np.uint8)
    for i in range(0, weight):
        for j in range(0, height):
            output[i][j] = 255-(img[i][j])
    return output


# ====================
cv2.namedWindow('IFMA')
brilho = 0
contraste = 1
isNegativo = False

cv2.imshow('IFMA', img)
while(1):

    k = cv2.waitKey(20)
    if k == 97:  # a
        brilho = min(brilho+5, 255)
        cv2.imshow('IFMA', aplicar_brilho(img))
        print('brilho em:', brilho)

    elif k == 122:  # z
        brilho = max(brilho-5, -255)
        cv2.imshow('IFMA', aplicar_brilho(img))
        print('brilho em:', brilho)

    if k == 115:  # s
        contraste = min(contraste+1, 255)
        cv2.imshow('IFMA', aplicar_contraste(img))
        print('contraste em:', contraste)

    elif k == 120:  # x
        contraste = max(contraste-1, 0)
        cv2.imshow('IFMA', aplicar_contraste(img))
        print('contraste em:', contraste)

    elif k == 110:  # n
        isNegativo = not(isNegativo)
        if (isNegativo == True):
            cv2.imshow('IFMA', aplicar_negativo(img))
            print('Negativo on')
        else:
            cv2.imshow('IFMA', img)
            print('Negativo off')

    elif k == 27:  # esc
        break

cv2.destroyAllWindows()
