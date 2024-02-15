def centrar_ventana(ventana, alto, ancho):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho / 2))
    y = int((pantalla_alto / 2) - (alto / 2))
    return ventana.geometry(f"{alto}x{ancho} +{x}+{y}")
