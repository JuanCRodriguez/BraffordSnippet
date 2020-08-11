from datetime import datetime


class Cabaña:

    def __init__(self, nombre, prefijo_macho, prefijo_hembra, productor, numero):
        self.id = None
        self.activa = True
        self.nombre = nombre
        self.prefijo_macho = prefijo_macho
        self.prefijo_hembra = prefijo_hembra
        self.productor = productor
        self.numero = numero
        self.fecha_inicio_actividad = datetime.now()
        self.establecimientos = []
        self.telefonos = []
        self.emails = []
        self.direcciones = []
        self._establecimiento_activo = None

    @property
    def establecimiento_default(self):
        return self._establecimiento_activo

    @establecimiento_default.setter
    def establecimiento_default(self, val):
        if val not in self.establecimientos:
            raise Exception("El establecimiento no se encuentra entre los de esta cabaña")
        self._establecimiento_activo = val
