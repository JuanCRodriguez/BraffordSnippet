from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_variedad.handler import TipoVariedadHandler
from dominio.enums.tipos import TiposVariedad
from dominio.producto import Variedad


class VariedadFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoVariedadHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Variedad] = []

    def get(self, variedad: TiposVariedad) -> Variedad:
        if variedad not in TiposVariedad:
            raise Exception("Tipo de variedad invalido")

        if val := self._check(variedad.value):
            return val

        return self._create(variedad)

    def _create(self, variedad: TiposVariedad):
        p = Variedad(None, variedad.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Variedad):
        with self._h.fetch(p) as q:
            q: TipoVariedadHandler
            q.with_descripcion()
        return self._h.results[0].id

    def _check(self, p: str):
        if variedades := [p_ for p_ in self._storage if p_.tipo == p]:
            if len(variedades) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return variedades[0]
        return False