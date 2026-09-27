import json
from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:

    def __init__(
        self,
        usuarios,
        productos,
        archivo_servicio=None,
        ruta_productos=None,
        ruta_ventas=None
    ):
        self.usuarios = [
            Usuario(
                usuario["id"],
                usuario["nombre"],
                usuario["usuario"],
                usuario["contraseña"]
            )
            for usuario in usuarios
        ]

        self.productos = [
            Producto(
                producto["id"],
                producto["nombre"],
                producto["precio"],
                producto["cantidad"]
            )
            for producto in productos
        ]

        self.archivo_servicio = archivo_servicio
        self.ruta_productos = ruta_productos
        self.ruta_ventas = ruta_ventas

    # ==========================================================
    # LOGIN
    # ==========================================================

    def validar_usuario(self, usuario, contraseña):
        for u in self.usuarios:
            if u.usuario == usuario and u.contraseña == contraseña:
                return True

        return False

    # ==========================================================
    # USUARIOS
    # ==========================================================

    def listar_usuarios(self):
        return self.usuarios

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    def listar_productos(self):
        return self.productos

    def registrar_producto(self, id, nombre, precio, cantidad):
        for producto in self.productos:
            if str(producto.id) == str(id):
                return False, "El ID del producto ya existe."

        try:
            nuevo_producto = Producto(
                int(id),
                nombre,
                float(precio),
                int(cantidad)
            )
        except ValueError:
            return False, "Los datos ingresados no son válidos."

        self.productos.append(nuevo_producto)
        self.guardar_productos()

        return True, "Producto registrado correctamente."

    def buscar_producto(self, id):
        for producto in self.productos:
            if str(producto.id) == str(id):
                return producto

        return None

    def actualizar_producto(self, id, nombre, precio, cantidad):
        producto = self.buscar_producto(id)

        if producto is None:
            return False, "Producto no encontrado."

        try:
            producto.nombre = nombre
            producto.precio = float(precio)
            producto.cantidad = int(cantidad)
        except ValueError:
            return False, "Los datos ingresados no son válidos."

        self.guardar_productos()

        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, id):
        producto = self.buscar_producto(id)

        if producto is None:
            return False, "Producto no encontrado."

        self.productos.remove(producto)
        self.guardar_productos()

        return True, "Producto eliminado correctamente."

    def guardar_productos(self):
        if (
            self.archivo_servicio is None
            or self.ruta_productos is None
        ):
            return

        datos = []

        for producto in self.productos:
            datos.append({
                "id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad
            })

        self.archivo_servicio.guardar_json(
            self.ruta_productos,
            datos
        )

    # ==========================================================
    # VENTAS - SEMANA 15
    # ==========================================================

    def registrar_venta(self, usuario_id, producto_id):
        usuario_encontrado = None
        producto_encontrado = None

        # Buscar usuario
        for usuario in self.usuarios:
            if str(usuario.id) == str(usuario_id):
                usuario_encontrado = usuario
                break

        # Buscar producto
        for producto in self.productos:
            if str(producto.id) == str(producto_id):
                producto_encontrado = producto
                break

        # Validar usuario
        if usuario_encontrado is None:
            return False, "El usuario seleccionado no existe."

        # Validar producto
        if producto_encontrado is None:
            return False, "El producto seleccionado no existe."

        # Crear fecha
        fecha = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Crear objeto Venta
        nueva_venta = Venta(
            usuario_encontrado.nombre,
            producto_encontrado.nombre,
            fecha
        )

        # Leer ventas existentes
        try:
            ventas = self.archivo_servicio.leer_json(
                self.ruta_ventas
            )
        except (FileNotFoundError, json.JSONDecodeError):
            ventas = []

        # Agregar información adicional para identificar
        # usuario y producto
        venta = nueva_venta.to_dict()

        venta["usuario_id"] = usuario_encontrado.id
        venta["producto_id"] = producto_encontrado.id

        ventas.append(venta)

        # Guardar en ventas.json
        self.archivo_servicio.guardar_json(
            self.ruta_ventas,
            ventas
        )

        return True, "Venta registrada correctamente."

    def listar_ventas(self):
        try:
            return self.archivo_servicio.leer_json(
                self.ruta_ventas
            )
        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):
            return []