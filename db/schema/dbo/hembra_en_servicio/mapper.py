from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from db.base.mapper import Mapper
from dominio.servicio import HembraEnServicio


@dataclass
class HembraEnServicioDataClass(object):
    id: Optional[int]
    id_hembra: int
    id_servicio: int
    fecha: datetime
    desestimado: int
    cantidadEmbrion: Optional[int]


class HembraEnServicioMapper(Mapper):

    def in_(self, o: HembraEnServicio) -> HembraEnServicioDataClass:
        return HembraEnServicioDataClass(
            id=o.id,
            id_hembra=o.hembra.id,
            id_servicio=o.servicio.id,
            fecha=o.fecha,
            desestimado=o.desestimado,
            cantidadEmbrion=0 #por el momento no se usa
            )
