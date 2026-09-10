class Usuario:
    def __init__(self, id, nombre, usuario, contraseña):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña

    def __str__(self):
        return f"{self.nombre} - Usuario: {self.usuario}"