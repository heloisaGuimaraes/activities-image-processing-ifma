# coding=utf-8
import cv2,sys

counter = 0
detections = [(0,0)]
def countPeople(x, y):
    lx, ly = detections[-1]
    rx = abs(lx-x)
    ry = abs(ly-y)
    n = 30
    
    if (rx<n or ry<n):
        detections[-1] = (x, y)
        return 0
    else:
        detections.append((x, y))
        return 1

# Put Text
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.6
color = (0, 0, 0)
thickness = 2  # px

def resize_image(image, scale_percent=50):
    rows, cols = image.shape[:2]
    width = int(cols * scale_percent / 100)
    height = int(rows * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image

face_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_frontalface_default.xml')

size = 35
cap = cv2.VideoCapture("../../files/IFMA Campus Caxias.mp4")
if not cap.isOpened():
    print("Erro ao abrir video")
    sys.exit(0)
else: 
    while cap.isOpened():
        ret, frame = cap.read()
        
        if ret is True:
            img = resize_image(frame)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,minSize=(size, size),scaleFactor=1.6)
        
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_color = img[y:y+h, x:x+w]
                center=(w//2, h//2)
                cv2.circle(roi_color, center, 2, (255, 0, 0), 3)
                a, b = center
                counter += countPeople(x, y)
                
            cv2.putText(img, "People: "+str(counter), (20 , 20), font,fontScale, color, thickness, cv2.LINE_AA)
                

            cv2.imshow('IFMA', img)
            c = cv2.waitKey(1)
            if c == 27:
                break
        else:
            break
        
cap.release()
cv2.destroyAllWindows()
