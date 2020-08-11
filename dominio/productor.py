from datetime import datetime


class Productor:

    def __init__(self, razon_social, cuit, numero_socio, observacion):
        self.id = None
        self.razon_social = razon_social
        self.cuit = cuit
        self.numero_socio = numero_socio
        self.web = "quecornoesesto"
        self.observacion = observacion
        self.activo = True
        self.fecha_inicio_actividad = datetime.now()
        self.direcciones = []
        self.telefonos = []
        self.emails = []
        self.establecimientos = []