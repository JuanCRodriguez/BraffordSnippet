from contextlib import contextmanager

from selenium.webdriver.remote.webelement import WebElement

from datacontracts.buscador_flexibilizacion import BuscadorServiciosAFlexbilizarDataContract
from dominio.servicio import TipoServicio, Servicio
from page_objects.base.page.handler import PageHandler
from page_objects.flexibilizacion.solicitudes.props import SolicitudFlexibilizacionServicioPageProps
from page_objects.home.props import HomePageProps


class SolicitudFlexibilizacionServicioPageHandler(PageHandler):
    url = "SolicitudFFRMServicios.aspx"
    _messages = SolicitudFlexibilizacionServicioPageProps.Messages
    _locators = SolicitudFlexibilizacionServicioPageProps.Locators
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
                return i + 2  # +1 por el 0 y +1 por el header de la tabla
        raise Exception("No se encontro el servicio indicado")

    def _informacion_fila(self, fila: int) -> BuscadorServiciosAFlexbilizarDataContract:
        row = self._bp.find_element(self._locators.FILA.format(fila))
        return BuscadorServiciosAFlexbilizarDataContract(
            NOMBRE_CABAÑA=row.find_element(*self._locators.COLUMNA_CABAÑA).text,
            NUMERO_SERVICIO=row.find_element(*self._locators.COLUMNA_NUMERO_SERVICIO).text,
            TIPO_SERVICIO=row.find_element(*self._locators.COLUMNA_TIPO_SERVICIO).text,
            H_EMB=row.find_element(*self._locators.COLUMNA_H_EMB).text,
            DIAS_VENCIDO=row.find_element(*self._locators.COLUMNA_VENCIDO_DIAS).text,
            FECHA_MAXIMA=row.find_element(*self._locators.COLUMNA_FECHA_MAXIMA).text,
            COSTO_MULTA=row.find_element(*self._locators.COLUMNA_COSTO_KG_INML).text,
            FLEXIBILIZADO=row.find_element(*self._locators.CHECK_FLEXIBILIZAR.format(fila)).is_selected()
        )

    def informacion_resultado(self, s: Servicio) -> BuscadorServiciosAFlexbilizarDataContract:
        return self._informacion_fila(
            self._fila_resultado(s)
        )

    def click_check_flexibilizar(self, s: Servicio):
        fila = self._fila_resultado(s)
        self._bp.find_element(self._locators.CHECK_FLEXIBILIZAR.format(fila)).click()

    def solicitar_flexibilizacion(self):
        with self._bp.stale_element(self._locators.TABLA_RESULTADOS):
            self._bp.find_element(self._locators.CHECK_CONDICIONES).click()
            self._bp.find_element(self._locators.BTN_SOLICITAR_FLEXIBILIZACION).click()

    def get_mensaje_ok(self):
        return self._bp.find_element(self._locators.LBL_MENSAJE_OK).text

    def get_numero_servicio_filtro(self):
        return self._bp.find_element(self._locators.TXT_NUMERO_SERVICIO).get_attribute('value')

    def hay_resultados(self):
        tabla = self._bp.find_element(self._locators.TABLA_RESULTADOS)
        primer_row = tabla.find_element(*self._locators.FILA.format(1))
        if primer_row.text == self._messages.LBL_SIN_RESULTADOS:
            return False
        # Si no hay resultados no se ven el check de condiciones y el boton
        self._bp.find_element(self._locators.CHECK_CONDICIONES)
        self._bp.find_element(self._locators.BTN_SOLICITAR_FLEXIBILIZACION)
        return True

    def ir_home(self):
        self._bp.find_element(self._locators.LOGO_HOME).click()
