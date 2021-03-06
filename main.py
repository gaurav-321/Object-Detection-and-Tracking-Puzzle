import cv2
import numpy as np
import imutils
import sys

crop_pix = []
done = False
locations = []

if len(sys.argv)>1:
    IMAGE = sys.argv[1]
else:
    IMAGE = "sample/odd-one-out-puzzle.png"
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(crop_pix) < 2:
        crop_pix.append((x, y))


def crop_pic(input_img, x, y, w, h):
    img = input_img.copy()[y:y + h, x:x + w]
    return img


def nothing(*args):
    global done
    done = False
    pass


def reset():
    global locations, done
    crop_pix.clear()
    locations = []
    done = False


cv2.namedWindow('Number of real object')
cv2.createTrackbar('l_R', 'Number of real object', 0, 100, nothing)
cv2.setTrackbarPos('l_R', 'Number of real object', 95)

while True:
    image = cv2.imread(
        IMAGE)
    image = imutils.resize(image, width=1280)
    if len(crop_pix) == 2:
        x, y = crop_pix[0]
        w, h = crop_pix[1][0] - x, crop_pix[1][1] - y
        crop = crop_pic(image, x, y, w, h)
        cv2.imshow("crop", crop)
        if not done:
            res = cv2.matchTemplate(image, crop, cv2.TM_CCOEFF_NORMED)
            threshold = cv2.getTrackbarPos('l_R', 'Number of real object')
            loc = np.where(res >= threshold/100)
            locations = loc
            for pt in zip(*locations[::-1]):  # Switch collumns and rows
                cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), -1)
            done = True
        else:
            for pt in zip(*locations[::-1]):  # Switch collumns and rows
                cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), -1)

    cv2.imshow("original", image)

    cv2.setMouseCallback('original', onMouse)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    elif cv2.waitKey(1) & 0xFF == ord("r"):
        reset()
