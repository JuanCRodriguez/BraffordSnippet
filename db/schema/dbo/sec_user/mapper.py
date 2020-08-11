from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.usuario import Usuario


@dataclass
class SecUserDataClass(object):
    id_user: int
    name: str
    pass_: str
    pass1: Any

class SecUserMapper(Mapper):

    def in_(self, o: Usuario) -> SecUserDataClass:
        return SecUserDataClass(
            id_user=o.id_sec,
            name= o.username,
            pass_='25d55ad283aa400af464c76d713c07ad',
            pass1=None
        )

