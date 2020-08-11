
class Telefono:

    def __init__(self, codigo_pais, codigo_interurbano, numero, interno,
                 observacion, tipo_contacto, tipo_telefono):
        self.id = None
        self.codigo_pais = codigo_pais
        self.codigo_interurbano = codigo_interurbano
        self.numero = numero
        self.interno = interno
        self.observacion = observacion
        self.tipo_contacto = tipo_contacto
        self.tipo_telefono = tipo_telefono