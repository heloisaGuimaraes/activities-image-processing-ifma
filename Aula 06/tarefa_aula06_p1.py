import cv2

GREEN = (0, 255, 0)
angle = 0

def setCenter(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img, (x, y), 3, GREEN, -1)
        center[0] = x
        center[1] = y
        
def rotateImage(img):
    M = cv2.getRotationMatrix2D((center[0], center[1]), angle, 1)
    res = cv2.warpAffine(img, M, (cols, rows))
   
    return res
    
img = cv2.imread('../files/logo-if.jpg')
rows, cols = img.shape[:2]
center = [(cols-1)/2.0, (rows-1)/2.0]

cv2.namedWindow('Logo IF')
cv2.setMouseCallback('Logo IF', setCenter)
cv2.imshow('Logo IF', img)

while(1):
    k = cv2.waitKey(20)
    if k == 100:  # d
        angle -= 5
        cv2.imshow('Logo IF', rotateImage(img))
        print('angulo em:', angle)
        
    if k == 114:  # r
        angle += 5
        cv2.imshow('Logo IF', rotateImage(img))
        print('angulo em:', angle)
        
    elif k == 27:  # esc
        break
cv2.destroyAllWindows()

