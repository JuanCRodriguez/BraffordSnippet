from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_denticion.mapper import TipoDenticionMapper, TipoDenticionDataClass
from db.schema.dbo.tipo_denticion.query import TipoDenticionQueryBuilder
from dominio.producto import Denticion


class TipoDenticionHandler(QueryHandler):
    _o: TipoDenticionDataClass
    _mapper = TipoDenticionMapper()
    _qb = TipoDenticionQueryBuilder()
    results: List[TipoDenticionDataClass]

    def create(self, o: Denticion):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.descripcion)
