from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_cuerno.mapper import TipoCuernoMapper, TipoCuernoDataClass
from db.schema.dbo.tipo_cuerno.query import TipoCuernoQueryBuilder
from dominio.producto import Cuerno


class TipoCuernoHandler(QueryHandler):
    _o: TipoCuernoDataClass
    _mapper = TipoCuernoMapper()
    _qb = TipoCuernoQueryBuilder()
    results: List[TipoCuernoDataClass]

    def create(self, o: Cuerno):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.descripcion)
