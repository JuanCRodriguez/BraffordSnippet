from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.hembra_en_servicio.mapper import HembraEnServicioDataClass
from db.schema.dbo.hembra_en_servicio.table import HembraEnServicioTable


class HembraEnServicioQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = HembraEnServicioTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: HembraEnServicioDataClass):
        self._q.into(self._table) \
            .insert(
                    o.id_hembra,
                    o.id_servicio,
                    self._q.to_datetime(o.fecha),
                    int(o.desestimado),
                    o.cantidadEmbrion)
        return self

    def __repr__(self):
        return repr(self._q)
