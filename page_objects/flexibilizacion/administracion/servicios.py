from contextlib import contextmanager

from selenium.webdriver.remote.webelement import WebElement

from datacontracts.buscador_flexibilizacion import BuscadorServiciosAFlexbilizarDataContract, \
    BuscadorServiciosFlexibilizadosDataContract
from dominio.servicio import Servicio
from page_objects.base.page.handler import PageHandler
from page_objects.flexibilizacion.administracion.props import ServiciosFlexibilizadosPageProps

class ServiciosFlexibilizadosPageHandler(PageHandler):
    url = "AdministracionFFRMServicios.aspx"
    _messages = ServiciosFlexibilizadosPageProps.Messages
    _locators = ServiciosFlexibilizadosPageProps.Locators
    _initial_validations = {
        _locators.LBL_TITULO_HOME: _messages.TITULO_HOME,
    }
    _initial_elements = [_locators.BTN_BUSCAR, _locators.BTN_EXPORTAR]

    def click_buscar(self):
        self._bp.find_element(self._locators.BTN_BUSCAR).click()

    def with_tipo_servicio(self, o: str):
        self._bp.find_select(self._locators.SELECT_TIPO_SERVICIO).select_by_visible_text(o)

    def with_numero_servicio(self, n: int):
        self._bp.find_element(self._locators.TXT_NUMERO_SERVICIO).send_keys(n)

    def _fila_resultado(self, s: Servicio):
        for i, e in enumerate(self._bp.find_elements(self._locators.FILAS)):
            e: WebElement
            if e.find_element(*self._locators.COLUMNA_NUMERO_SERVICIO).text == str(s.id):
                return i + 2 # +1 por el 0 y +1 por el header de la tabla
        raise Exception("No se encontro el servicio indicado")

    def _informacion_fila(self, fila: int) -> BuscadorServiciosFlexibilizadosDataContract:
        row = self._bp.find_element(self._locators.FILA.format(fila))
        return BuscadorServiciosFlexibilizadosDataContract(
            NOMBRE_CABAÑA=row.find_element(*self._locators.COLUMNA_CABAÑA).text,
            NUMERO_SERVICIO=row.find_element(*self._locators.COLUMNA_NUMERO_SERVICIO).text,
            TIPO_SERVICIO=row.find_element(*self._locators.COLUMNA_TIPO_SERVICIO).text,
            H_EMB=row.find_element(*self._locators.COLUMNA_H_EMB).text,
            DIAS_VENCIDO=row.find_element(*self._locators.COLUMNA_VENCIDO_DIAS).text,
            FECHA_SOLICITUD=row.find_element(*self._locators.COLUMNA_FECHA_SOLICITUD).text,
            COSTO_MULTA=row.find_element(*self._locators.COLUMNA_COSTO_KG_INML).text,
            FACTURADO=row.find_element(*self._locators.CHK_FACTURADO.format(fila)).is_selected()
        )

    def informacion_resultado(self, s: Servicio) -> BuscadorServiciosFlexibilizadosDataContract:
        return self._informacion_fila(
            self._fila_resultado(s)
        )

    def click_check_facturar(self, s: Servicio):
        fila = self._fila_resultado(s)
        self._bp.find_element(self._locators.CHK_FACTURADO.format(fila)).click()

    def guardar(self):
        with self._bp.stale_element(self._locators.TABLA):
            self._bp.find_element(self._locators.BTN_GUARDAR).click()

    def get_mensaje_ok(self):
        return self._bp.find_element(self._locators.LBL_MENSAJE_OK).text