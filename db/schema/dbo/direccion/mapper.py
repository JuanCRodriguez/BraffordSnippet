from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.contacto.direccion import Direccion


@dataclass
class DireccionDataClass(object):
    id: Any
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

class DireccionMapper(Mapper):

    def in_(self, o: Direccion) -> DireccionDataClass:
        return DireccionDataClass(
            id=o.id,
            id_tipo_contacto= o.tipo_contacto.id if o.tipo_contacto else None,
            id_provincia=o.provincia.id,
            localidad=o.localidad,
            calle=o.calle,
            cp=o.cp,
            numero_puerta=o.numero_puerta,
            piso=o.piso,
            oficina=o.oficina,
            departamento=o.departamento,
            observacion=o.observacion,
            _num=o.num,
            partido_departamento=o.partido_departamento
        )
