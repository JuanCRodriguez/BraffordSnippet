from dataclasses import dataclass
from datetime import datetime
from typing import Union

from dominio.enums.tipos import TiposRegistro
from dominio.mediciones import Mediciones


class Producto:

    def __init__(self, rp, nombre,
                 apodo, tatuaje, raza,
                 registro, color, cuerno,
                 variedad, sexo, codigo_aba,
                 pompe, medicion, dep,
                 fecha_nacimiento, tipo_parto, establecimiento):
        self.fecha_carga = datetime.now()
        self.id = None
        self.dep = dep
        self.rp = rp
        self.medicion: Mediciones = medicion
        self.codigo_aba = codigo_aba
        self.codigo_hba = None
        self.nombre = nombre
        self.apodo = apodo
        self.tatuaje = tatuaje
        self.raza: Raza = raza
        self.registro: Registro = registro
        self.color: Color = color
        self.cuerno: Cuerno = cuerno
        self.variedad: Variedad = variedad
        self.sexo: Sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_parto: Parto = tipo_parto
        self.establecimiento = establecimiento
        self.pompe: Pompe = pompe
        self.servicio_nacimiento = None
        self.padre = None
        self.madre = None


@dataclass
class Raza:
    id: Union[None, int]
    nombre: str


@dataclass
class Registro:
    id: Union[None, int]
    tipo: TiposRegistro
    orden: int

@dataclass
class Color:
    id: Union[None, int]
    nombre: str


@dataclass
class Cuerno:
    id: Union[None, int]
    tipo: str


@dataclass
class Variedad:
    id: Union[None, int]
    tipo: str

@dataclass
class Parto:
    id: Union[None, int]
    tipo: str

@dataclass
class Pompe:
    id: Union[None, int]
    resultado: str

@dataclass
class Sexo:
    id: Union[None, int]
    nombre: str

@dataclass
class Denticion:
    id: Union[None, int]
    tipo: str