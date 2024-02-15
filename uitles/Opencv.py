import cv2 as cv
import os
from .RecortarImg import init
from config import temp_path, imagen_rotada, imagen_cortada


class Opencv:
    def __init__(self) -> None:
        self.img = None

    # self.temp_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp")

    def RotarImagen(self, img) -> str:
        img = cv.imread(img)
        rotada = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
        cv.imwrite(str(os.path.join(temp_path, imagen_rotada)), rotada)
        cv.waitKey(0)
        return os.path.join(temp_path, imagen_rotada)

    def CortarImagen(self, img) -> str:
        init(img)
        if os.path.isfile(str(os.path.join(temp_path, imagen_cortada))) == True:
            return os.path.join(temp_path, imagen_cortada)
        else:
            return img
