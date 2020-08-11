from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.sec_profile.mapper import SecProfileDataClass
from db.schema.dbo.sec_profile.table import SecProfileTable


class SecProfileQueryBuilder(QueryBuilder):

    def __init__(self):
        super().__init__()
        self._table = SecProfileTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: SecProfileDataClass):
        self._q.into(self._table).insert(o.id_profile, o.name)
        return self

    def select(self):
        self._q.from_(self._table).select(self._table.id_profile, self._table.name)

    def with_id_profile(self, id_):
        self._q.where(self._table.id_profile == id_)

    def with_name(self, name):
        self._q.where(self._table.name == name)

    def __repr__(self):
        return repr(self._q)
