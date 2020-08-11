from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.tipo_sexo.mapper import TipoSexoMapper, TipoSexoDataClass
from db.schema.dbo.tipo_sexo.query import TipoSexoQueryBuilder
from dominio.producto import Sexo


class TipoSexoHandler(QueryHandler):
    _o: TipoSexoDataClass
    _mapper = TipoSexoMapper()
    _qb = TipoSexoQueryBuilder()
    results: List[TipoSexoDataClass]

    def create(self, o: Sexo):
        raise Exception("Protected table")

    def with_id(self):
        self._wheres += 1
        self._qb.with_id(self._o.id)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_descripcion(self._o.descripcion)
