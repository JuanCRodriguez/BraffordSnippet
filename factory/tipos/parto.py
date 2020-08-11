from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_parto.handler import TipoPartoHandler
from dominio.enums.tipos import TiposParto
from dominio.producto import Parto


class PartoFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoPartoHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Parto] = []

    def get(self, parto: TiposParto) -> Parto:
        if parto not in TiposParto:
            raise Exception("Tipo de parto invalido")

        if val := self._check(parto.value):
            return val

        return self._create(parto)

    def _create(self, parto: TiposParto):
        p = Parto(None, parto.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Parto):
        with self._h.fetch(p) as q:
            q: TipoPartoHandler
            q.with_descripcion()
        return self._h.results[0].id

    def _check(self, p: str):
        if partos := [p_ for p_ in self._storage if p_.tipo == p]:
            if len(partos) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return partos[0]
        return False