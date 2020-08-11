from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_pompe.table import TipoPompeTable
from dominio.producto import Pompe


@dataclass
class TipoPompeDataClass(object):
    id: int
    descripcion: str

class TipoPompeMapper(Mapper):

    def in_(self, o: Pompe) -> TipoPompeDataClass:
        return TipoPompeDataClass(
            id=o.id,
            descripcion=o.resultado
        )

    def out(self, o: TipoPompeTable) -> TipoPompeDataClass:
        return TipoPompeDataClass(
            id=o.id,
            descripcion=o.descripcion
        )