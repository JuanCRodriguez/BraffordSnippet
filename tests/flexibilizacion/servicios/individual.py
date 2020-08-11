import allure
import pytest

from actions.flexibilizacion.buscar_solicitudes import BuscarServiciosAFlexibilizarActionHandler, \
    BuscarServiciosFlexibilizadosActionHandler
from actions.flexibilizacion.solicitar import SolicitarFlexibilizacionServicioActionHandler
from actions.login import LoginActionHandler
from dominio.enums.tipos import TiposSexo, TiposRegistro, TiposPerfil, TiposServicio
from dominio.flexibilizacion import ServicioFlexibilizacion
from utils.date import now_minus, now


@allure.feature("Flexibilizacion")
@allure.story("Flexibilizar un servicio")
@allure.title("El usuario flexibiliza un servicio individual con menos de 30 dias vencido")
@pytest.mark.parametrize("productos", [
    {
        "P1": (TiposSexo.HEMBRA, TiposRegistro.DEFINITIVO),
        "P2": (TiposSexo.MACHO, TiposRegistro.DEFINITIVO)
    }],
    ids=[
        "P1: Hembra, Definitivo, "
        "P2: Macho, Definitivo"
    ], indirect=True)
@pytest.mark.parametrize("servicio", [
    {
        "Hembras": ["P1"],
        "Machos": ["P2"],
        "Fecha Inicio": now_minus(266),
        "Fecha Fin": now_minus(234),
        "Fecha Carga": now_minus(104),
        "Limita Registro": True,
        "Tipo": TiposServicio.INDIVIDUAL
    }],
    ids=[
        "Servicio Individual con registro limitado, 7 dias de vencimiento y 5kg de multa"
    ], indirect=True)
@pytest.mark.parametrize("usuarios", [
    {
        "U1": TiposPerfil.PRODUCTOR,
    }],
    ids=[
        "Un productor"
    ], indirect=True)
def test_001(context, usuarios, productos, servicio):
    flex = ServicioFlexibilizacion(servicio, dias_esperados=7, multa_esperada=5)
    with allure.step("El productor ingresa al sistema"):
        LoginActionHandler(context).do(usuarios['U1'])
    with allure.step("Busca el servicio y solicita su flexibilizacion"):
        BuscarServiciosAFlexibilizarActionHandler(context).go_to().do(servicio).success(flex)
        action = SolicitarFlexibilizacionServicioActionHandler(context).verify_state(flex).do()

    with allure.step("El servicio es flexibilizado correctamente"):
        action.success()
        flex.solicitar()
        BuscarServiciosFlexibilizadosActionHandler(context).go_to().do(servicio).success(flex)

@allure.feature("Flexibilizacion")
@allure.story("Flexibilizar un servicio")
@allure.title("El usuario flexibiliza un servicio individual entre 31 y 267 dias de vencimiento")
@pytest.mark.parametrize("productos", [
    {
        "P1": (TiposSexo.HEMBRA, TiposRegistro.DEFINITIVO),
        "P2": (TiposSexo.MACHO, TiposRegistro.DEFINITIVO)
    }],
    ids=[
        "P1: Hembra, Definitivo, "
        "P2: Macho, Definitivo"
    ], indirect=True)
@pytest.mark.parametrize("servicio", [
    {
        "Hembras": ["P1"],
        "Machos": ["P2"],
        "Fecha Inicio": now_minus(237),
        "Fecha Fin": now_minus(237),
        "Fecha Carga": now_minus(80),
        "Limita Registro": True,
        "Tipo": TiposServicio.INDIVIDUAL
    }],
    ids=[
        "Servicio Individual con registro limitado, 34 dias de vencimiento y 10kg de multa"
    ], indirect=True)
@pytest.mark.parametrize("usuarios", [
    {
        "U1": TiposPerfil.PRODUCTOR,
    }],
    ids=[
        "Un productor"
    ], indirect=True)
def test_002(context, usuarios, productos, servicio):
    flex = ServicioFlexibilizacion(servicio, dias_esperados=34, multa_esperada=10)
    with allure.step("El productor ingresa al sistema"):
        LoginActionHandler(context).do(usuarios['U1'])
    with allure.step("Busca el servicio y solicita su flexibilizacion"):
        BuscarServiciosAFlexibilizarActionHandler(context).go_to().do(servicio).success(flex)
        action = SolicitarFlexibilizacionServicioActionHandler(context).verify_state(flex).do()

    with allure.step("El servicio es flexibilizado correctamente"):
        action.success()
        flex.solicitar()
        BuscarServiciosFlexibilizadosActionHandler(context).go_to().do(servicio).success(flex)


@allure.feature("Flexibilizacion")
@allure.story("Flexibilizar un servicio")
@allure.title("El usuario flexibiliza un servicio individual "
              "con menos de 30 dias vencido, dos hembras suceptibles a dar cria GA y una no")
@pytest.mark.parametrize("productos", [
    {
        "P1": (TiposSexo.HEMBRA, TiposRegistro.DEFINITIVO),
        "P2": (TiposSexo.MACHO, TiposRegistro.DEFINITIVO),
        "P3": (TiposSexo.HEMBRA, TiposRegistro.DEFINITIVO),
        "P4": (TiposSexo.HEMBRA, TiposRegistro.PREPARATORIO)
    }],
    ids=[
        "P1: Hembra, Definitivo, "
        "P2: Macho, Definitivo, "
        "P3: Hembra, Definitivo, "
        "P4: Hembra, Preparatorio"
    ], indirect=True)
@pytest.mark.parametrize("servicio", [
    {
        "Hembras": ["P1", "P3", "P4"],
        "Machos": ["P2"],
        "Fecha Inicio": now_minus(237),
        "Fecha Fin": now_minus(237),
        "Fecha Carga": now_minus(105),
        "Limita Registro": True,
        "Tipo": TiposServicio.INDIVIDUAL
    }],
    ids=[
        "Servicio Individual con registro limitado, 9 dias de vencimiento y 10kg de multa"
    ], indirect=True)
@pytest.mark.parametrize("usuarios", [
    {
        "U1": TiposPerfil.PRODUCTOR,
    }],
    ids=[
        "Un productor"
    ], indirect=True)
def test_003(context, usuarios, productos, servicio):
    flex = ServicioFlexibilizacion(servicio, dias_esperados=9, multa_esperada=10)
    with allure.step("El productor ingresa al sistema"):
        LoginActionHandler(context).do(usuarios['U1'])
    with allure.step("Busca el servicio y solicita su flexibilizacion"):
        BuscarServiciosAFlexibilizarActionHandler(context).go_to().do(servicio).success(flex)
        action = SolicitarFlexibilizacionServicioActionHandler(context).verify_state(flex).do()

    with allure.step("El servicio es flexibilizado correctamente"):
        action.success()
        flex.solicitar()
        BuscarServiciosFlexibilizadosActionHandler(context).go_to().do(servicio).success(flex)


@allure.feature("Flexibilizacion")
@allure.story("Flexibilizar un servicio")
@allure.title("El usuario flexibiliza un servicio individual "
              "entre 31 y 267 dias vencido, tres hembras suceptibles a dar cria GA y una no")
@pytest.mark.parametrize("productos", [
    {
        "P1": (TiposSexo.HEMBRA, TiposRegistro.DEFINITIVO),
        "P2": (TiposSexo.MACHO, TiposRegistro.DEFINITIVO),
        "P3": (TiposSexo.HEMBRA, TiposRegistro.DEFINITIVO),
        "P4": (TiposSexo.HEMBRA, TiposRegistro.PREPARATORIO),
        "P5": (TiposSexo.HEMBRA, TiposRegistro.CONTROLADO)
    }],
    ids=[
        "P1: Hembra, Definitivo, "
        "P2: Macho, Definitivo, "
        "P3: Hembra, Definitivo, "
        "P4: Hembra, Preparatorio, "
        "P5: Hembra, Controlado"
    ], indirect=True)
@pytest.mark.parametrize("servicio", [
    {
        "Hembras": ["P1", "P3", "P4", "P5"],
        "Machos": ["P2"],
        "Fecha Inicio": now_minus(237),
        "Fecha Fin": now_minus(237),
        "Fecha Carga": now_minus(83),
        "Limita Registro": True,
        "Tipo": TiposServicio.INDIVIDUAL
    }],
    ids=[
        "Servicio Individual con registro limitado, 31 dias de vencimiento y 30kg de multa"
    ], indirect=True)
@pytest.mark.parametrize("usuarios", [
    {
        "U1": TiposPerfil.PRODUCTOR,
    }],
    ids=[
        "Un productor"
    ], indirect=True)
def test_004(context, usuarios, productos, servicio):
    flex = ServicioFlexibilizacion(servicio, dias_esperados=31, multa_esperada=30)
    with allure.step("El productor ingresa al sistema"):
        LoginActionHandler(context).do(usuarios['U1'])
    with allure.step("Busca el servicio y solicita su flexibilizacion"):
        BuscarServiciosAFlexibilizarActionHandler(context).go_to().do(servicio).success(flex)
        action = SolicitarFlexibilizacionServicioActionHandler(context).verify_state(flex).do()

    with allure.step("El servicio es flexibilizado correctamente"):
        action.success()
        flex.solicitar()
        BuscarServiciosFlexibilizadosActionHandler(context).go_to().do(servicio).success(flex)



@allure.feature("Flexibilizacion")
@allure.story("Flexibilizar un servicio")
@allure.title("No se pueden flexibilizar servicios que iniciaron hace mas de 267 dias")
@pytest.mark.parametrize("productos", [
    {
        "P1": (TiposSexo.HEMBRA, TiposRegistro.DEFINITIVO),
        "P2": (TiposSexo.MACHO, TiposRegistro.DEFINITIVO),
    }],
    ids=[
        "P1: Hembra, Definitivo,"
        "P2: Macho, Definitivo"
    ], indirect=True)
@pytest.mark.parametrize("servicio", [
    {
        "Hembras": ["P1"],
        "Machos": ["P2"],
        "Fecha Inicio": now_minus(267),
        "Fecha Fin": now_minus(250),
        "Fecha Carga": now(),
        "Limita Registro": True,
        "Tipo": TiposServicio.INDIVIDUAL
    }],
    ids=[
        "Servicio Individual con registro limitado, con fecha de inicio hace 267 dias"
    ], indirect=True)
@pytest.mark.parametrize("usuarios", [
    {
        "U1": TiposPerfil.PRODUCTOR,
    }],
    ids=[
        "Un productor"
    ], indirect=True)
def test_004(context, usuarios, productos, servicio):
    flex = ServicioFlexibilizacion(servicio, dias_esperados=127, multa_esperada=10)
    with allure.step("El productor ingresa al sistema"):
        LoginActionHandler(context).do(usuarios['U1'])
    with allure.step("Busca el servicio y solicita su flexibilizacion"):
        a = BuscarServiciosAFlexibilizarActionHandler(context).go_to().do(servicio)

    with allure.step("El servicio es flexibilizado correctamente"):
        a.failure(flex)