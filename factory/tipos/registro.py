from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileHandler
from db.schema.dbo.tipo_registro.handler import TipoRegistroHandler
from dominio.enums.tipos import TiposRegistro, OrdenRegistro
from dominio.producto import Registro


class RegistroFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TipoRegistroHandler(db)
        # Cosas como los roles y los tipos, son "singletons" asique los guardo para futuras consultas
        self._storage: List[Registro] = []

    def get(self, registro: TiposRegistro) -> Registro:
        if registro not in TiposRegistro:
            raise Exception("Tipo de registro invalido")

        if val := self._check(registro):
            return val

        return self._create(registro)

    def _create(self, registro: TiposRegistro):
        p = Registro(None, registro, 0)
        p.id, p.orden = self._fetch(p)
        self._storage.append(p)
        return p

    def _fetch(self, p: Registro):
        with self._h.fetch(p) as q:
            q: TipoRegistroHandler
            q.with_descripcion()
        resultado = self._h.results[0]
        # esto es bastante feito y rebuscado, pero por el momento alcanza
        if resultado.orden != getattr(OrdenRegistro, p.tipo.name, None):
            raise Exception("El orden de los enums no coincide con el de la base")
        return resultado.id, resultado.orden

    def _check(self, p: TiposRegistro):
        if registros := [p_ for p_ in self._storage if p_.tipo == p]:
            if len(registros) != 1:
                raise Exception("no deberia haber mas de uno :thinking:")
            return registros[0]
        return False
