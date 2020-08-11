from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.productor import Productor


@dataclass
class PersonaJuridicaDataClass(object):
    id: Any
    razon_social: str
    observacion: str
    cuit: str
    num_socio: str
    web: str
    activo: int
    fecha_inicio_actividad: str


class PersonaJuridicaMapper(Mapper):

    def in_(self, o: Productor) -> PersonaJuridicaDataClass:
        return PersonaJuridicaDataClass(
            id=o.id,
            razon_social=o.razon_social,
            observacion=o.observacion,
            cuit=o.cuit,
            num_socio=o.numero_socio,
            web=o.web,
            activo=int(o.activo),
            fecha_inicio_actividad= o.fecha_inicio_actividad
        )

