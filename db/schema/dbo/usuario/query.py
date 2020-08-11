from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.usuario.mapper import UsuarioDataClass
from db.schema.dbo.usuario.table import UsuarioTable


class UsuarioQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = UsuarioTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: UsuarioDataClass):
        self._q.into(self._table) \
            .insert(
            o.id_user,
            o.nombre,
            o.apellido,
            o.id_cabania,
            o.habilitado_voto,
            o.activo
        )
        return self

    def __repr__(self):
        return repr(self._q)
