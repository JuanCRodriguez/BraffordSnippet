from random import randint

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.persona_juridica.handler import PersonaJuridicaHandler, PersonaJuridicaDireccionRelationBuilder, \
    PersonaJuridicaTelefonoRelationBuilder, PersonaJuridicaEmailRelationBuilder
from dominio.contacto.direccion import Direccion
from dominio.contacto.email import Email
from dominio.contacto.telefono import Telefono
from dominio.productor import Productor


class ProductorFactory:

    def __init__(self, db: MSSQLConnection):
        self._productor_handler = PersonaJuridicaHandler(db)
        self._productor_direccion_relation = PersonaJuridicaDireccionRelationBuilder(db)
        self._productor_telefono_relation = PersonaJuridicaTelefonoRelationBuilder(db)
        self._productor_email_relation = PersonaJuridicaEmailRelationBuilder(db)

    def create(self,
               direccion: Direccion,
               telefono: Telefono,
               email: Email) -> Productor:

        if not direccion.id:
            raise Exception("Productor invalida")

        if not telefono.id:
            raise Exception("Perfil invalido")

        if not email.id:
            raise Exception("Email invalido")

        return self._create(direccion, telefono, email)

    def _create(self,
                direccion: Direccion,
                telefono: Telefono,
                email: Email) -> Productor:
        productor = Productor(f"Razon {randint(1, 999)}", "Cuit", 999, "Obs de prueba")
        productor.id = self._productor_handler.create(productor)

        self._productor_direccion_relation.create(direccion, productor)
        productor.direcciones.append(direccion)

        self._productor_telefono_relation.create(telefono, productor)
        productor.telefonos.append(telefono)

        self._productor_email_relation.create(email, productor)
        productor.emails.append(email)
        return productor
