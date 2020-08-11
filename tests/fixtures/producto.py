from random import choice

import pytest

from dominio.cabaña import Cabaña
from dominio.enums.tipos import TiposSexo, TiposRegistro, TiposDenticion, TiposRaza, TiposColor, TiposCuerno, \
    TiposVariedad, TiposParto, TiposPompe
from dominio.establecimiento import Establecimiento
from factory.medicion import MedicionFactory
from factory.producto import ProductoFactory
from factory.tipos.color import ColorFactory
from factory.tipos.cuerno import CuernoFactory
from factory.tipos.denticion import DenticionFactory
# params :
# {
#   "Numero Prod": (Sexo, Registro)
# }
from factory.tipos.parto import PartoFactory
from factory.tipos.pompe import PompeFactory
from factory.tipos.raza import RazaFactory
from factory.tipos.registro import RegistroFactory
from factory.tipos.sexo import SexoFactory
from factory.tipos.variedad import VariedadFactory
from utils.context import Context


@pytest.fixture()
def productos(context: Context, request, establecimiento: Establecimiento):
    if not request.param:
        raise Exception("Invalid param")

    aux = dict()
    # por el momento son dos atributos, asique se puede hardcodear,
    # pero eventualmente habra que migrar a un diccionario nesteado
    # o un dataclass
    for key, props in request.param.items():
        if not props:
            raise Exception("Invalid props")
        tipo_sexo: TiposSexo
        tipo_registro: TiposRegistro
        tipo_sexo, tipo_registro = props

        denticion = DenticionFactory(context.db).get(choice(list(TiposDenticion)))
        medicion = MedicionFactory(context.db).create(denticion)
        raza = RazaFactory(context.db).get(choice(list(TiposRaza)))
        sexo = SexoFactory(context.db).get(tipo_sexo)
        registro = RegistroFactory(context.db).get(tipo_registro)
        color = ColorFactory(context.db).get(choice(list(TiposColor)))
        cuerno = CuernoFactory(context.db).get(choice(list(TiposCuerno)))
        variedad = VariedadFactory(context.db).get(choice(list(TiposVariedad)))
        parto = PartoFactory(context.db).get(choice(list(TiposParto)))
        pompe = PompeFactory(context.db).get(TiposPompe.SIN_ANALISIS)
        aux[key] = ProductoFactory(context.db).create(
            cabaña=establecimiento.cabaña,
            establecimiento=establecimiento,
            mediciones=medicion,
            raza=raza,
            registro=registro,
            color=color,
            cuerno=cuerno,
            variedad=variedad,
            parto=parto,
            pompe=pompe,
            sexo=sexo
        )
    context.db.commit()
    return aux