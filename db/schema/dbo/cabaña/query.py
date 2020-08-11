from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.cabaña.mapper import CabañaDataClass
from db.schema.dbo.cabaña.table import CabañaTable


class CabañaQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = CabañaTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: CabañaDataClass):
        self._q.into(self._table) \
            .insert(o.nombre,
                    o.prefijo_macho,
                    o.prefijo_hembra,
                    o.id_persona_juridica,
                    o.numero,
                    o.id_establecimiento_defecto,
                    o.activa,
                    self._q.to_datetime(o.fecha_inicio_actividad))
        return self

    def __repr__(self):
        return repr(self._q)
