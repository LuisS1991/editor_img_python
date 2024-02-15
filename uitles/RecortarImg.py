import cv2 as cv
import os
from config import temp_path, imagen_cortada


xI, yI, xF, yF = 0, 0, 0, 0
flag = False
img = None


def draw(event, x, y, bandera, param):
    # para que sean globales
    global xI, yI, xF, yF, flag, img

    # cuando se oprimer el btn izquirdo raton
    if event == cv.EVENT_LBUTTONDOWN:
        xI, yI = x, y
        flag = False

    # cuando se deja oprimer el btn izquirdo raton
    if event == cv.EVENT_LBUTTONUP:
        xF, yF = x, y
        flag = True
        recortar = img[yI:yF, xI:xF, :]
        cv.imwrite(str(os.path.join(temp_path, imagen_cortada)), recortar)


def init(imagen):
    global img, flag
    img = cv.imread(imagen, cv.IMREAD_UNCHANGED)
    scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    cv.namedWindow("ventana", cv.WINDOW_AUTOSIZE)
    cv.setMouseCallback("ventana", draw)

    while True:
        img = resized

        if flag == True:
            cv.rectangle(img, (xI, yI), (xF, yF), (255, 0, 0), 2)

        cv.imshow("ventana", img)

        k = cv.waitKey(1) & 0xFF
        if k == 27 or not cv.getWindowProperty("ventana", cv.WND_PROP_VISIBLE):
            flag = False
            break

    cv.destroyAllWindows()
