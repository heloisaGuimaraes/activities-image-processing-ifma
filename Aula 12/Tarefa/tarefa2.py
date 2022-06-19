import cv2
import numpy as np

# Put Text
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.6
color = (0, 0, 0)
thickness = 2  # px

# Sort by radius
VALUES = ['10 cents', '5 cents', '50 cents', '25 cents', '1 real']
# ============================================

img = cv2.imread('../../files/coins.jpeg')
img_blur = cv2.medianBlur(img, 5)
img_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT,
                           1, 100, param1=200, param2=50, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
sorted_circles = np.sort(circles[0, :, -1])

for i in circles[0, :]:  # x, y, r
    x, y, r = i[0:3]

    cv2.circle(img, (x, y), r, (0, 0, 255), 2)
    cv2.circle(img, (x, y), 2, (255, 0, 0), 3)

    text = VALUES[np.argmax(sorted_circles == r)]
    cv2.putText(img, text, (x, y+r), font,
                fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow('Coins', img)

cv2.waitKey(0)
cv2.destroyAllWindows()