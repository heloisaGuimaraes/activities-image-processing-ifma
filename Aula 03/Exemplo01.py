import cv2

#  Acessando a webcam ou um vídeo já pronto
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("../files/IFMA Campus Caxias.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("WIDTH: '{}'".format(frame_width))
print("HEIGHT : '{}'".format(frame_height))

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        # Informação se está funcionando, imagem do momento
        if ret is True:  # Se está funcionando:
            cv2.imshow('Input', frame)  # Mostramos a imagem

            # Convertemos em escala de cinza
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('Cinza', gray)  # Mostramos a nova imagem

            if cv2.waitKey(20) & 0xFF == ord('q'):  # Comando para fechar
                break

            if cv2.waitKey(20) & 0xFF == ord('w'):  # Comando para salvar uma imagem
                print("Salvando frame...")
                cv2.imwrite('print.jpg', frame)
                cv2.imwrite('gray.jpg', gray)

        else:
            break

capture.release()
cv2.destroyAllWindows()
