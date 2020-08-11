from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from db.base.mapper import Mapper
from dominio.servicio import Servicio


@dataclass
class ServicioDataClass(object):
    id: int
    cantidad_embrion: int
    cantidad_machos_sin_registrar: int
    cantidad_hembras_sin_registrar: int
    numero_termo: int
    id_tipo_servicio: int
    fecha_inicio: datetime
    fecha_fin: datetime
    id_embrion: int
    fecha_carga: datetime
    id_cabania: int
    pendiente_aprobacion: int
    limita_registro: int
    cantidad_hembras_sin_registrar_no_bo: int
    id_transferencia: int
    estado_servicio: int
    cantidad_machos_sin_registrar_otras_razas: int
    cantidad_hembras_sin_registrar_otras_razas: int
    fecha_modificacion: Optional[datetime]

class ServicioMapper(Mapper):

    def in_(self, o: Servicio) -> ServicioDataClass:
        return ServicioDataClass(
            id=o.id,
            cantidad_embrion=0,
            cantidad_machos_sin_registrar=o.cantidad_machos_sin_registrar(),
            cantidad_hembras_sin_registrar=o.cantidad_hembras_sin_registrar(),
            numero_termo=0,
            id_tipo_servicio=o.tipo.id,
            fecha_inicio=o.fecha_inicio,
            fecha_fin=o.fecha_fin,
            id_embrion=o.embrion.id if o.embrion else None,
            fecha_carga=o.fecha_carga,
            id_cabania=o.cabaña.id,
            pendiente_aprobacion=int(o.pendiente_aprobacion),
            limita_registro=int(o.limita_registro),
            cantidad_hembras_sin_registrar_no_bo=o.cantidad_hembras_sin_registrar_no_bo(),
            id_transferencia=o.transferencia.id if o.transferencia else None,
            estado_servicio=o.estado,
            cantidad_machos_sin_registrar_otras_razas=o.cantidad_machos_sin_registrar_otras_razas(),
            cantidad_hembras_sin_registrar_otras_razas=o.cantidad_hembras_sin_registrar_otras_razas(),
            fecha_modificacion=o.fecha_carga
        )
