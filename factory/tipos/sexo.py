from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_sexo.handler import TipoSexoHandler
from dominio.enums.tipos import TiposSexo
from dominio.producto import Sexo


class SexoFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoSexoHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Sexo] = []

    def get(self, sexo: TiposSexo) -> Sexo:
        if sexo not in TiposSexo:
            raise Exception("Tipo de sexo invalido")

        if val := self._check(sexo.value):
            return val

        return self._create(sexo)

    def _create(self, sexo: TiposSexo):
        p = Sexo(None, sexo.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Sexo):
        with self._h.fetch(p) as q:
            q: TipoSexoHandler
            q.with_descripcion()
        return self._h.results[0].id

    def _check(self, p: str):
        if sexos := [p_ for p_ in self._storage if p_.nombre == p]:
            if len(sexos) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return sexos[0]
        return False