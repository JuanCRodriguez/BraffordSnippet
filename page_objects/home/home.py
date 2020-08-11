from page_objects.base.page.handler import PageHandler
from page_objects.home.props import HomePageProps

class HomePageHandler(PageHandler):
    url = "Home.aspx"
    _messages = HomePageProps.Messages
    _locators = HomePageProps.Locators
    _initial_validations = {
        _locators.LBL_TITULO_HOME: _messages.TITULO_HOME,
        _locators.DROPDOWN.format(HomePageProps.Dropdowns.PRODUCTOS): _messages.TITULO_DROPDOWN_PRODUCTOS,
        _locators.DROPDOWN.format(HomePageProps.Dropdowns.FLEXIBILIZACION): _messages.TITULO_DROPDOWN_FLEXIBILIZACION
    }

    def ir_servicios_a_flexibilizar(self):
        self._ir_a_dropdown(HomePageProps.Dropdowns.FLEXIBILIZACION)
        self._ir_a_sub_menu(*HomePageProps.SubMenues.Flexibilizacion.SOLICITUDES_SERVICIOS)

    def ir_servicios_flexibilizados(self):
        self._ir_a_dropdown(HomePageProps.Dropdowns.FLEXIBILIZACION)
        self._ir_a_sub_menu(*HomePageProps.SubMenues.Flexibilizacion.ADMINISTRACION_SERVICIOS)

    def _ir_a_dropdown(self, n):
        self._bp.find_element(self._locators.DROPDOWN.format(n)).click()
        self._bp.find_element(self._locators.MENU_DROPDOWN)

    def _ir_a_sub_menu(self, x, y):
        with self._bp.stale_element(self._locators.MENU_DROPDOWN):
            self._bp.find_element(self._locators.LBL_OPCION_SUB_MENU.format(x, y)).click()
