# Faça a redução da resolução de uma imagem tomando
# por base a eliminação dos pixels da vizinhança-8.

import cv2
import numpy as np

# Distancia entre um pixel e outro
dist = 3

# Lendo a imagem e coletando os dados de largura e altura
img = cv2.imread('../files/logo-if.jpg')
weight, height = img.shape[0:2]

# Definindo o tamanho da nova imagem reduzida
little_weight = int(weight/3)
little_height = int(height/3)


# Função para reduzir a imagem
def reduce(image):
    output = np.zeros((little_weight, little_height, 3), np.uint8)
    for i in range(0, little_weight):
        l = int((i*3))  # Posição X da imagem menor
        for j in range(0, little_height):
            c = int((j*3))  # Posição Y da imagem menor
            # Inserindo o Pixel da nova imagem
            output[i][j] = np.mean(np.mean((image[l:l+dist, c:c+dist]), axis=0), axis=0)
    return output


# Mostrando os resultados
cv2.imshow('First Image', img)
reduced = reduce(img)
cv2.imshow('New Image', reduced)

cv2.waitKey(0)
cv2.destroyAllWindows()