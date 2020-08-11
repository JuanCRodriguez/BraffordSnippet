from dataclasses import dataclass
from typing import Optional

from db.base.mapper import Mapper
from dominio.servicio import MachoEnServicio


@dataclass
class MachosEnServicioDataClass(object):
    id: Optional[int]
    servicioid: int
    machoid: int
    semenid: Optional[int]
    cantidadsemen: Optional[int]
    desestimado: Optional[int]
    adn: Optional[int]


class MachosEnServicioMapper(Mapper):

    def in_(self, o: MachoEnServicio) -> MachosEnServicioDataClass:
        return MachosEnServicioDataClass(
            id=o.id,
            servicioid=o.servicio.id,
            machoid=o.macho.id,
            semenid=o.semen_id,
            cantidadsemen=o.cantidad_semen,
            desestimado=o.desestimado,
            adn=o.adn
            )
