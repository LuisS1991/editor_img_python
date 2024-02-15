import customtkinter
from PIL import Image
import os
from Uitles.FileHelper import seleccionarImge, rutaSeleccionada, eliminar_temporales
from Uitles import Opencv
import shutil
import sys


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("image_example.py")
        self.geometry("1000x650")
        self.image_path = ""
        self.temp_path = "temp/"
        self.icons_path = "recursos/"
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.__init_nav()
        self.__init_panel()
        self.__openCV = Opencv()

    def __init_panel(self):
        self.my_frame = customtkinter.CTkFrame(master=self)
        self.my_frame.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")

        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.my_frame,
            text="sin imagen",
            image=customtkinter.CTkImage(
                Image.open(os.path.join(self.icons_path, "image_icon_light.png")),
                size=(700, 600),
            ),
        )
        self.home_frame_large_image_label.grid(row=0, column=0, padx=50, pady=10)

    def __init_nav(self):
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text="Image Example",
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold"),
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Seleccionar Imagen",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.__seleccionar_imagen,
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Recortar Imagen",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.__cortar_imgen,
        )
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Rotar Imagen",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.__rotar_imagen,
        )
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Exportar",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=self.guardarFoto,
        )
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

    # eventos
    def __seleccionar_imagen(self):
        # print("evento")
        self.image_path = seleccionarImge()
        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.my_frame,
            text="",
            image=customtkinter.CTkImage(Image.open(self.image_path), size=(800, 600)),
        )
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

    def __cortar_imgen(self):
        img_tmp = self.__openCV.CortarImagen(self.image_path)
        print(img_tmp)
        self.image_path = os.path.join(self.temp_path, img_tmp)
        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.my_frame,
            text="",
            image=customtkinter.CTkImage(
                Image.open(os.path.join(self.temp_path, img_tmp)), size=(800, 600)
            ),
        )
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

    def __rotar_imagen(self):
        img_tmp = self.__openCV.RotarImagen(self.image_path)

        self.image_path = os.path.join(self.temp_path, img_tmp)
        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.my_frame,
            text="",
            image=customtkinter.CTkImage(
                Image.open(os.path.join(self.temp_path, img_tmp)), size=(800, 600)
            ),
        )
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

    def guardarFoto(self):
        destino = rutaSeleccionada()
        shutil.copy(self.image_path, destino)
        eliminar_temporales(self.temp_path)
        pass


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = App()
    app.mainloop()
