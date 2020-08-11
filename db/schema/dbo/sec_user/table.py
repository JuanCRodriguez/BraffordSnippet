from typing import Any, Union

from pypika import Table
from pypika.terms import Term


class SecUserTable(Table):
    id_user: Union[int, Term]
    name: Union[str, Term]
    pass1: Union[Any, Term]

    def __init__(self):
        super().__init__("sec_user")

    @property
    def pass_(self) -> int:
        return getattr(self, "pass")

class SecProfileUserRelation(Table):
    id_user: Union[int, Term]
    id_profile: Union[int, Term]

    def __init__(self):
        super().__init__("sec_profile_user")

