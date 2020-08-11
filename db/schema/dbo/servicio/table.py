from typing import Union

from pypika import Table
from pypika.terms import Term


class ServicioTable(Table):
    id: Union[int, Term]
    cantidad_embrion: Union[int, Term]
    cantidad_machos_sin_registrar: Union[int, Term]
    cantidad_hembras_sin_registrar: Union[int, Term]
    numero_termo: Union[int, Term]
    id_tipo_servicio: Union[int, Term]
    fecha_inicio: Union[str, Term]
    fecha_fin: Union[str, Term]
    id_embrion: Union[int, Term]
    fecha_carga: Union[str, Term]
    id_cabania: Union[int, Term]
    pendiente_aprobacion: Union[int, Term]
    limita_registro: Union[int, Term]
    cantidad_hembras_sin_registrar_no_bo: Union[int, Term]
    id_transferencia: Union[int, Term]
    estado_servicio: Union[int, Term]
    cantidad_machos_sin_registrar_otras_razas: Union[int, Term]
    cantidad_hembras_sin_registrar_otras_razas: Union[int, Term]
    fecha_modificacion: Union[str, Term]

    def __init__(self):
        super().__init__('servicio')

