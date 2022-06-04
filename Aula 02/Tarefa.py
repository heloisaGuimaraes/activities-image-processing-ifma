import cv2
# Carregando as imagens: uma para teste e a outra para comparar
img = cv2.imread('../files/logo-if.jpg')

gray = cv2.imread('../files/logo-if.jpg', cv2.IMREAD_GRAYSCALE)

# Pegando as informações da matriz da imagem (as tuplas de pixels)
(row, col) = img.shape[0:2]

for i in range(row):
    for j in range(col):
        img[i, j] = sum(img[i, j]) * 0.33
        # Fazendo uma média para transformar em uma escala só

cv2.imshow('Media', img)
cv2.imshow('Gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
