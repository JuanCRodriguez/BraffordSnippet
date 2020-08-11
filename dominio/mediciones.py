from dataclasses import dataclass
from datetime import datetime
from typing import Union, Any


class Mediciones:

    def __init__(self, peso_nac, fecha_nac,
                 peso_destete, fecha_destete,
                 peso_final, fecha_final,
                 circunferencia_escrotal, fecha_circunferencia_escrotal,
                 alzada, fecha_alzada,
                 area_ojo_bife, fecha_area_ojo_bife,
                 espesor_grasa_dorsal, fecha_egd,
                 denticion, fecha_denticion,
                 destete_precoz, espesor_grasa_cadera,
                 fecha_espesor_grasa_cadera, grasa_intramuscular,
                 fecha_grasa_intramuscular):
        self.id = None
        self.nacimiento = Medicion(peso_nac, fecha_nac)
        self.destete = Medicion(peso_destete, fecha_destete)
        self.final = Medicion(peso_final, fecha_final)
        self.ce = Medicion(circunferencia_escrotal, fecha_circunferencia_escrotal)
        self.alzada = Medicion(alzada, fecha_alzada)
        self.area_ojo_bife = Medicion(area_ojo_bife, fecha_area_ojo_bife)
        self.espesor_grasa_dorsal = Medicion(espesor_grasa_dorsal, fecha_egd)
        self.espesor_grasa_cadera = Medicion(espesor_grasa_cadera, fecha_espesor_grasa_cadera)
        self.fecha_espesor_grasa_cadera = fecha_espesor_grasa_cadera
        self.denticion = Medicion(denticion, fecha_denticion)
        self.grasa_intramuscular = Medicion(grasa_intramuscular, fecha_grasa_intramuscular)
        self.destete_precoz = destete_precoz

@dataclass
class Medicion:
    medicion: Any
    fecha: Union[None, datetime]
