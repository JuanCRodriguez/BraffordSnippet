from actions.base.base import BaseActionHandler
from datacontracts.buscador_flexibilizacion import BuscadorServiciosAFlexbilizarDataContract, \
    BuscadorServiciosFlexibilizadosDataContract
from dominio.flexibilizacion import ServicioFlexibilizacion
from dominio.servicio import Servicio
from page_objects.flexibilizacion.administracion.servicios import ServiciosFlexibilizadosPageHandler
from page_objects.flexibilizacion.solicitudes.servicios import SolicitudFlexibilizacionServicioPageHandler
from page_objects.home.home import HomePageHandler


class BuscarServiciosAFlexibilizarActionHandler(BaseActionHandler):

    def go_to(self):
        self._page: HomePageHandler = self.page_factory.create(HomePageHandler)
        self._page.ir_servicios_a_flexibilizar()
        return self

    def do(self, s: Servicio):
        self._page = self.page_factory.create(SolicitudFlexibilizacionServicioPageHandler)
        self._page: SolicitudFlexibilizacionServicioPageHandler
        self._page.with_numero_servicio(s.id)
        self._page.click_buscar()
        return self

    def success(self, flexibilizacion: ServicioFlexibilizacion):
        self._page: SolicitudFlexibilizacionServicioPageHandler
        obtenido = self._page.informacion_resultado(flexibilizacion.servicio)
        esperado = BuscadorServiciosAFlexbilizarDataContract.from_domain(flexibilizacion)
        self._assert.that(esperado).equals(obtenido)

    def failure(self, f: ServicioFlexibilizacion):
        self._page: SolicitudFlexibilizacionServicioPageHandler
        self._assert.that(self._page.get_numero_servicio_filtro()).equals(str(f.servicio.id))
        self._assert.that(self._page.hay_resultados()).equals(False)

class BuscarServiciosFlexibilizadosActionHandler(BaseActionHandler):

    def go_to(self):
        self._page: HomePageHandler = self.page_factory.create(HomePageHandler)
        self._page.ir_servicios_flexibilizados()
        return self

    def do(self, s: Servicio):
        self._page = self.page_factory.create(ServiciosFlexibilizadosPageHandler)
        self._page: ServiciosFlexibilizadosPageHandler
        self._page.with_numero_servicio(s.id)
        self._page.click_buscar()
        return self

    def success(self, flexibilizacion: ServicioFlexibilizacion):
        self._page: ServiciosFlexibilizadosPageHandler
        obtenido = self._page.informacion_resultado(flexibilizacion.servicio)
        esperado = BuscadorServiciosFlexibilizadosDataContract.from_domain(flexibilizacion)
        self._assert.that(esperado).equals(obtenido)