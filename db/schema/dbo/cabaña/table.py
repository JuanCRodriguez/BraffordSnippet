from typing import Any, Union

from pypika import Table
from pypika.terms import Term


class CabañaTable(Table):
    id: Union[int, Term]
    nombre: Union[str, Term]
    prefijo_macho: Union[str, Term]
    prefijo_hembra: Union[str, Term]
    id_persona_juridica: Union[Any, Term]
    numero: Union[int, Term]
    id_establecimiento_defecto: Union[Any, Term]
    activa: Union[int, Term]
    fecha_inicio_actividad: Union[str, Term]

    def __init__(self):
        super().__init__('cabania')


class CabañaEmailRelation(Table):
    id_email: Union[int, Term]
    id_cabania: Union[int, Term]

    def __init__(self):
        super().__init__('cabania_email')


class CabañaDireccionRelation(Table):
    id_direccion: Union[int, Term]
    id_cabania: Union[int, Term]

    def __init__(self):
        super().__init__('cabania_direccion')


class CabañaTelefonoRelation(Table):
    id_telefono: Union[int, Term]
    id_cabania: Union[int, Term]

    def __init__(self):
        super().__init__('cabania_telefono')
