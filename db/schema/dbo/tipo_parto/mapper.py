from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_parto.table import TipoPartoTable
from dominio.producto import Parto


@dataclass
class TipoPartoDataClass(object):
    id: int
    descripcion: str

class TipoPartoMapper(Mapper):

    def in_(self, o: Parto) -> TipoPartoDataClass:
        return TipoPartoDataClass(
            id=o.id,
            descripcion=o.tipo
        )

    def out(self, o: TipoPartoTable) -> TipoPartoDataClass:
        return TipoPartoDataClass(
            id=o.id,
            descripcion=o.descripcion
        )