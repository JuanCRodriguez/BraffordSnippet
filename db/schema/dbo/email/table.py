from typing import Union

from pypika import Table
from pypika.terms import Term


class EmailTable(Table):
    id: Union[int, Term]
    cuenta: Union[str, Term]
    observacion: Union[str, Term]
    contacto: Union[int, Term]
    id_tipo_contacto: Union[int, Term]
    verificada: Union[int, Term]
    email_token: Union[str, Term]

    def __init__(self):
        super().__init__('email')
