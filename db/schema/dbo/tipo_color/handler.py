from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_color.mapper import TipoColorMapper, TipoColorDataClass
from db.schema.dbo.tipo_color.query import TipoColorQueryBuilder
from dominio.producto import Color


class TipoColorHandler(QueryHandler):
    _o: TipoColorDataClass
    _mapper = TipoColorMapper()
    _qb = TipoColorQueryBuilder()
    results: List[TipoColorDataClass]

    def create(self, o: Color):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_nombre(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.nombre)
