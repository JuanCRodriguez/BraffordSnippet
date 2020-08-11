from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_raza.table import TipoRazaTable
from dominio.producto import Raza


@dataclass
class TipoRazaDataClass(object):
    id: int
    descripcion: str

class TipoRazaMapper(Mapper):

    def in_(self, o: Raza) -> TipoRazaDataClass:
        return TipoRazaDataClass(
            id=o.id,
            descripcion=o.nombre
        )

    def out(self, o: TipoRazaTable) -> TipoRazaDataClass:
        return TipoRazaDataClass(
            id=o.id,
            descripcion=o.descripcion
        )