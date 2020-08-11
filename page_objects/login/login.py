from selenium.common.exceptions import TimeoutException

from dominio.usuario import Usuario
from page_objects.base.page.handler import PageHandler
from page_objects.login.props import LoginPageProps


class LoginPageHandler(PageHandler):
    url = "Login.aspx"
    _messages = LoginPageProps.Messages
    _locators = LoginPageProps.Locators
    _initial_validations = {_locators.TITULO_PANEL: _messages.TITULO_PANEL}
    _initial_elements = [_locators.BTN_INICIAR_SESION]

    def iniciar_sesion(self, usuario: Usuario):
        self._completar_credenciales_login(usuario.username, usuario.password)
        self.click_login()

    def _completar_credenciales_login(self, username, contra):
        self._bp.find_element(self._locators.TXT_USER).send_keys(username)
        self._bp.element_text_equals(self._locators.TXT_USER, username)
        self._bp.find_element(self._locators.TXT_CONTRASEÑA).send_keys(contra)
        self._bp.element_text_equals(self._locators.TXT_CONTRASEÑA, contra)

    def redirigir(self):
        try:
            self.next_page = None
        except TimeoutException as e:
            raise Exception("No se pudo redirigir a la pagina indicada", e)

    def click_login(self):
        self._bp.find_element(self._locators.BTN_INICIAR_SESION).click()
