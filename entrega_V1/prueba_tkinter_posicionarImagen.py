import tkinter as tk
from PIL import Image, ImageTk


class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configuración de la ventana principal
        self.title("Ventana Principal")

        # Cargar imagen
        self.imagen = Image.open(
            "C:\\Users\\Edu guapo\\Desktop\\TFG_Automatize3\\entrega_V1\\Resources\\automatize_logo.png")
        self.imagen = self.imagen.resize((400, 400), Image.ANTIALIAS)  # Ajustar tamaño inicial
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        # Crear widget Label para mostrar la imagen
        self.label_imagen = tk.Label(self, image=self.imagen_tk)
        self.label_imagen.pack(fill=tk.BOTH, expand=True)

        # Establecer la función de ajuste de tamaño de la imagen cuando cambie el tamaño de la ventana
        self.bind("<Configure>", self.ajustar_tamaño_imagen)

    def ajustar_tamaño_imagen(self, event):
        # Obtener las nuevas dimensiones de la ventana
        nueva_altura = event.height - self.label_imagen.winfo_y() - 10
        nueva_anchura = event.width - 10

        # Redimensionar imagen
        self.imagen = self.imagen.resize((nueva_anchura, nueva_altura), Image.ANTIALIAS)
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        # Actualizar widget Label con la nueva imagen redimensionada
        self.label_imagen.configure(image=self.imagen_tk)


if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.mainloop()
