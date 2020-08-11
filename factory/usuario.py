from random import randint

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.sec_profile.handler import SecProfileUserRelationBuilder
from db.schema.dbo.sec_user.handler import SecUserHandler
from db.schema.dbo.usuario.handler import UsuarioHandler, UsuarioEmailRelationBuilder
from dominio.cabaña import Cabaña
from dominio.contacto.email import Email
from dominio.perfil import Perfil
from dominio.usuario import Usuario


class UsuarioFactory:

    def __init__(self, db: MSSQLConnection):
        self._sec_handler = SecUserHandler(db)
        self._sec_profile_relation = SecProfileUserRelationBuilder(db)

        self._user_handler = UsuarioHandler(db)
        self._user_email_relation = UsuarioEmailRelationBuilder(db)

    def create(self,
               cabaña: Cabaña,
               email: Email,
               perfil: Perfil) -> Usuario:
        if not cabaña.id:
            raise Exception("Cabaña invalida")

        if not perfil.id:
            raise Exception("Perfil invalido")

        if not email.id:
            raise Exception("Email invalido")

        return self._create(cabaña, email, perfil)

    def _create(self,
                cabaña: Cabaña,
                email: Email,
                perfil: Perfil) -> Usuario:
        usuario = Usuario("Usuario", "De prueba", f"usuario{randint(100, 5000)}",
                          cabaña, email, perfil)
        usuario.id_sec = self._sec_handler.create(usuario)
        usuario.id_usuario = self._user_handler.create(usuario)
        self._sec_profile_relation.create(usuario, usuario.rol)
        self._user_email_relation.create(usuario.email, usuario)
        return usuario
