# coding=utf-8
# import numpy as np
import cv2

def resize_image(image, scale_percent=50):
    rows, cols = image.shape[:2]
    width = int(cols * scale_percent / 100)
    height = int(rows * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image

def put_object(img,object, x, y, adjx=15, adjy=15):
    obj_rows, obj_cols = object.shape[:2]
    roi_img = img[(y-adjy):(y-adjy)+obj_rows, (x-adjx):(x-adjx)+obj_cols] 
    roi_img [object < [150,150,150]] = object [object < [150,150,150]]    
    return img
    
# ==========================================================================
face_cascade = cv2.CascadeClassifier(
    '../classificadores/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier(
    '../classificadores/haarcascade_mcs_mouth.xml')
# ==========================================================================

img = cv2.imread('face.jpg')
img = resize_image(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

moustache = cv2.imread('moustache_w.png')
moustache = resize_image(moustache, 30)


glasses = cv2.imread('sungalsses_w.png')
glasses = resize_image(glasses, 30)

faces = face_cascade.detectMultiScale(gray)
for (x, y, w, h) in faces:
    # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)   
    for (ex, ey, ew, eh) in eyes:
        roi_color = put_object(roi_color, glasses, ex, ey, 14, -10)
        break
        # cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        

    mouth = mouth_cascade.detectMultiScale(roi_gray, 2.0, 20)
    for (mx, my, mw, mh) in mouth:
        roi_color = put_object(roi_color, moustache, mx, my, 15,15)
        # cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 0, 255), 2)
        # break

cv2.imshow('Turing', img)

cv2.waitKey(0)
cv2.destroyAllWindows()