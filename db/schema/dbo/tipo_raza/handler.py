from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_raza.mapper import TipoRazaMapper, TipoRazaDataClass
from db.schema.dbo.tipo_raza.query import TipoRazaQueryBuilder
from dominio.producto import Raza


class TipoRazaHandler(QueryHandler):
    _o: TipoRazaDataClass
    _mapper = TipoRazaMapper()
    _qb = TipoRazaQueryBuilder()
    results: List[TipoRazaDataClass]

    def create(self, o: Raza):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.descripcion)
