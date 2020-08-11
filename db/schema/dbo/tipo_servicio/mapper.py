from dataclasses import dataclass

from db.base.mapper import Mapper
from db.schema.dbo.tipo_servicio.table import TipoServicioTable
from dominio.servicio import TipoServicio


@dataclass
class TipoServicioDataClass(object):
    id: int
    nombre: str

class TipoServicioMapper(Mapper):

    def in_(self, o: TipoServicio) -> TipoServicioDataClass:
        return TipoServicioDataClass(
            id=o.id,
            nombre=o.nombre
        )

    def out(self, o: TipoServicioTable) -> TipoServicioDataClass:
        return TipoServicioDataClass(
            id=o.id,
            nombre=o.descripcion
        )