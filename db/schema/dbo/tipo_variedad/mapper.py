from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_variedad.table import TipoVariedadTable
from dominio.producto import Variedad


@dataclass
class TipoVariedadDataClass(object):
    id: int
    descripcion: str

class TipoVariedadMapper(Mapper):

    def in_(self, o: Variedad) -> TipoVariedadDataClass:
        return TipoVariedadDataClass(
            id=o.id,
            descripcion=o.tipo
        )

    def out(self, o: TipoVariedadTable) -> TipoVariedadDataClass:
        return TipoVariedadDataClass(
            id=o.id,
            descripcion=o.descripcion
        )