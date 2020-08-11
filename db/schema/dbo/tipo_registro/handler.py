from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_registro.mapper import TipoRegistroMapper, TipoRegistroDataClass
from db.schema.dbo.tipo_registro.query import TipoRegistroQueryBuilder
from dominio.producto import Registro


class TipoRegistroHandler(QueryHandler):
    _o: TipoRegistroDataClass
    _mapper = TipoRegistroMapper()
    _qb = TipoRegistroQueryBuilder()
    results: List[TipoRegistroDataClass]

    def create(self, o: Registro):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.descripcion)
