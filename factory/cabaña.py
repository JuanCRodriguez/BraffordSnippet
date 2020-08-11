from random import randint

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.cabaña.handler import CabañaHandler, CabañaEmailRelationBuilder, CabañaDireccionRelationBuilder, \
    CabañaTelefonoRelationBuilder
from dominio.contacto.direccion import Direccion
from dominio.contacto.email import Email
from dominio.contacto.telefono import Telefono
from dominio.cabaña import Cabaña
from dominio.productor import Productor


class CabañaFactory:

    def __init__(self, db: MSSQLConnection):
        self._cabaña_handler = CabañaHandler(db)
        self._cabaña_direccion_relation = CabañaDireccionRelationBuilder(db)
        self._cabaña_telefono_relation = CabañaTelefonoRelationBuilder(db)
        self._cabaña_email_relation = CabañaEmailRelationBuilder(db)

    def create(self,
               productor: Productor,
               direccion: Direccion,
               telefono: Telefono,
               email: Email) -> Cabaña:
        if not productor.id:
            raise Exception("Productor invalido")

        if not direccion.id:
            raise Exception("Cabaña invalida")

        if not telefono.id:
            raise Exception("Perfil invalido")

        if not email.id:
            raise Exception("Email invalido")

        return self._create(productor, direccion, telefono, email)

    def _create(self,
                productor: Productor,
                direccion: Direccion,
                telefono: Telefono,
                email: Email) -> Cabaña:
        cabaña = Cabaña(f"Cab {randint(1, 999)}", "PRM", "PRH", productor, 999)
        cabaña.id = self._cabaña_handler.create(cabaña)

        self._cabaña_direccion_relation.create(direccion, cabaña)
        cabaña.direcciones.append(direccion)

        self._cabaña_telefono_relation.create(telefono, cabaña)
        cabaña.telefonos.append(telefono)

        self._cabaña_email_relation.create(email, cabaña)
        cabaña.emails.append(email)
        return cabaña
