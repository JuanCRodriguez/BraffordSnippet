from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.sec_user.mapper import SecUserDataClass
from db.schema.dbo.sec_user.table import SecUserTable


class SecUserQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = SecUserTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: SecUserDataClass):
        self._q.into(self._table) \
            .insert(o.name,
                    o.pass_,
                    o.pass1)
        return self

    def __repr__(self):
        return repr(self._q)
