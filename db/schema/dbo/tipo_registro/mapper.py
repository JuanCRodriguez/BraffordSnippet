from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_registro.table import TipoRegistroTable
from dominio.producto import Registro


@dataclass
class TipoRegistroDataClass(object):
    id: int
    descripcion: str
    orden: int

class TipoRegistroMapper(Mapper):

    def in_(self, o: Registro) -> TipoRegistroDataClass:
        return TipoRegistroDataClass(
            id=o.id,
            descripcion=o.tipo.value,
            orden=o.orden
        )

    def out(self, o: TipoRegistroTable) -> TipoRegistroDataClass:
        return TipoRegistroDataClass(
            id=o.id,
            descripcion=o.descripcion,
            orden=o.orden
        )