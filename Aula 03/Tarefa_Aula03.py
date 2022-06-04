from random import randint
import cv2
import numpy as np


BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS = [BLUE, GREEN, RED, BLACK, GRAY]

points = []
c = randint(0, len(COLORS)-1)


def circle(frame):
    for x, y in points:
        cv2.circle(frame, (x, y), 30, COLORS[c], -1)


def draw_circle(event, x, y, flags, param):  # Função para desenhar circulos
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

# =============================================================================


capture = cv2.VideoCapture("../files/IFMA Campus Caxias.mp4")  # Lendo o vídeo

# Acessando as informações da imagem
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# Mostrando as informações
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))

# Configurações do mouse
cv2.namedWindow('Rabiscado')
cv2.setMouseCallback('Rabiscado', draw_circle)

if not capture.isOpened():
    print("Erro ao acessar o vídeo")
else:
    # Criando a base do novo arquivo de vídeo, para modificar depois
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("video_rabiscado.avi", fourcc, int(
        fps), (int(frame_width), int(frame_height)), True)

    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:

            circle(frame)

            output.write(frame)

            cv2.imshow('Rabiscado', frame)

            if cv2.waitKey(20) & 0xFF == 27:  # Fechando o programa
                break

            if cv2.waitKey(20) & 0xFF == 32:  # Limpando a tela
                points = []
                print('Tela limpa')

            if cv2.waitKey(20) & 0xFF == ord('c'):  # Sorteando a cor
                c = randint(0, len(COLORS)-1)
                print("Sorteado: ", c)

            # if cv2.waitKey(20) & 0xFF == ord('w'):  # Salvando um print
            #     print("Salvando frame...")
            #     # cv2.imwrite('print.jpg', scribbled)

        else:
            break

capture.release()
output.release()
cv2.destroyAllWindows()
