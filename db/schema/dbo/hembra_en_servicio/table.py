from typing import Union, Optional

from pypika import Table
from pypika.terms import Term


class HembraEnServicioTable(Table):
    id: Union[int, Term]
    id_hembra: Union[int, Term]
    id_servicio: Union[int, Term]
    fecha: Union[str, Term]
    desestimado: Union[int, Term]
    cantidadEmrion: Union[Optional[int], Term]

    def __init__(self):
        super().__init__('hembra_en_servicio')
