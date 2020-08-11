from datetime import datetime
from random import randint
from typing import List

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.hembra_en_servicio.handler import HembraEnServicioHandler
from db.schema.dbo.machosenservicio.handler import MachosEnServicioHandler
from db.schema.dbo.sec_user.handler import SecUserHandler
from db.schema.dbo.servicio.handler import ServicioHandler
from dominio.cabaña import Cabaña
from dominio.enums.tipos import TiposSexo
from dominio.producto import Producto
from dominio.servicio import Servicio, TipoServicio


class ServicioFactory:

    def __init__(self, db: MSSQLConnection):
        self._servicio_handler = ServicioHandler(db)
        self._hembra_en_servicio_handler = HembraEnServicioHandler(db)
        self._macho_en_servicio_handler = MachosEnServicioHandler(db)

    def create(self,
               limita_registro: bool,
               tipo: TipoServicio,
               fecha_inicio: datetime,
               fecha_fin: datetime,
               fecha_carga: datetime,
               cabaña: Cabaña,
               machos: List[Producto],
               hembras: List[Producto]) -> Servicio:
        if not tipo.id:
            raise Exception("Tipo de servicio invalido")

        for macho in machos:
            if not macho.id:
                raise Exception("Macho invalido", macho)
            if macho.sexo.nombre != TiposSexo.MACHO.value:
                raise Exception("El producto no es macho")

        for hembra in hembras:
            if not hembra.id:
                raise Exception("Hembra invalida")
            if hembra.sexo.nombre != TiposSexo.HEMBRA.value:
                raise Exception("El producto no es hembra")

        return self._create(limita_registro, tipo, fecha_inicio, fecha_fin, fecha_carga, cabaña, machos, hembras)

    def _create(self,
                limita_registro: bool,
                tipo: TipoServicio,
                fecha_inicio: datetime,
                fecha_fin: datetime,
                fecha_carga: datetime,
                cabaña: Cabaña,
                machos: List[Producto],
                hembras: List[Producto]) -> Servicio:
        servicio = Servicio(tipo, limita_registro, fecha_inicio, fecha_fin, fecha_carga, cabaña)
        servicio.id = self._servicio_handler.create(servicio)

        for h in hembras:
            h_s = servicio.agregar_hembra(h)
            h_s.id = self._hembra_en_servicio_handler.create(h_s)

        for m in machos:
            m_s = servicio.agregar_macho(m)
            m_s.id = self._macho_en_servicio_handler.create(m_s)

        return servicio
