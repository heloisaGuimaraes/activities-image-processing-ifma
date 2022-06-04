import cv2
import numpy as np
# numpy - w, h = r, c
# opencv - h, w = c, r

# (w, h)
ar_4_3 = (1280, 960)
ar_16_9 = (1280, 720)


def resize_image(image, scale_percent=50):
    rows, cols = image.shape[:2]
    width = int(cols * scale_percent / 100)
    height = int(rows * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image


def change_aspect_ratio(image, a_ratio=ar_4_3):
    output = np.zeros(image.shape, np.uint8)
    r = a_ratio[0] / image.shape[1]  # 1280.0 / image.shape[1]
    dim = (a_ratio[1], int(image.shape[0] * r))
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    output[:, 159:1119] = image
    return output


def crop_image(image):
    output = np.zeros(image.shape, np.uint8)
    output[:, 159:1119] = image[:, 159:1119].copy()
    return output


def make_mask(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY_INV)
    n = 2
    kernel_size = (n, n)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    mask = cv2.dilate(mask, kernel, iterations=3)
    # cv2.imshow('mask', mask)
    return mask


def inpaint_logo(image):
    width, height = logo_if.shape[:2]
    mask_if = make_mask(logo_if)
    # cv2.imshow('mask', mask_if)

    # GET LOCAL
    s_rows = 31
    e_rows = s_rows+width
    s_cols = 1133
    e_cols = s_cols+height
    local = image[s_rows:e_rows, s_cols:e_cols]

    # MASK AND LOCAL
    local[mask_if != 0] = [0, 0, 0]
    # cv2.imshow('local', local)

    n = 5
    # telea = cv2.inpaint(local, mask_if, n, cv2.INPAINT_TELEA)
    # image[s_rows:e_rows, s_cols:e_cols] = telea

    ns = cv2.inpaint(local, mask_if, n, cv2.INPAINT_NS)
    image[s_rows:e_rows, s_cols:e_cols] = ns

    return image


# =========================================================
capture = cv2.VideoCapture("../files/IFMA Campus Caxias.mp4")

logo_if = cv2.imread('logo-if-vertical.png')
logo_if = resize_image(logo_if, 20)
# cv2.imshow('if-logo', logo_if)

can_crop = False
can_change = False
if not capture.isOpened():
    print("Error accessing video")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            frame = inpaint_logo(frame)

            if (can_change):
                frame = change_aspect_ratio(frame)
            elif (can_crop):
                frame = crop_image(frame)

            cv2.imshow('original', resize_image(frame))
            # cv2.imshow('original', frame)

            k = cv2.waitKey(20)
            if k == 97:  # a
                can_change = not can_change
                can_crop = False

            if k == 99:  # c
                can_crop = not can_crop
                can_change = False

            # if k == 114:  # r
            #     isCropped = False
            #     isChanged = False

            if (k == 113 or k == 27):  # q or ESC
                break
        else:
            break

capture.release()
cv2.destroyAllWindows()
