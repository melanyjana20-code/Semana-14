from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self, usuarios, productos, archivo_servicio=None, ruta_productos=None):
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

    def validar_usuario(self, usuario, contraseña):
        for u in self.usuarios:
            if u.usuario == usuario and u.contraseña == contraseña:
                return True
        return False

    def listar_usuarios(self):
        return self.usuarios

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
        if self.archivo_servicio is None or self.ruta_productos is None:
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