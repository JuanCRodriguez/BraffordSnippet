from dominio.cabaña import Cabaña
from dominio.contacto.email import Email


class Usuario:

    def __init__(self, nombre, apellido, username, cabaña, email, rol):
        self.id_sec = None
        self.id_usuario = None
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.cabaña: Cabaña= cabaña
        self.email: Email= email
        self.password = '12345678'
        self.rol = rol
