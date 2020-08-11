from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_cuerno.table import TipoCuernoTable
from dominio.producto import Cuerno


@dataclass
class TipoCuernoDataClass(object):
    id: int
    descripcion: str

class TipoCuernoMapper(Mapper):

    def in_(self, o: Cuerno) -> TipoCuernoDataClass:
        return TipoCuernoDataClass(
            id=o.id,
            descripcion=o.tipo
        )

    def out(self, o: TipoCuernoTable) -> TipoCuernoDataClass:
        return TipoCuernoDataClass(
            id=o.id,
            descripcion=o.descripcion
        )