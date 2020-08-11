from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.email.mapper import EmailDataClass
from db.schema.dbo.email.table import EmailTable


class EmailQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = EmailTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: EmailDataClass):
        self._q.into(self._table) \
            .insert(o.cuenta,
                    o.observacion,
                    o.contacto,
                    o.id_tipo_contacto,
                    o.verificada,
                    o.email_token
                    )
        return self

    def __repr__(self):
        return repr(self._q)
