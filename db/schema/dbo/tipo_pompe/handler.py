from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_pompe.mapper import TipoPompeMapper, TipoPompeDataClass
from db.schema.dbo.tipo_pompe.query import TipoPompeQueryBuilder
from dominio.producto import Pompe


class TipoPompeHandler(QueryHandler):
    _o: TipoPompeDataClass
    _mapper = TipoPompeMapper()
    _qb = TipoPompeQueryBuilder()
    results: List[TipoPompeDataClass]

    def create(self, o: Pompe):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.descripcion)
