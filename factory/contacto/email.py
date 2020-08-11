from random import randint

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.email.handler import EmailHandler
from dominio.contacto.email import Email


class EmailFactory:

    def __init__(self, db: MSSQLConnection):
        self._h = EmailHandler(db)

    def create(self) -> Email:
        e = Email(f"Email{randint(100, 500)}@test.com", 0, 0, None)
        e.id = self._h.create(e)
        return e
