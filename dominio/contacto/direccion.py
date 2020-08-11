class Direccion:

    def __init__(self, provincia, localidad, calle, cp,
                 numero_puerta, piso, departamento, oficina,
                 observacion, partido_departamento, tipo_contacto, _num):
        self.id = None
        self.tipo_contacto = tipo_contacto
        self.provincia = provincia
        self.localidad = localidad
        self.calle = calle
        self.cp = cp
        self.numero_puerta = numero_puerta
        self.piso = piso
        self.departamento = departamento
        self.oficina = oficina
        self.observacion = observacion
        self.partido_departamento = partido_departamento
        self.num = _num
