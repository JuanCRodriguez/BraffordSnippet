from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.servicio.mapper import ServicioDataClass
from db.schema.dbo.servicio.table import ServicioTable


class ServicioQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = ServicioTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: ServicioDataClass):
        self._q.into(self._table) \
            .insert(o.cantidad_embrion,
                    o.cantidad_machos_sin_registrar,
                    o.cantidad_hembras_sin_registrar,
                    o.numero_termo,
                    o.id_tipo_servicio,
                    self._q.to_datetime(o.fecha_inicio),
                    self._q.to_datetime(o.fecha_fin),
                    o.id_embrion,
                    self._q.to_datetime(o.fecha_carga),
                    o.id_cabania,
                    o.pendiente_aprobacion,
                    o.limita_registro,
                    o.cantidad_hembras_sin_registrar_no_bo,
                    o.id_transferencia,
                    o.estado_servicio,
                    o.cantidad_machos_sin_registrar_otras_razas,
                    o.cantidad_hembras_sin_registrar_otras_razas,
                    self._q.to_datetime(o.fecha_modificacion)
                    )
        return self

    def __repr__(self):
        return repr(self._q)
