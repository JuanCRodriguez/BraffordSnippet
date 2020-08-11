from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_servicio.mapper import TipoServicioMapper, TipoServicioDataClass
from db.schema.dbo.tipo_servicio.query import TipoServicioQueryBuilder
from dominio.servicio import TipoServicio


class TipoServicioHandler(QueryHandler):
    _o: TipoServicioDataClass
    _mapper = TipoServicioMapper()
    _qb = TipoServicioQueryBuilder()
    results: List[TipoServicioDataClass]

    def create(self, o: TipoServicio):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_nombre(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.nombre)
