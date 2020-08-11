from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_sexo.table import TipoSexoTable
from dominio.producto import Sexo


@dataclass
class TipoSexoDataClass(object):
    id: int
    descripcion: str

class TipoSexoMapper(Mapper):

    def in_(self, o: Sexo) -> TipoSexoDataClass:
        return TipoSexoDataClass(
            id=o.id,
            descripcion=o.nombre
        )

    def out(self, o: TipoSexoTable) -> TipoSexoDataClass:
        return TipoSexoDataClass(
            id=o.id,
            descripcion=o.descripcion
        )