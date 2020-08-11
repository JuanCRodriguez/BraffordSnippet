from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.medicion.mapper import MedicionDataClass
from db.schema.dbo.medicion.table import MedicionTable


class MedicionQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = MedicionTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: MedicionDataClass):
        self._q.into(self._table) \
            .insert(o.peso_nacimiento,
                    self._q.to_datetime(o.fecha_pn),
                    o.peso_destete,
                    self._q.to_datetime(o.fecha_pd),
                    o.peso_final,
                    self._q.to_datetime(o.fecha_pf),
                    o.ce,
                    self._q.to_datetime(o.fecha_ce),
                    o.alzada,
                    self._q.to_datetime(o.fecha_alzada),
                    o.area_ojo_bife,
                    self._q.to_datetime(o.fecha_area_ojo_bife),
                    o.espesor_grasa_dorsal,
                    self._q.to_datetime(o.fecha_egd),
                    o.id_tipo_denticion,
                    self._q.to_datetime(o.fecha_denticion),
                    o.destete_precoz,
                    o.EspesorGrasaCadera,
                    self._q.to_datetime(o.FechaEspesorGrasaCadera),
                    o.GrasaIntramuscular,
                    self._q.to_datetime(o.FechaGrasaIntramuscular)),
        return self

    def __repr__(self):
        return repr(self._q)
