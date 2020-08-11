from actions.base.base import BaseActionHandler
from dominio.usuario import Usuario
from page_objects.home.home import HomePageHandler
from page_objects.login.login import LoginPageHandler


class LoginActionHandler(BaseActionHandler):

    def do(self, usuario: Usuario):
        self._page: LoginPageHandler = self.page_factory.get_login()
        self._page.iniciar_sesion(usuario)
        return self