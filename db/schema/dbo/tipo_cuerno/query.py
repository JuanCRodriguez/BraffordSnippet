from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.tipo_cuerno.mapper import TipoCuernoDataClass
from db.schema.dbo.tipo_cuerno.table import TipoCuernoTable


class TipoCuernoQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = TipoCuernoTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: TipoCuernoDataClass):
        self._q.into(self._table).insert(o.id, o.descripcion)
        return self

    def select(self):
        self._q.from_(self._table).select(self._table.id, self._table.descripcion)

    def with_id(self, id_):
        self._q.where(self._table.id == id_)

    def with_descripcion(self, desc):
        self._q.where(self._table.descripcion == desc)

    def __repr__(self):
        return repr(self._q)
