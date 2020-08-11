from dataclasses import dataclass

from dominio.cabaña import Cabaña
from dominio.flexibilizacion import ServicioFlexibilizacion


@dataclass
class BuscadorServiciosAFlexbilizarDataContract:
    NOMBRE_CABAÑA: str
    NUMERO_SERVICIO: str
    TIPO_SERVICIO: str
    H_EMB: str
    DIAS_VENCIDO: str
    FECHA_MAXIMA: str
    COSTO_MULTA: str
    FLEXIBILIZADO: bool

    @classmethod
    def from_domain(cls, flexibilizacion: ServicioFlexibilizacion):
        return cls(
            NOMBRE_CABAÑA=flexibilizacion.servicio.cabaña.nombre,
            NUMERO_SERVICIO=str(flexibilizacion.servicio.id),
            TIPO_SERVICIO=flexibilizacion.servicio.tipo.nombre,
            H_EMB=str(flexibilizacion.h_ga),
            DIAS_VENCIDO=str(flexibilizacion.dias_vencido),
            FECHA_MAXIMA="{d.day}/{d.month}/{d.year}".format(d=flexibilizacion.fecha_maxima),
            COSTO_MULTA=str(flexibilizacion.costo),
            FLEXIBILIZADO=flexibilizacion.flexibilizado
        )

@dataclass
class BuscadorServiciosFlexibilizadosDataContract:

    NOMBRE_CABAÑA: str
    NUMERO_SERVICIO: str
    TIPO_SERVICIO: str
    H_EMB: str
    DIAS_VENCIDO: str
    FECHA_SOLICITUD: str
    COSTO_MULTA: str
    FACTURADO: bool

    @classmethod
    def from_domain(cls, flexibilizacion: ServicioFlexibilizacion):
        if flexibilizacion.fecha_solicitud is None:
            raise Exception("No se solicito la flexibilizacion")
        return cls(
            NOMBRE_CABAÑA=flexibilizacion.servicio.cabaña.nombre,
            NUMERO_SERVICIO=str(flexibilizacion.servicio.id),
            TIPO_SERVICIO=flexibilizacion.servicio.tipo.nombre,
            H_EMB=str(flexibilizacion.h_ga),
            DIAS_VENCIDO=str(flexibilizacion.dias_vencido),
            FECHA_SOLICITUD="{d.day}/{d.month}/{d.year}".format(d=flexibilizacion.fecha_solicitud),
            COSTO_MULTA=str(flexibilizacion.costo),
            FACTURADO=flexibilizacion.facturado
        )