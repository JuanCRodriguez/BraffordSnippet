from typing import Any

from pypika import Table


class DireccionTable(Table):
    id: int
    id_tipo_contacto: Any
    id_provincia: int
    localidad: str
    calle: str
    cp: str
    numero_puerta: str
    piso: str
    departamento: str
    oficina: str
    observacion: str
    _num: Any
    partido_departamento: str

    def __init__(self):
        super().__init__('direccion')
