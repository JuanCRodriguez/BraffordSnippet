from dataclasses import dataclass
from typing import Any

from db.base.mapper import Mapper
from dominio.contacto.email import Email


@dataclass
class EmailDataClass(object):
    id: Any
    cuenta: str
    observacion: str
    contacto: int
    id_tipo_contacto: int
    verificada: int
    email_token: str


class EmailMapper(Mapper):

    def in_(self, o: Email) -> EmailDataClass:
        return EmailDataClass(
            id=o.id,
            cuenta=o.cuenta,
            observacion=o.observacion,
            contacto=0,
            id_tipo_contacto=o.tipo_contacto.id if o.tipo_contacto else None,
            # Dudo que en algun momento se implemente un test sobre esto
            verificada=int(True),
            email_token="Ignora2"
        )
