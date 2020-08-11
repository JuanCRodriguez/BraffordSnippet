from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_color.table import TipoColorTable
from dominio.producto import Color


@dataclass
class TipoColorDataClass(object):
    id: int
    nombre: str

class TipoColorMapper(Mapper):

    def in_(self, o: Color) -> TipoColorDataClass:
        return TipoColorDataClass(
            id=o.id,
            nombre=o.nombre
        )

    def out(self, o: TipoColorTable) -> TipoColorDataClass:
        return TipoColorDataClass(
            id=o.id,
            nombre=o.descripcion
        )