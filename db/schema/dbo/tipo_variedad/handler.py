from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_variedad.mapper import TipoVariedadMapper, TipoVariedadDataClass
from db.schema.dbo.tipo_variedad.query import TipoVariedadQueryBuilder
from dominio.producto import Variedad


class TipoVariedadHandler(QueryHandler):
    _o: TipoVariedadDataClass
    _mapper = TipoVariedadMapper()
    _qb = TipoVariedadQueryBuilder()
    results: List[TipoVariedadDataClass]

    def create(self, o: Variedad):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.descripcion)
