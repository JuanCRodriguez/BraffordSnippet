from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_parto.mapper import TipoPartoMapper, TipoPartoDataClass
from db.schema.dbo.tipo_parto.query import TipoPartoQueryBuilder
from dominio.producto import Parto


class TipoPartoHandler(QueryHandler):
    _o: TipoPartoDataClass
    _mapper = TipoPartoMapper()
    _qb = TipoPartoQueryBuilder()
    results: List[TipoPartoDataClass]

    def create(self, o: Parto):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.descripcion)
