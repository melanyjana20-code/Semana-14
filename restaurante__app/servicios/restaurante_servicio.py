from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:

    def __init__(self, usuarios, productos):
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

    def validar_usuario(self, usuario, contraseña):
        for u in self.usuarios:
            if u.usuario == usuario and u.contraseña == contraseña:
                return True
        return False

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos