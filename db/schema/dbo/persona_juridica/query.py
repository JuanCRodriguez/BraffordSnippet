from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.persona_juridica.mapper import PersonaJuridicaDataClass
from db.schema.dbo.persona_juridica.table import PersonaJuridicaTable


class PersonaJuridicaQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = PersonaJuridicaTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: PersonaJuridicaDataClass):
        self._q.into(self._table) \
            .insert(o.razon_social,
                    o.observacion,
                    o.cuit,
                    o.num_socio,
                    o.web,
                    o.activo,
                    self._q.to_datetime(o.fecha_inicio_actividad))
        return self

    def __repr__(self):
        return repr(self._q)
