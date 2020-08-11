from typing import Union

from pypika import Table, MSSQLQuery

from db.conn.mssql.query import MSSQLQueryBuilder


class QueryBuilder:

    _q: Union[MSSQLQuery, MSSQLQueryBuilder]

    def select(self): ...

    def insert(self, o): ...

    def reset(self):
        self.__init__()

    def __repr__(self):
        return repr(self._q)


class RelationQueryBuilder:

    def __init__(self, table: Table):
        self._table = table
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, l, r):
        self._q.into(self._table).insert(l, r)
        return self

    def __repr__(self):
        return repr(self._q)