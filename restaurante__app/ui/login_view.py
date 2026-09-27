import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root, servicio, mostrar_principal):
        self.root = root
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        self.frame = tk.Frame(
            self.root,
            bg="white"
        )

        self.frame.pack(
            expand=True,
            fill="both"
        )

        titulo = tk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 24, "bold"),
            bg="white",
            fg="#8B3A62"
        )

        titulo.pack(pady=(60, 30))

        subtitulo = tk.Label(
            self.frame,
            text="Inicio de sesión",
            font=("Arial", 14),
            bg="white"
        )

        subtitulo.pack(pady=5)

        tk.Label(
            self.frame,
            text="Usuario:",
            font=("Arial", 11),
            bg="white"
        ).pack(pady=(20, 5))

        self.usuario_entry = tk.Entry(
            self.frame,
            font=("Arial", 11),
            width=30
        )

        self.usuario_entry.pack(pady=5)

        tk.Label(
            self.frame,
            text="Contraseña:",
            font=("Arial", 11),
            bg="white"
        ).pack(pady=(10, 5))

        self.contraseña_entry = tk.Entry(
            self.frame,
            show="*",
            font=("Arial", 11),
            width=30
        )

        self.contraseña_entry.pack(pady=5)

        tk.Button(
            self.frame,
            text="Ingresar",
            font=("Arial", 11, "bold"),
            width=20,
            bg="#8B3A62",
            fg="white",
            command=self.ingresar
        ).pack(pady=25)

        self.usuario_entry.focus()

        self.root.bind(
            "<Return>",
            lambda event: self.ingresar()
        )

    def ingresar(self):
        usuario = self.usuario_entry.get().strip()
        contraseña = self.contraseña_entry.get().strip()

        if not usuario or not contraseña:
            messagebox.showwarning(
                "Campos vacíos",
                "Ingrese usuario y contraseña."
            )
            return

        if self.servicio.validar_usuario(
            usuario,
            contraseña
        ):
            self.root.unbind("<Return>")
            self.frame.destroy()
            self.mostrar_principal()

        else:
            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )

            self.contraseña_entry.delete(
                0,
                tk.END
            )

            self.contraseña_entry.focus()