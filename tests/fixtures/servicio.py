from typing import List

import pytest
from _pytest.fixtures import SubRequest

from dominio.establecimiento import Establecimiento
from dominio.producto import Producto
from factory.servicio import ServicioFactory
from factory.tipos.servicio import TipoServicioFactory
from utils.context import Context


@pytest.fixture()
def servicio(context: Context, productos: List[Producto], establecimiento: Establecimiento, request: SubRequest):
    # params
    # {
    #     "Hembras": [key producto (P1)],
    #     "Machos": [key producto (P2)],
    #     "Fecha Inicio": datetime,
    #     "Fecha Fin": datetime,
    #     "Fecha Carga": datetime,
    #     "Limita Registro": bool,
    #     "Tipo": TipoServicio
    # }
    tipo_servicio = TipoServicioFactory(context.db).get(request.param['Tipo'])
    hembras = [productos[key] for key in request.param['Hembras']]
    machos = [productos[key] for key in request.param['Machos']]
    servicio = ServicioFactory(context.db).create(
        limita_registro=request.param['Limita Registro'],
        tipo=tipo_servicio,
        fecha_inicio=request.param['Fecha Inicio'],
        fecha_fin=request.param['Fecha Fin'],
        fecha_carga=request.param['Fecha Carga'],
        cabaña=establecimiento.cabaña,
        machos=machos,
        hembras=hembras
    )
    context.db.commit()
    return servicio
