from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.producto import Producto


@dataclass
class ProductoDataClass(object):
    id: Any
    rp: str
    nombre: str
    apodo: Any
    tatuaje: Any
    id_tipo_raza: int
    id_tipo_registro: int
    id_tipo_color: int
    id_tipo_cuerno: int
    id_tipo_variedad: int
    id_tipo_sexo: int
    id_medicion: int
    id_dep: Any
    id_padre: Any
    id_madre: Any
    id_receptor: Any
    importado: int
    id_tipo_codigo_importacion: Any
    codigo_importacion: Any
    codigo_aba: int
    codigo_hba: Any
    fecha_nacimiento: str
    id_servicio_nacimiento: Any
    mellizo: int
    fecha_carga: int
    activo: int
    pendiente_revision: int
    id_tipo_parto: int
    m1: Any
    m2: Any
    id_criador: int
    numero_analisis: Any
    resultado_analisis: Any
    id_tipo_analisis: Any
    rp_extranjero: Any
    hba_extranjero: Any
    fecha_actualizacion: Any
    hba_solicitado: int
    fecha_solicitud_hba: Any
    id_establecimiento_criador: int
    fecha_baja: Any
    fecha_alta_hba: Any
    observaciones_analisis: Any
    asociacion: Any
    nacido_te: int
    nro_tramite_sra: Any
    id_tipo_pompe: int
    pendiente_aprobacion_pompe: int
    fecha_resultado_pompe_positivo: Any
    fecha_cierta: int
    id_producto_adicionales: Any
    hba_enviado_sra: int
    toro_dador: int
    
class ProductoMapper(Mapper):
    
    def in_(self, o: Producto) -> ProductoDataClass:
        return ProductoDataClass(
            id= o.id,
            rp= o.rp,
            nombre= o.nombre,
            apodo= o.apodo,
            tatuaje= o.tatuaje,
            id_tipo_raza= o.raza.id,
            id_tipo_registro= o.registro.id,
            id_tipo_color= o.color.id,
            id_tipo_cuerno= o.cuerno.id if o.cuerno else None,
            id_tipo_variedad= o.variedad.id,
            id_tipo_sexo= o.sexo.id,
            id_medicion= o.medicion.id,
            id_dep= o.dep.id if o.dep else None,
            id_padre= o.padre.id if o.padre else None,
            id_madre= o.madre.id if o.madre else None,
            id_receptor= None,
            importado= 0,
            id_tipo_codigo_importacion= None,
            codigo_importacion= None,
            codigo_aba= o.codigo_aba,
            codigo_hba= o.codigo_hba,
            fecha_nacimiento= o.fecha_nacimiento,
            id_servicio_nacimiento= o.servicio_nacimiento.id if o.servicio_nacimiento else None,
            mellizo= 0,
            fecha_carga= o.fecha_carga,
            activo= 1,
            pendiente_revision= 0,
            id_tipo_parto= o.tipo_parto.id,
            m1= None,
            m2= None,
            id_criador= o.establecimiento.cabaña.id,
            numero_analisis= None,
            resultado_analisis= None,
            id_tipo_analisis= None,
            rp_extranjero= None,
            hba_extranjero= None,
            fecha_actualizacion= None,
            hba_solicitado= 0,
            fecha_solicitud_hba= None,
            id_establecimiento_criador= o.establecimiento.id,
            fecha_baja= None,
            fecha_alta_hba= None,
            observaciones_analisis= None,
            asociacion= None,
            nacido_te= 0,
            nro_tramite_sra= None,
            id_tipo_pompe= o.pompe.id,
            pendiente_aprobacion_pompe= 0,
            fecha_resultado_pompe_positivo= None,
            fecha_cierta= 1,
            id_producto_adicionales= None,
            hba_enviado_sra= 0,
            toro_dador= 0,
        )