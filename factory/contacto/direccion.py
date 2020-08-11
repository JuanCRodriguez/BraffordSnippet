from random import randint

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.direccion.handler import DireccionHandler
from dominio.contacto.direccion import Direccion
from dominio.provincia import Provincia


class DireccionFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = DireccionHandler(db)

    def create(self) -> Direccion:
        n = randint(1, 500)
        d = Direccion(Provincia(1, "CAPITAL FEDERAL"), f"Loc {n}", f"Calle {n}", f"Cp {n}", f"Nro {n}", f"Piso {n}",
                      f"Dep {n}", f"Ofi {n}", f"Obs {n}", f"Parti{n}", None, None)
        d.id = self._h.create(d)
        return d
