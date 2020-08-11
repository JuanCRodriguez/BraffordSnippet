from typing import Union

from pypika import Table
from pypika.terms import Term


class ProductoTable(Table):
    # ¯\_(ツ)_/¯
    id: Union[int, Term]
    rp: Union[str, Term]
    nombre: Union[str, Term]
    apodo: Union[str, Term]
    tatuaje: Union[str, Term]
    id_tipo_raza: Union[int, Term]
    id_tipo_registro: Union[int, Term]
    id_tipo_color: Union[int, Term]
    id_tipo_cuerno: Union[int, Term]
    id_tipo_variedad: Union[int, Term]
    id_tipo_sexo: Union[int, Term]
    id_medicion: Union[int, Term]
    id_dep: Union[int, Term]
    id_padre: Union[int, Term]
    id_madre: Union[int, Term]
    id_receptor: Union[int, Term]
    importado: Union[int, Term]
    id_tipo_codigo_importacion: Union[int, Term]
    codigo_importacion: Union[str, Term]
    codigo_aba: Union[int, Term]
    codigo_hba: Union[int, Term]
    fecha_nacimiento: Union[str, Term]
    id_servicio_nacimiento: Union[int, Term]
    mellizo: Union[int, Term]
    fecha_carga: Union[int, Term]
    activo: Union[int, Term]
    pendiente_revision: Union[int, Term]
    id_tipo_parto: Union[int, Term]
    m1: Union[int, Term]
    m2: Union[int, Term]
    id_criador: Union[int, Term]
    numero_analisis: Union[str, Term]
    resultado_analisis: Union[str, Term]
    id_tipo_analisis: Union[int, Term]
    rp_extranjero: Union[str, Term]
    hba_extranjero: Union[str, Term]
    fecha_actualizacion: Union[str, Term]
    hba_solicitado: Union[int, Term]
    fecha_solicitud_hba: Union[str, Term]
    id_establecimiento_criador: Union[int, Term]
    fecha_baja: Union[str, Term]
    fecha_alta_hba: Union[str, Term]
    observaciones_analisis: Union[str, Term]
    asociacion: Union[str, Term]
    nacido_te: Union[int, Term]
    nro_tramite_sra: Union[int, Term]
    id_tipo_pompe: Union[int, Union[int, Term]]
    pendiente_aprobacion_pompe: Union[int, Term]
    fecha_resultado_pompe_positivo: Union[str, Term]
    fecha_cierta: Union[int, Term]
    id_producto_adicionales: Union[int, Term]
    hba_enviado_sra: Union[int, Term]
    toro_dador: Union[int, Term]

    def __init__(self):
        super().__init__("producto")

class ProductoEstablecimientoRelation(Table):
    id_producto: Union[int, Term]
    id_establecimiento: Union[int, Term]

    def __init__(self):
        super().__init__('producto_establecimiento')

class ProductoCabañaRelation(Table):
    id_cabania: Union[int, Term]
    id_producto: Union[int, Term]

    def __init__(self):
        super().__init__('producto_cabania')