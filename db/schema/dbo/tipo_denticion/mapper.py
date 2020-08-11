from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_denticion.table import TipoDenticionTable
from dominio.producto import Denticion


@dataclass
class TipoDenticionDataClass(object):
    id: int
    descripcion: str

class TipoDenticionMapper(Mapper):

    def in_(self, o: Denticion) -> TipoDenticionDataClass:
        return TipoDenticionDataClass(
            id=o.id,
            descripcion=o.tipo
        )

    def out(self, o: TipoDenticionTable) -> TipoDenticionDataClass:
        return TipoDenticionDataClass(
            id=o.id,
            descripcion=o.descripcion
        )