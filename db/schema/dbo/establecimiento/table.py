from typing import Union

from pypika import Table
from pypika.terms import Term


class EstablecimientoTable(Table):
    id: Union[int, Term]
    nombre: Union[str, Term]
    id_cabania: Union[int, Term]
    renspa: Union[str, Term]

    def __init__(self):
        super().__init__('establecimiento')


class EstablecimientoEmailRelation(Table):
    id_email: Union[int, Term]
    id_establecimiento: Union[int, Term]

    def __init__(self):
        super().__init__('establecimiento_email')


class EstablecimientoDireccionRelation(Table):
    id_direccion: Union[int, Term]
    id_establecimiento: Union[int, Term]

    def __init__(self):
        super().__init__('establecimiento_direccion')


class EstablecimientoTelefonoRelation(Table):
    id_telefono: Union[int, Term]
    id_establecimiento: Union[int, Term]

    def __init__(self):
        super().__init__('establecimiento_telefono')
