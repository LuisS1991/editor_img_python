from tkinter import filedialog
import os


def seleccionarImge():
    ruta_imge = filedialog.askopenfile(
        initialdir="/home/jpmontevideo/Descargas",
        filetypes=[("image", ".jpg"), ("image", ".jpeg"), ("image", ".png")],
    )
    if len(ruta_imge.name) > 0:
        return ruta_imge.name

    return "/home/jpmontevideo/Descargas"


def rutaSeleccionada():
    guardarimg = filedialog.asksaveasfilename(
        initialdir="/home/jpmontevideo/Descargas",
        title="Seleccione el archivo",
        defaultextension=".jpeg",
        filetypes=(("jpeg files", "*.jpeg"), ("all files", "*.*")),
    )
    if len(guardarimg) > 0:
        return guardarimg
    return "/home/jpmontevideo/Descargas/"


def eliminar_temporales(ruta):
    fiecheros_temp = os.listdir(ruta)
    for temp in fiecheros_temp:
        os.remove(os.path.join(ruta, temp))
