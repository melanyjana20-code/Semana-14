import tkinter as tk
from tkinter import messagebox


class MainView:

    def __init__(self, root, servicio, cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        titulo = tk.Label(
            self.frame,
            text="Panel Principal - Restaurante",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        tk.Button(
            self.frame,
            text="Ver Productos",
            width=20,
            command=self.mostrar_productos
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="Ver Usuarios",
            width=20,
            command=self.mostrar_usuarios
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="Ventas (Pendiente)",
            width=20,
            state="disabled"
        ).pack(pady=5)

        tk.Button(
            self.frame,
            text="Cerrar sesión",
            width=20,
            command=self.cerrar
        ).pack(pady=20)

    def mostrar_productos(self):
        productos = self.servicio.listar_productos()

        texto = "PRODUCTOS REGISTRADOS\n\n"

        for producto in productos:
            texto += (
                f"ID: {producto.id}\n"
                f"Nombre: {producto.nombre}\n"
                f"Precio: ${producto.precio:.2f}\n"
                f"Cantidad: {producto.cantidad}\n"
                "--------------------------\n"
            )

        messagebox.showinfo("Productos", texto)

    def mostrar_usuarios(self):
        usuarios = self.servicio.listar_usuarios()

        texto = "USUARIOS REGISTRADOS\n\n"

        for usuario in usuarios:
            texto += (
                f"ID: {usuario.id}\n"
                f"Nombre: {usuario.nombre}\n"
                f"Usuario: {usuario.usuario}\n"
                "--------------------------\n"
            )

        messagebox.showinfo("Usuarios", texto)

    def cerrar(self):
        self.frame.destroy()
        self.cerrar_sesion()