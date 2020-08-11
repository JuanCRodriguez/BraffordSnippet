from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.cabaña import Cabaña


@dataclass
class CabañaDataClass(object):
    id: Any
    nombre: str
    prefijo_macho: str
    prefijo_hembra: str
    id_persona_juridica: Any
    numero: int
    id_establecimiento_defecto: Any
    activa: int
    fecha_inicio_actividad: str

class CabañaMapper(Mapper):

    def in_(self, o: Cabaña) -> CabañaDataClass:
        return CabañaDataClass(
            id=o.id,
            nombre=o.nombre,
            prefijo_macho=o.prefijo_macho,
            prefijo_hembra=o.prefijo_hembra,
            id_persona_juridica=o.productor.id,
            numero=o.numero,
            id_establecimiento_defecto=o.establecimiento_default,
            activa= int(o.activa),
            fecha_inicio_actividad= o.fecha_inicio_actividad
        )
