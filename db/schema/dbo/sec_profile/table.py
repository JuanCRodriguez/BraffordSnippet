from typing import Union

from pypika import Table
from pypika.terms import Term


class SecProfileTable(Table):
    id_profile: Union[int, Term]
    name: Union[str, Term]

    def __init__(self):
        super().__init__('sec_profile')