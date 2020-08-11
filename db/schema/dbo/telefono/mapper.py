from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.contacto.telefono import Telefono


@dataclass
class TelefonoDataClass(object):
    id: Any
    codigo_pais: str
    codigo_interurbano: str
    numero: str
    interno: str
    observacion: str
    id_tipo_contacto: int
    id_tipo_telefono: int


class TelefonoMapper(Mapper):

    def in_(self, o: Telefono) -> TelefonoDataClass:
        return TelefonoDataClass(
            id=o.id,
            codigo_pais=o.codigo_pais,
            codigo_interurbano=o.codigo_interurbano,
            numero=o.numero,
            interno=o.interno,
            observacion=o.observacion,
            id_tipo_telefono=o.tipo_telefono.id if o.tipo_telefono else None,
            id_tipo_contacto=o.tipo_contacto.id if o.tipo_contacto else None,
        )
