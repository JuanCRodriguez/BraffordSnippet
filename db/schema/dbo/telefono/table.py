from typing import Union

from pypika import Table
from pypika.terms import Term


class TelefonoTable(Table):

    id: Union[int, Term]
    codigo_pais: Union[str, Term]
    codigo_interurbano: Union[str, Term]
    numero: Union[str, Term]
    interno: Union[str, Term]
    observacion: Union[str, Term]
    id_tipo_contacto: Union[int, Term]
    id_tipo_telefono: Union[int, Term]

    def __init__(self):
        super().__init__('telefono')
