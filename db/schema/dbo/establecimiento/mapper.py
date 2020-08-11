from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.establecimiento import Establecimiento


@dataclass
class EstablecimientoDataClass(object):
    id: Any
    nombre: str
    id_cabania: int
    renspa: str


class EstablecimientoMapper(Mapper):

    def in_(self, o: Establecimiento) -> EstablecimientoDataClass:
        return EstablecimientoDataClass(
            id=o.id,
            nombre=o.nombre,
            id_cabania=o.cabaña.id,
            renspa=o.renspa,
            )
