import pytest

from factory.cabaña import CabañaFactory
from factory.contacto.direccion import DireccionFactory
from factory.contacto.email import EmailFactory
from factory.contacto.telefono import TelefonoFactory
from factory.establecimiento import EstablecimientoFactory
from factory.productor import ProductorFactory


@pytest.fixture()
def establecimiento(context, cabaña):
    d, t, e = dte(context.db)
    establecimiento = EstablecimientoFactory(context.db).create(cabaña, d, t, e)
    context.db.commit()
    return establecimiento

@pytest.fixture()
def cabaña(context, productor):
    d, t, e = dte(context.db)
    return CabañaFactory(context.db).create(productor, d, t, e)

@pytest.fixture
def productor(context):
    d, t, e = dte(context.db)
    return ProductorFactory(context.db).create(d, t, e)

def dte(db):
    return DireccionFactory(db).create(), \
           TelefonoFactory(db).create(), \
           EmailFactory(db).create()
