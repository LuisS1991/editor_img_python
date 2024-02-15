import shutil
from tkinter import messagebox
from uitles import Opencv
from uitles.FileHelper import seleccionarImagen, rutaSeleccionada, eliminar_temporales
from .Ventana_Princiapl_Disenio import VentanaPpl


class Ventana(VentanaPpl):
    def __init__(self) -> None:
        super().__init__()
        self.__openCV = Opencv()

    def on_closing(self):
        eliminar_temporales(self.temp_path)
        self.destroy()

    def cortar_imgen(self):
        if len(self.image_path) > 0:
            img_tmp = self.__openCV.CortarImagen(self.image_path)
            self.image_path = img_tmp
            self.imagen_trabajo = self.cargar_imagen_trabajo("", self.image_path)
            self.imagen_trabajo.grid(row=0, column=0, padx=50, pady=10)
        else:
            messagebox.showerror(message="seleccione una imagen", title="Error")

    def rotar_imagen(self):
        if len(self.image_path) > 0:
            img_tmp = self.__openCV.RotarImagen(self.image_path)
            self.image_path = img_tmp
            self.imagen_trabajo = self.cargar_imagen_trabajo("", self.image_path)
            self.imagen_trabajo.grid(row=0, column=0, padx=50, pady=10)
        else:
            messagebox.showerror(message="seleccione una imagen", title="Error")

    def guardarFoto(self):
        if len(self.image_path) > 0:
            destino = rutaSeleccionada()
            shutil.copy(self.image_path, destino)
            eliminar_temporales(self.temp_path)
            messagebox.showinfo(
                message="Imagen Eportada Correctamente", title="Guardado"
            )
        else:
            messagebox.showerror(message="seleccione una imagen", title="Error")

    def seleccionar_imagen(self):
        self.image_path = seleccionarImagen()
        self.imagen_trabajo = self.cargar_imagen_trabajo("", self.image_path)
        self.imagen_trabajo.grid(row=0, column=0, padx=50, pady=10)
        eliminar_temporales(self.temp_path)
