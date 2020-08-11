from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from dominio.enums.tipos import TiposPerfil
from dominio.perfil import Perfil


class PerfilFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = SecProfileHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Perfil] = []

    def get(self, perfil: TiposPerfil) -> Perfil:
        if perfil not in TiposPerfil:
            raise Exception("Invalid profile")

        if val := self._check(perfil.value):
            return val

        return self._create(perfil)

    def _create(self, perfil: TiposPerfil):
        p = Perfil(perfil.value, None)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Perfil):
        with self._h.fetch(p) as q:
            q: SecProfileHandler
            q.with_descripcion()
        return self._h.results[0].id_profile

    def _check(self, p: str):
        if perfiles := [p_ for p_ in self._storage if p_.nombre == p]:
            if len(perfiles) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return perfiles[0]
        return False