import tkinter as tk
import os

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("900x600")
        self.root.resizable(True, True)

        archivo_servicio = ArchivoServicio()

        base_dir = os.path.dirname(os.path.abspath(__file__))

        ruta_usuarios = os.path.join(
            base_dir,
            "datos",
            "usuarios.json"
        )

        ruta_productos = os.path.join(
            base_dir,
            "datos",
            "productos.json"
        )

        ruta_ventas = os.path.join(
            base_dir,
            "datos",
            "ventas.json"
        )

        usuarios = archivo_servicio.leer_json(ruta_usuarios)
        productos = archivo_servicio.leer_json(ruta_productos)

        # Si ventas.json está vacío, se inicializa como una lista.
        if not os.path.exists(ruta_ventas) or os.path.getsize(ruta_ventas) == 0:
            archivo_servicio.guardar_json(ruta_ventas, [])

        self.restaurante_servicio = RestauranteServicio(
            usuarios,
            productos,
            archivo_servicio,
            ruta_productos,
            ruta_ventas
        )

        self.mostrar_login()

    def mostrar_login(self):
        LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_principal
        )

    def mostrar_principal(self):
        MainView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_login
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()