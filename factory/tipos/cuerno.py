from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_cuerno.handler import TipoCuernoHandler
from dominio.enums.tipos import TiposCuerno
from dominio.producto import Cuerno


class CuernoFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoCuernoHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Cuerno] = []

    def get(self, cuerno: TiposCuerno) -> Cuerno:
        if cuerno not in TiposCuerno:
            raise Exception("Tipo de cuerno invalido")

        if val := self._check(cuerno.value):
            return val

        return self._create(cuerno)

    def _create(self, cuerno: TiposCuerno):
        p = Cuerno(None, cuerno.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Cuerno):
        with self._h.fetch(p) as q:
            q: TipoCuernoHandler
            q.with_descripcion()
        return self._h.results[0].id

    def _check(self, p: str):
        if cuernos := [p_ for p_ in self._storage if p_.tipo == p]:
            if len(cuernos) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return cuernos[0]
        return False