import cv2 as cv

xI, yI, xF, yF = 0, 0, 0, 0
flag = False
img = None

def draw(event, x, y, bandera, param):
    # para que sean globales
    global xI, yI, xF, yF, flag, img, temp_path

    # cuando se oprimer el btn izquirdo raton
    if event == cv.EVENT_LBUTTONDOWN:
        xI, yI = x, y
        flag = False

    # cuando se deja oprimer el btn izquirdo raton
    if event == cv.EVENT_LBUTTONUP:
        xF, yF = x, y
        flag = True
        recortar = img[yI:yF, xI:xF, :]

        cv.imwrite("temp/temp_recortada.jpeg", recortar)


def init(imagen) -> str:
    global img
    img = cv.imread(imagen)
    cv.namedWindow("ventana")
    cv.setMouseCallback("ventana", draw)

    while True:
        img = cv.imread(imagen)

        if flag == True:
            cv.rectangle(img, (xI, yI), (xF, yF), (255, 0, 0), 2)

        cv.imshow("ventana", img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()
    return "temp_recortada.jpeg"
