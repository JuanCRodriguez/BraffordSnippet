from typing import Union

from pypika import Table
from pypika.terms import Term


class UsuarioTable(Table):
    id: Union[int, Term]
    id_user: Union[int, Term]
    nombre: Union[str, Term]
    apellido: Union[str, Term]
    id_cabania: Union[int, Term]
    habilitado_voto: Union[int, Term]
    activo: Union[int, Term]

    def __init__(self):
        super().__init__('usuario')


class UsuarioEmailRelation(Table):
    id_email: Union[int, Term]
    id_usuario: Union[int, Term]

    def __init__(self):
        super().__init__('usuario_email')
