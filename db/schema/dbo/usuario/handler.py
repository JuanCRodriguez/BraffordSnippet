from typing import List

from db.base.handler import QueryHandler, Relation
from db.schema.dbo.email.mapper import EmailMapper
from db.schema.dbo.usuario.mapper import UsuarioMapper, UsuarioDataClass
from db.schema.dbo.usuario.query import UsuarioQueryBuilder
from db.schema.dbo.usuario.table import UsuarioEmailRelation
from dominio.usuario import Usuario


class UsuarioHandler(QueryHandler):
    _o: UsuarioDataClass
    _mapper = UsuarioMapper()
    _qb = UsuarioQueryBuilder()
    results: List[UsuarioDataClass]

    def create(self, o: Usuario):
        if not o.id_sec:
            raise Exception()
        return super().create(o)


class UsuarioEmailRelationBuilder(Relation):
    _left_mapper = EmailMapper()
    _right_mapper = UsuarioMapper()
    _table = UsuarioEmailRelation()

