from typing import Union

from pypika import Table
from pypika.terms import Term


class ProvinciaTable(Table):
    id: Union[int, Term]
    descripcion: Union[str, Term]

    def __init__(self):
        super().__init__("provincia")
