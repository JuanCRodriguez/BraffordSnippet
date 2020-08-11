from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.mediciones import Mediciones


@dataclass
class MedicionDataClass(object):
    
    id: Any
    peso_nacimiento: int
    fecha_pn: str
    peso_destete: int
    fecha_pd: str
    peso_final: int
    fecha_pf: str
    ce: int
    fecha_ce: str
    alzada: int
    fecha_alzada: str
    area_ojo_bife: int
    fecha_area_ojo_bife: str
    espesor_grasa_dorsal: int
    fecha_egd: str
    id_tipo_denticion: int
    fecha_denticion: str
    destete_precoz: int
    EspesorGrasaCadera: int
    FechaEspesorGrasaCadera: str
    GrasaIntramuscular: int
    FechaGrasaIntramuscular: str

class MedicionMapper(Mapper):

    def in_(self, o: Mediciones) -> MedicionDataClass:
        return MedicionDataClass(
            id=o.id,
            peso_nacimiento= o.nacimiento.medicion,
            fecha_pn= o.nacimiento.fecha,
            peso_destete= o.destete.medicion,
            fecha_pd= o.destete.fecha,
            peso_final= o.final.medicion,
            fecha_pf= o.final.fecha,
            ce= o.ce.medicion,
            fecha_ce= o.ce.fecha,
            alzada= o.alzada.medicion,
            fecha_alzada= o.alzada.fecha,
            area_ojo_bife= o.area_ojo_bife.medicion,
            fecha_area_ojo_bife= o.area_ojo_bife.fecha,
            espesor_grasa_dorsal= o.espesor_grasa_dorsal.medicion,
            fecha_egd= o.espesor_grasa_dorsal.fecha,
            id_tipo_denticion= o.denticion.medicion.id,
            fecha_denticion= o.denticion.fecha,
            destete_precoz= o.destete_precoz,
            EspesorGrasaCadera= o.espesor_grasa_cadera.medicion,
            FechaEspesorGrasaCadera= o.espesor_grasa_cadera.fecha,
            GrasaIntramuscular= o.grasa_intramuscular.medicion,
            FechaGrasaIntramuscular= o.grasa_intramuscular.fecha,
        )