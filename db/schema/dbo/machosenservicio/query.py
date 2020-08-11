from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.machosenservicio.mapper import MachosEnServicioDataClass
from db.schema.dbo.machosenservicio.table import MachosEnServicioTable


class MachosEnServicioQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = MachosEnServicioTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: MachosEnServicioDataClass):
        self._q.into(self._table) \
            .insert(
                    o.servicioid,
                    o.machoid,
                    o.semenid,
                    o.cantidadsemen,
                    int(o.desestimado),
                    o.adn)
        return self

    def __repr__(self):
        return repr(self._q)
