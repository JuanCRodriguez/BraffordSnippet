from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_raza.handler import TipoRazaHandler
from dominio.enums.tipos import TiposRaza
from dominio.producto import Raza


class RazaFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoRazaHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Raza] = []

    def get(self, raza: TiposRaza) -> Raza:
        if raza not in TiposRaza:
            raise Exception("Invalid profile")

        if val := self._check(raza.value):
            return val

        return self._create(raza)

    def _create(self, raza: TiposRaza):
        p = Raza(None, raza.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Raza):
        with self._h.fetch(p) as q:
            q: TipoRazaHandler
            q.with_descripcion()
        return self._h.results[0].id

    def _check(self, p: str):
        if razas := [p_ for p_ in self._storage if p_.nombre == p]:
            if len(razas) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return razas[0]
        return False