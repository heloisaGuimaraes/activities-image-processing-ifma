import cv2
import numpy as np


def rotateImage(img):
    M = cv2.getRotationMatrix2D((0, 0), angle, 1)
    M = np.array([M[0], M[1], [0, 0, 1]])
    M_translate = np.identity(3)
    M_translate[2][0] = -center[0]  # c
    M_translate[2][1] = -center[1]  # l
    M = M_translate.dot(M)
    M_translate[2][0] = center[0]  # c
    M_translate[2][1] = center[1]  # l
    M = M.dot(M_translate)
    
    M = np.linalg.inv(M)

    res = rotateInv(img, M, cols, rows)
    return res


def rotateInv(img, M, cols, rows):
    output = np.zeros(img.shape, np.uint8)
    point = np.ones((1, 3))
    for c in range(cols):
        point[0][0] = c
        for r in range(rows):
            point[0][1] = r
            output[r][c] = calculate_points(point, M, cols, rows)
    return output


def calculate_points(point, M, cols, rows):
    new_pos = point.dot(M)
    col = int(new_pos[0][0])
    row = int(new_pos[0][1])

    if (any([col < 0, col >= cols, row < 0, row >= rows])):
        return np.array([0, 0, 0])
    else:
        return img[row][col]


def setCenter(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img, (x, y), 3, GREEN, -1)
        center[0] = x
        center[1] = y


# =====================================================================
angle = 0
img = cv2.imread('../files/logo-if.jpg')
rows, cols = img.shape[:2]
center = [(cols-1)/2.0, (rows-1)/2.0]
print(center)


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
