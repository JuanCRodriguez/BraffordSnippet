from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from dominio.cabaña import Cabaña
from dominio.enums.estados import EstadosServicio
from dominio.enums.tipos import TiposSexo
from dominio.producto import Producto


@dataclass
class TipoServicio:
    id: Optional[int]
    nombre: str


class Servicio:

    def __init__(self, tipo: TipoServicio,
                 limita_registro:bool,
                 fecha_inicio: datetime,
                 fecha_fin: datetime,
                 fecha_carga: datetime,
                 cabaña: Cabaña):
        self.transferencia = None
        self.id = None # se utiliza como numero tambien
        self.cabaña = cabaña
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_carga = fecha_carga
        self.limita_registro = limita_registro
        self.tipo = tipo
        self.hembras: List[HembraEnServicio] = []
        self.machos: List[MachoEnServicio] = []
        self.estado = EstadosServicio.APROBADO
        self.embrion = None
        self.pendiente_aprobacion = False

    def agregar_hembra(self, p: Producto):
        if p.sexo.nombre != TiposSexo.HEMBRA.value:
            raise Exception("El bicho no es hembra", p.sexo)
        self.hembras.append(
            h := HembraEnServicio(
                id=None,
                hembra=p,
                servicio=self,
                fecha=datetime.now(),
                desestimado=False
            )
        )
        return h


    def agregar_macho(self, p: Producto):
        if p.sexo.nombre != TiposSexo.MACHO.value:
            raise Exception("El bicho no es macho", p.sexo)
        self.machos.append(
            m := MachoEnServicio(
                id=None,
                macho=p,
                servicio=self,
                semen_id=None,
                cantidad_semen=None,
                desestimado=False,
                adn=None
            )
        )
        return m

    def cantidad_embriones(self):
        return 0

    def cantidad_machos_sin_registrar(self):
        return 0

    def cantidad_hembras_sin_registrar(self):
        return 0

    def cantidad_hembras_sin_registrar_no_bo(self):
        return 0

    def cantidad_machos_sin_registrar_otras_razas(self):
        return 0

    def cantidad_hembras_sin_registrar_otras_razas(self):
        return 0

@dataclass
class HembraEnServicio:
    id: Optional[int]
    hembra: Producto
    servicio: Servicio
    fecha: datetime
    desestimado: bool

@dataclass
class MachoEnServicio:
    id: Optional[int]
    macho: Producto
    servicio: Servicio
    semen_id: Optional[int]
    cantidad_semen: Optional[int]
    desestimado: bool
    adn: Optional[str]