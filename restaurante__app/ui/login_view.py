import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root, servicio, mostrar_principal):
        self.root = root
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)

        titulo = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        tk.Label(
            self.frame,
            text="Usuario:"
        ).pack()

        self.usuario_entry = tk.Entry(self.frame)
        self.usuario_entry.pack(pady=5)

        tk.Label(
            self.frame,
            text="Contraseña:"
        ).pack()

        self.contraseña_entry = tk.Entry(
            self.frame,
            show="*"
        )
        self.contraseña_entry.pack(pady=5)

        tk.Button(
            self.frame,
            text="Ingresar",
            command=self.ingresar
        ).pack(pady=20)

    def ingresar(self):
        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()

        if not usuario or not contraseña:
            messagebox.showwarning(
                "Campos vacíos",
                "Ingrese usuario y contraseña."
            )
            return

        if self.servicio.validar_usuario(usuario, contraseña):
            self.frame.destroy()
            self.mostrar_principal()
        else:
            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )