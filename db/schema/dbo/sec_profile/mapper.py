from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.perfil import Perfil


@dataclass
class SecProfileDataClass(object):
    id_profile: Any
    name: str


class SecProfileMapper(Mapper):

    def in_(self, o: Perfil) -> SecProfileDataClass:
        return SecProfileDataClass(
            id_profile=o.id,
            name=o.nombre,
        )

    def out(self, o) -> SecProfileDataClass:
        return SecProfileDataClass(
            id_profile=o.id_profile,
            name=o.name
        )
