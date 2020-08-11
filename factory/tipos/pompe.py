from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_pompe.handler import TipoPompeHandler
from dominio.enums.tipos import TiposPompe
from dominio.producto import Pompe


class PompeFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoPompeHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Pompe] = []

    def get(self, pompe: TiposPompe) -> Pompe:
        if pompe not in TiposPompe:
            raise Exception("Tipo de pompe invalido")

        if val := self._check(pompe.value):
            return val

        return self._create(pompe)

    def _create(self, pompe: TiposPompe):
        p = Pompe(None, pompe.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Pompe):
        with self._h.fetch(p) as q:
            q: TipoPompeHandler
            q.with_descripcion()
        return self._h.results[0].id

    def _check(self, p: str):
        if pompes := [p_ for p_ in self._storage if p_.resultado == p]:
            if len(pompes) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return pompes[0]
        return False