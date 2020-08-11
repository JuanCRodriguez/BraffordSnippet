from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_color.handler import TipoColorHandler
from dominio.enums.tipos import TiposColor
from dominio.producto import Color


class ColorFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoColorHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Color] = []

    def get(self, color: TiposColor) -> Color:
        if color not in TiposColor:
            raise Exception("Color invalido")

        if val := self._check(color.value):
            return val

        return self._create(color)

    def _create(self, color: TiposColor):
        p = Color(None, color.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Color):
        with self._h.fetch(p) as q:
            q: TipoColorHandler
            q.with_nombre()
        return self._h.results[0].id

    def _check(self, p: str):
        if colors := [p_ for p_ in self._storage if p_.nombre == p]:
            if len(colors) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return colors[0]
        return False