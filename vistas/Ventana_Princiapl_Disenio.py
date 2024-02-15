import customtkinter
from PIL import Image
from uitles.Centrar_Ventana import centrar_ventana
from config import temp_path, icons_path, imagen_empyt_default


class VentanaPpl(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        # funcionamiento del programa
        self.image_path = ""
        self.temp_path = temp_path
        self.icons_path = icons_path
        self.logo_image = customtkinter.CTkImage(
            Image.open("favicon.ico"), size=(26, 26)
        )
        self.__config_ventana()
        self.__menu_lateral()
        self.__cargar_area_trabajo()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        pass

    # configuracion de ventana
    def __config_ventana(self) -> None:
        self.title("Editor imagenes")
        self.iconbitmap("favicon.ico")
        w, h = 1024, 650
        self.geometry("%dx%d+0+0" % (w, h))
        centrar_ventana(self, w, h)
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    # area de trabajo
    def __cargar_area_trabajo(self):
        self.my_frame = customtkinter.CTkFrame(master=self)
        self.my_frame.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")

        self.imagen_trabajo = self.cargar_imagen_trabajo(
            "seleccionar imagen", imagen_empyt_default
        )
        self.imagen_trabajo.grid(row=0, column=0, padx=50, pady=10)

    # menu lateral
    def __menu_lateral(self):
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text="Editor Imagenes",
            image=self.logo_image,
            padx=5, pady=5,
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
            command=self.seleccionar_imagen,
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
            command=self.cortar_imgen,
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
            command=self.rotar_imagen,
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

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    # auxiliares
    def cargar_imagen_trabajo(self, texto, imagen):
        return customtkinter.CTkLabel(
            self.my_frame,
            text=texto,
            image=customtkinter.CTkImage(
                Image.open(imagen),
                size=(700, 600),
            ),
        )

    # eventos
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def cortar_imgen(self):
        pass

    def rotar_imagen(self):
        pass

    def guardarFoto(self):
        pass

    def seleccionar_imagen(self):
        pass
