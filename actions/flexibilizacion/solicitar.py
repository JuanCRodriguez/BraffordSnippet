from actions.base.base import BaseActionHandler
from datacontracts.buscador_flexibilizacion import BuscadorServiciosAFlexbilizarDataContract
from dominio.flexibilizacion import ServicioFlexibilizacion
from page_objects.flexibilizacion.solicitudes.servicios import SolicitudFlexibilizacionServicioPageHandler


class SolicitarFlexibilizacionServicioActionHandler(BaseActionHandler):
    _f: ServicioFlexibilizacion = None
    _page: SolicitudFlexibilizacionServicioPageHandler

    def verify_state(self, flexibilizacion: ServicioFlexibilizacion):
        self._page = self.page_factory.create(SolicitudFlexibilizacionServicioPageHandler)
        obtenido = self._page.informacion_resultado(flexibilizacion.servicio)
        esperado = BuscadorServiciosAFlexbilizarDataContract.from_domain(flexibilizacion)
        self._assert.that(esperado).equals(obtenido)
        self._f = flexibilizacion
        return self

    def do(self):
        if self._f is None:
            raise ValueError()
        self._page.click_check_flexibilizar(self._f.servicio)
        self._page.solicitar_flexibilizacion()
        return self

    def success(self):
        self._assert\
            .that("Se flexibilizaron los servicios correctamente")\
            .equals(self._page.get_mensaje_ok())
        self._page.ir_home()