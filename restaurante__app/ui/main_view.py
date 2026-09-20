import tkinter as tk
from tkinter import ttk, messagebox


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
        titulo.pack(pady=10)

        menu = tk.Frame(self.frame)
        menu.pack(pady=5)

        ttk.Button(
            menu,
            text="Ver Productos",
            command=self.mostrar_productos
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            menu,
            text="Ver Usuarios",
            command=self.mostrar_usuarios
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            menu,
            text="Ventas (Pendiente)",
            state="disabled"
        ).grid(row=0, column=2, padx=5)

        ttk.Button(
            menu,
            text="Cerrar sesión",
            command=self.cerrar
        ).grid(row=0, column=3, padx=5)

        self.contenido = tk.Frame(self.frame)
        self.contenido.pack(
            expand=True,
            fill="both",
            padx=15,
            pady=10
        )

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_productos(self):
        self.limpiar_contenido()

        formulario = tk.LabelFrame(
            self.contenido,
            text="Gestión de productos",
            padx=10,
            pady=10
        )
        formulario.pack(fill="x", pady=5)

        tk.Label(formulario, text="ID:").grid(
            row=0, column=0, padx=5, pady=5
        )

        self.id_entry = tk.Entry(formulario)
        self.id_entry.grid(
            row=0, column=1, padx=5, pady=5
        )

        tk.Label(formulario, text="Nombre:").grid(
            row=1, column=0, padx=5, pady=5
        )

        self.nombre_entry = tk.Entry(formulario)
        self.nombre_entry.grid(
            row=1, column=1, padx=5, pady=5
        )

        tk.Label(formulario, text="Precio:").grid(
            row=0, column=2, padx=5, pady=5
        )

        self.precio_entry = tk.Entry(formulario)
        self.precio_entry.grid(
            row=0, column=3, padx=5, pady=5
        )

        tk.Label(formulario, text="Cantidad:").grid(
            row=1, column=2, padx=5, pady=5
        )

        self.cantidad_entry = tk.Entry(formulario)
        self.cantidad_entry.grid(
            row=1, column=3, padx=5, pady=5
        )

        botones = tk.Frame(formulario)
        botones.grid(
            row=2,
            column=0,
            columnspan=4,
            pady=10
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self.registrar_producto
        ).grid(row=0, column=0, padx=5)

        ttk.Button(
            botones,
            text="Cargar por ID",
            command=self.cargar_producto
        ).grid(row=0, column=1, padx=5)

        ttk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).grid(row=0, column=2, padx=5)

        ttk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).grid(row=0, column=3, padx=5)

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).grid(row=0, column=4, padx=5)

        tabla_frame = tk.LabelFrame(
            self.contenido,
            text="Productos registrados"
        )
        tabla_frame.pack(
            expand=True,
            fill="both",
            pady=5
        )

        columnas = ("id", "nombre", "precio", "cantidad")

        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading("id", text="ID")
        self.tabla_productos.heading("nombre", text="Nombre")
        self.tabla_productos.heading("precio", text="Precio")
        self.tabla_productos.heading("cantidad", text="Cantidad")

        self.tabla_productos.column(
            "id",
            width=60
        )

        self.tabla_productos.column(
            "nombre",
            width=180
        )

        self.tabla_productos.column(
            "precio",
            width=100
        )

        self.tabla_productos.column(
            "cantidad",
            width=100
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_productos.pack(
            side="left",
            expand=True,
            fill="both"
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.cargar_tabla_productos()

    def cargar_tabla_productos(self):
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = self.servicio.listar_productos()

        for producto in productos:
            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.id,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.cantidad
                )
            )

    def registrar_producto(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        cantidad = self.cantidad_entry.get()

        if not id or not nombre or not precio or not cantidad:
            messagebox.showwarning(
                "Campos vacíos",
                "Complete todos los campos."
            )
            return

        correcto, mensaje = self.servicio.registrar_producto(
            id,
            nombre,
            precio,
            cantidad
        )

        if correcto:
            messagebox.showinfo(
                "Registro",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()
        else:
            messagebox.showerror(
                "Error",
                mensaje
            )

    def cargar_producto(self):
        id = self.id_entry.get()

        if not id:
            messagebox.showwarning(
                "Campo vacío",
                "Ingrese el ID del producto."
            )
            return

        producto = self.servicio.buscar_producto(id)

        if producto is None:
            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )
            return

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, producto.nombre)

        self.precio_entry.delete(0, tk.END)
        self.precio_entry.insert(0, producto.precio)

        self.cantidad_entry.delete(0, tk.END)
        self.cantidad_entry.insert(0, producto.cantidad)

    def actualizar_producto(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        cantidad = self.cantidad_entry.get()

        if not id or not nombre or not precio or not cantidad:
            messagebox.showwarning(
                "Campos vacíos",
                "Complete todos los campos."
            )
            return

        correcto, mensaje = self.servicio.actualizar_producto(
            id,
            nombre,
            precio,
            cantidad
        )

        if correcto:
            messagebox.showinfo(
                "Actualización",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()
        else:
            messagebox.showerror(
                "Error",
                mensaje
            )

    def eliminar_producto(self):
        id = self.id_entry.get()

        if not id:
            messagebox.showwarning(
                "Campo vacío",
                "Ingrese el ID del producto."
            )
            return

        confirmar = messagebox.askyesno(
            "Eliminar producto",
            "¿Está seguro de eliminar este producto?"
        )

        if not confirmar:
            return

        correcto, mensaje = self.servicio.eliminar_producto(id)

        if correcto:
            messagebox.showinfo(
                "Eliminación",
                mensaje
            )

            self.limpiar_formulario()
            self.cargar_tabla_productos()
        else:
            messagebox.showerror(
                "Error",
                mensaje
            )

    def limpiar_formulario(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        grupo = tk.LabelFrame(
            self.contenido,
            text="Usuarios registrados",
            padx=10,
            pady=10
        )
        grupo.pack(
            expand=True,
            fill="both"
        )

        columnas = (
            "id",
            "nombre",
            "usuario"
        )

        tabla = ttk.Treeview(
            grupo,
            columns=columnas,
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("usuario", text="Usuario")

        tabla.column("id", width=60)
        tabla.column("nombre", width=200)
        tabla.column("usuario", width=150)

        scrollbar = ttk.Scrollbar(
            grupo,
            orient="vertical",
            command=tabla.yview
        )

        tabla.configure(
            yscrollcommand=scrollbar.set
        )

        tabla.pack(
            side="left",
            expand=True,
            fill="both"
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        usuarios = self.servicio.listar_usuarios()

        for usuario in usuarios:
            tabla.insert(
                "",
                "end",
                values=(
                    usuario.id,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    def cerrar(self):
        self.frame.destroy()
        self.cerrar_sesion()