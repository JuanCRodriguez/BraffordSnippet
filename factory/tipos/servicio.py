from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.tipo_servicio.handler import TipoServicioHandler
from dominio.enums.tipos import TiposServicio
from dominio.servicio import TipoServicio


class TipoServicioFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoServicioHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[TipoServicio] = []

    def get(self, servicio: TiposServicio) -> TipoServicio:
        if servicio not in TiposServicio:
            raise Exception("Tipo de servicio invalido")

        if val := self._check(servicio.value):
            return val

        return self._create(servicio)

    def _create(self, servicio: TiposServicio):
        p = TipoServicio(None, servicio.value)
        p.id = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: TipoServicio):
        with self._h.fetch(p) as q:
            q: TipoServicioHandler
            q.with_nombre()
        return self._h.results[0].id

    def _check(self, p: str):
        if tipos := [p_ for p_ in self._storage if p_.nombre == p]:
            if len(tipos) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return tipos[0]
        return False