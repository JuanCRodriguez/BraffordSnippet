from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.telefono.mapper import TelefonoDataClass
from db.schema.dbo.telefono.table import TelefonoTable


class TelefonoQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = TelefonoTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: TelefonoDataClass):
        self._q.into(self._table) \
            .insert(o.codigo_pais,
                    o.codigo_interurbano,
                    o.numero,
                    o.interno,
                    o.observacion,
                    o.id_tipo_contacto,
                    o.id_tipo_telefono)
        return self

    def __repr__(self):
        return repr(self._q)
