from typing import Type

from page_objects.base.page.handler import PageHandler
from page_objects.flexibilizacion.administracion.servicios import ServiciosFlexibilizadosPageHandler
from page_objects.flexibilizacion.solicitudes.servicios import SolicitudFlexibilizacionServicioPageHandler
from page_objects.home.home import HomePageHandler
from page_objects.login.login import LoginPageHandler


class PageHandlerFactory(object):

    def __init__(self, driver):
        self.driver = driver

    def create(self, class_: Type[PageHandler]):
        if class_ in self.__paginas:
            return self._create(class_)
        raise ValueError(f"{class_.__class__} no es un PageHandler valido")

    def get_login(self) -> LoginPageHandler:
        return self._create(LoginPageHandler)

    def _create(self, class_):
        return class_(self.driver)

    def set_driver(self, new_driver):
        self.driver = new_driver

    __paginas = [
        LoginPageHandler,
        HomePageHandler,
        SolicitudFlexibilizacionServicioPageHandler,
        ServiciosFlexibilizadosPageHandler
    ]
