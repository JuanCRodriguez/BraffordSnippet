from typing import Union

from pypika import Table
from pypika.terms import Term


class MedicionTable(Table):
    id: Union[int, Term]
    peso_nacimiento: Union[int, Term]
    fecha_pn: Union[str, Term]
    peso_destete: Union[int, Term]
    fecha_pd: Union[str, Term]
    peso_final: Union[int, Term]
    fecha_pf: Union[str, Term]
    ce: Union[int, Term]
    fecha_ce: Union[str, Term]
    alzada: Union[int, Term]
    fecha_alzada: Union[str, Term]
    area_ojo_bife: Union[int, Term]
    fecha_area_ojo_bife: Union[str, Term]
    espesor_grasa_dorsal: Union[int, Term]
    fecha_egd: Union[str, Term]
    id_tipo_denticion: Union[int, Term]
    fecha_denticion: Union[str, Term]
    destete_precoz: Union[int, Term]
    # esto esta tan bastardeado que te das cuenta que estas columnas la hizo una persona diferente a las anteriores
    EspesorGrasaCadera: Union[int, Term]
    FechaEspesorGrasaCadera: Union[str, Term]
    GrasaIntramuscular: Union[int, Term]
    FechaGrasaIntramuscular: Union[str, Term]

    def __init__(self):
        super().__init__('medicion')