from typing import Union, Optional

from pypika import Table
from pypika.terms import Term


class MachosEnServicioTable(Table):
    id: Union[int, Term]
    servicioid: Union[int, Term]
    machoid: Union[int, Term]
    semenid: Union[Optional[int], Term]
    cantidadsemen: Union[Optional[int], Term]
    desestimado: Union[Optional[int], Term]
    adn: Union[Optional[int], Term]

    def __init__(self): # facepalm
        super().__init__('machosenservicio')
