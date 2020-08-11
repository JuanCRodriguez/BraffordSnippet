from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.establecimiento.mapper import EstablecimientoDataClass
from db.schema.dbo.establecimiento.table import EstablecimientoTable


class EstablecimientoQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = EstablecimientoTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: EstablecimientoDataClass):
        self._q.into(self._table) \
            .insert(o.nombre,
                    o.id_cabania,
                    o.renspa)
        return self

    def __repr__(self):
        return repr(self._q)
