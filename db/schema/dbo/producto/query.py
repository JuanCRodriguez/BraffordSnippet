from typing import Union

from pypika import MSSQLQuery

from db.base.query_builder import QueryBuilder
from db.conn.mssql.query import MSSQLQueryBuilder
from db.schema.dbo.producto.mapper import ProductoDataClass
from db.schema.dbo.producto.table import ProductoTable


class ProductoQueryBuilder(QueryBuilder):

    def __init__(self):
        self._table = ProductoTable()
        self._q: Union[MSSQLQuery, MSSQLQueryBuilder] = MSSQLQueryBuilder()

    def insert(self, o: ProductoDataClass):
        self._q.into(self._table) \
            .insert(o.rp,
                    o.nombre,
                    o.apodo,
                    o.tatuaje,
                    o.id_tipo_raza,
                    o.id_tipo_registro,
                    o.id_tipo_color,
                    o.id_tipo_cuerno,
                    o.id_tipo_variedad,
                    o.id_tipo_sexo,
                    o.id_medicion,
                    o.id_dep,
                    o.id_padre,
                    o.id_madre,
                    o.id_receptor,
                    o.importado,
                    o.id_tipo_codigo_importacion,
                    o.codigo_importacion,
                    o.codigo_aba,
                    o.codigo_hba,
                    self._q.to_datetime(o.fecha_nacimiento),
                    o.id_servicio_nacimiento,
                    o.mellizo,
                    self._q.to_datetime(o.fecha_carga),
                    o.activo,
                    o.pendiente_revision,
                    o.id_tipo_parto,
                    o.m1,
                    o.m2,
                    o.id_criador,
                    o.numero_analisis,
                    o.resultado_analisis,
                    o.id_tipo_analisis,
                    o.rp_extranjero,
                    o.hba_extranjero,
                    self._q.to_datetime(o.fecha_actualizacion),
                    o.hba_solicitado,
                    o.fecha_solicitud_hba,
                    o.id_establecimiento_criador,
                    o.fecha_baja,
                    o.fecha_alta_hba,
                    o.observaciones_analisis,
                    o.asociacion,
                    o.nacido_te,
                    o.nro_tramite_sra,
                    o.id_tipo_pompe,
                    o.pendiente_aprobacion_pompe,
                    self._q.to_datetime(o.fecha_resultado_pompe_positivo),
                    o.fecha_cierta,
                    o.id_producto_adicionales,
                    o.hba_enviado_sra,
                    o.toro_dador)
        return self

    def __repr__(self):
        return repr(self._q)
