from dataclasses import dataclass

from db.base.mapper import Mapper
from dominio.usuario import Usuario


@dataclass
class UsuarioDataClass(object):
    id: int
    id_user: int
    nombre: str
    apellido: str
    id_cabania: int
    habilitado_voto: int
    activo: int


class UsuarioMapper(Mapper):

    def in_(self, o: Usuario) -> UsuarioDataClass:
        return UsuarioDataClass(
            id=o.id_usuario,
            id_user=o.id_sec,
            nombre=o.nombre,
            apellido=o.apellido,
            id_cabania=o.cabaña.id,
            habilitado_voto=1,
            activo=1
        )
