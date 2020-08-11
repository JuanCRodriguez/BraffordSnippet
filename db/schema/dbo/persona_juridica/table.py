from typing import Any, Union

from pypika import Table
from pypika.terms import Term


class PersonaJuridicaTable(Table):

    id: Union[Any, Term]
    razon_social: Union[str, Term]
    observacion: Union[str, Term]
    cuit: Union[str, Term]
    num_socio: Union[str, Term]
    web: Union[str, Term]
    activo: Union[int, Term]
    fecha_inicio_actividad: Union[str, Term]

    def __init__(self):
        super().__init__('persona_juridica')


class PersonaJuridicaDireccionRelation(Table):

    id_direccion: Union[int, Term]
    id_persona_juridica: Union[int, Term]

    def __init__(self):
        super().__init__('persona_juridica_direccion')


class PersonaJuridicaTelefonoRelation(Table):

    id_telefono: Union[int, Term]
    id_persona_juridica: Union[int, Term]

    def __init__(self):
        super().__init__('persona_juridica_telefono')


class PersonaJuridicaEmailRelation(Table):

    id_email: Union[int, Term]
    id_persona_juridica: Union[int, Term]

    def __init__(self):
        super().__init__('persona_juridica_email')