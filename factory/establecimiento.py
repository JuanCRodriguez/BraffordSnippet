from random import randint

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.establecimiento.handler import EstablecimientoHandler, EstablecimientoEmailRelationBuilder, \
    EstablecimientoDireccionRelationBuilder, \
    EstablecimientoTelefonoRelationBuilder
from dominio.cabaña import Cabaña
from dominio.contacto.direccion import Direccion
from dominio.contacto.email import Email
from dominio.contacto.telefono import Telefono
from dominio.establecimiento import Establecimiento


class EstablecimientoFactory:

    def __init__(self, db: MSSQLConnection):
        self._establecimiento_handler = EstablecimientoHandler(db)
        self._establecimiento_direccion_relation = EstablecimientoDireccionRelationBuilder(db)
        self._establecimiento_telefono_relation = EstablecimientoTelefonoRelationBuilder(db)
        self._establecimiento_email_relation = EstablecimientoEmailRelationBuilder(db)

    def create(self,
               cabaña: Cabaña,
               direccion: Direccion,
               telefono: Telefono,
               email: Email) -> Establecimiento:
        if not cabaña.id:
            raise Exception("Cabaña invalida")

        if not direccion.id:
            raise Exception("Establecimiento invalida")

        if not telefono.id:
            raise Exception("Perfil invalido")

        if not email.id:
            raise Exception("Email invalido")

        return self._create(cabaña, direccion, telefono, email)

    def _create(self,
                cabaña: Cabaña,
                direccion: Direccion,
                telefono: Telefono,
                email: Email) -> Establecimiento:
        e = Establecimiento(f"Establecimiento {randint(1, 50)}", cabaña, "Renspa", email, telefono,
                            direccion)
        e.id = self._establecimiento_handler.create(e)

        self._establecimiento_direccion_relation.create(direccion, e)
        self._establecimiento_telefono_relation.create(telefono, e)
        self._establecimiento_email_relation.create(email, e)
        return e
