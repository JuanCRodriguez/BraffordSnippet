from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_denticion.handler import TipoDenticionHandler
from dominio.enums.tipos import TiposDenticion
from dominio.producto import Denticion


class DenticionFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoDenticionHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Denticion] = []

    def get(self, denticion: TiposDenticion) -> Denticion:
        if denticion not in TiposDenticion:
            raise Exception("Tipo de denticion invalido")

        if val := self._check(denticion.value):
            return val

        return self._create(denticion)

    def _create(self, denticion: TiposDenticion):
        p = Denticion(None, denticion.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Denticion):
        with self._h.fetch(p) as q:
            q: TipoDenticionHandler
            q.with_descripcion()
        return self._h.results[0].id

    def _check(self, p: str):
        if denticiones := [p_ for p_ in self._storage if p_.tipo == p]:
            if len(denticiones) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return denticiones[0]
        return False