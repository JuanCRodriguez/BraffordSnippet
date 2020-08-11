from random import randint

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.telefono.handler import TelefonoHandler
from dominio.contacto.telefono import Telefono


class TelefonoFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = TelefonoHandler(db)

    def create(self) -> Telefono:
        n = randint(1, 500)
        t = Telefono(f"cod {n}", f"int {n}", f"num {n}", f"int{n}", f"obs {n}", None, None)
        t.id = self._h.create(t)
        return t
