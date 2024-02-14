import cv2 as cv
from .RecortarImg import init


class Opencv:
    def __init__(self) -> None:
        self.img = None

    # self.temp_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp")

    def RotarImagen(self, img) -> str:
        img = cv.imread(img)
        rotada = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
        cv.imwrite("temp/img_temp_rotada_90.jpeg", rotada)
        cv.waitKey(0)
        return "img_temp_rotada_90.jpeg"

    def CortarImagen(self, img) -> str:
        init(img)
        return "temp_recortada.jpeg"
