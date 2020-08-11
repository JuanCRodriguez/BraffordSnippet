from dominio.cabaña import Cabaña
from dominio.contacto.email import Email
from dominio.contacto.telefono import Telefono


class Establecimiento:

    def __init__(self, nombre, cabaña, renspa, email, telefono, direccion):
        self.id = None
        self.nombre = nombre
        self.cabaña: Cabaña = cabaña
        self.renspa = renspa
        self.email: Email = email
        self.telefono: Telefono = telefono
        self.direccion: direccion = direccion
