import cv2

def resize_image(image, scale_percent=50):
    rows, cols = image.shape[:2]
    width = int(cols * scale_percent / 100)
    height = int(rows * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image

capture = cv2.VideoCapture("../../files/IFMA Campus Caxias.mp4")

if not capture.isOpened():
    print("Erro ao acessar o vídeo")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            frame = resize_image(frame)
            cv2.imshow('Original', frame)
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('Cinza', gray)
            
            canny = cv2.Canny(frame,90,180)
            cv2.imshow('Canny', canny)
            
            k = cv2.waitKey(20)
            if k == 27:  # esc
                break
        else:
            break

capture.release()
cv2.destroyAllWindows()