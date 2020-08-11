from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.direccion.mapper import DireccionDataClass
from db.schema.dbo.direccion.table import DireccionTable


class DireccionQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = DireccionTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: DireccionDataClass):
        self._q.into(self._table) \
            .insert(o.id_tipo_contacto,
                    o.id_provincia,
                    o.localidad,
                    o.calle,
                    o.cp,
                    o.numero_puerta,
                    o.piso,
                    o.oficina,
                    o.departamento,
                    o.observacion,
                    o._num,
                    o.partido_departamento
                    )
        return self

    def __repr__(self):
        return repr(self._q)
