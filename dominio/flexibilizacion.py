from datetime import timedelta, datetime
from typing import Optional

from dominio.enums.tipos import OrdenRegistro, TiposServicio
from dominio.servicio import Servicio
from utils.cria import cria_suceptible_ga
from utils.date import now_plus, cal_days_diff, now


class Flexibilizacion:

    def __init__(self, servicio: Servicio, dias_esperados, multa_esperada):
        self.servicio = servicio
        self.flexibilizado = False
        self.facturado = False
        self.fecha_solicitud: Optional[datetime] = None
        self.dias_vencido = self._calcular_dias_vencidos()
        self.costo = self._calcular_costo()
        self.fecha_maxima = self._calcular_fecha_maxima()
        if dias_esperados != self.dias_vencido:
            raise Exception("Los dias esperados no coinciden con los dias vencido", self.dias_vencido)
        if multa_esperada != self.costo:
            raise Exception("La multa esperada no coincide con el costo", self.costo)

    def solicitar(self):
        self.flexibilizado = True
        self.fecha_solicitud = now()

    def _calcular_costo(self) -> int: raise NotImplementedError()
    def _calcular_dias_vencidos(self) -> int: raise NotImplementedError()
    def _calcular_fecha_maxima(self) -> datetime: raise NotImplementedError()

class ServicioFlexibilizacion(Flexibilizacion):
    MAXIMOS_DIAS_VENCIDO = 267
    DIAS_DESDE = 122

    def __init__(self, servicio: Servicio, dias_esperados, multa_esperada):
        super().__init__(servicio, dias_esperados, multa_esperada)
        self.h_ga = len([h for h in self.servicio.hembras if h.hembra.registro.orden >= OrdenRegistro.CONTROLADO])
        self.emb_ga = len([h for h in self.servicio.machos if h.macho.registro.orden >= OrdenRegistro.REGISTRADO])

    def _calcular_costo(self):
        cant_hembras = len([h for h in self.servicio.hembras if cria_suceptible_ga(h.hembra)])
        if self.servicio.tipo.nombre == TiposServicio.INDIVIDUAL.value:
            if self.dias_vencido >= 1 and self.dias_vencido <= 31:
                costo = 5 * cant_hembras
            else:
                costo = 10 * cant_hembras
        else:
            if self.dias_vencido >= 1 and self.dias_vencido <= 31:
               costo = 1 * cant_hembras
            else:
               costo = 3 * cant_hembras
        return costo

    def _calcular_dias_vencidos(self):
        fecha_obtenida = self.servicio.fecha_fin + timedelta(days=self.DIAS_DESDE)
        return abs((fecha_obtenida - self.servicio.fecha_carga).days) - 1 # :shrug:

    def _calcular_fecha_maxima(self):
        return self.servicio.fecha_inicio + timedelta(days=self.MAXIMOS_DIAS_VENCIDO)