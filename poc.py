# from datetime import datetime
#
# from selenium.webdriver.chrome.options import Options
#
# from db.conn.mssql.conn import MSSQLConnection
# from db.schema.dbo.cabaña.handler import CabañaHandler, CabañaDireccionRelationBuilder, CabañaTelefonoRelationBuilder, \
#     CabañaEmailRelationBuilder
# from db.schema.dbo.direccion.handler import DireccionHandler
# from db.schema.dbo.email.handler import EmailHandler
# from db.schema.dbo.establecimiento.handler import EstablecimientoHandler, EstablecimientoEmailRelationBuilder, \
#     EstablecimientoDireccionRelationBuilder, EstablecimientoTelefonoRelationBuilder
# from db.schema.dbo.hembra_en_servicio.handler import HembraEnServicioHandler
# from db.schema.dbo.machosenservicio.handler import MachosEnServicioHandler
# from db.schema.dbo.medicion.handler import MedicionHandler
# from db.schema.dbo.persona_juridica.handler import PersonaJuridicaHandler, PersonaJuridicaDireccionRelationBuilder, \
#     PersonaJuridicaTelefonoRelationBuilder, PersonaJuridicaEmailRelationBuilder
# from db.schema.dbo.producto.handler import ProductoHandler, ProductoEstablecimientoRelationBuilder, \
#     ProductoCabañaRelationBuilder
# from db.schema.dbo.sec_profile.handler import SecProfileHandler, SecProfileUserRelationBuilder
# from db.schema.dbo.sec_user.handler import SecUserHandler
# from db.schema.dbo.servicio.handler import ServicioHandler
# from db.schema.dbo.telefono.handler import TelefonoHandler
# from db.schema.dbo.tipo_color.handler import TipoColorHandler
# from db.schema.dbo.tipo_cuerno.handler import TipoCuernoHandler
# from db.schema.dbo.tipo_denticion.handler import TipoDenticionHandler
# from db.schema.dbo.tipo_parto.handler import TipoPartoHandler
# from db.schema.dbo.tipo_pompe.handler import TipoPompeHandler
# from db.schema.dbo.tipo_raza.handler import TipoRazaHandler
# from db.schema.dbo.tipo_registro.handler import TipoRegistroHandler
# from db.schema.dbo.tipo_servicio.handler import TipoServicioHandler
# from db.schema.dbo.tipo_sexo.handler import TipoSexoHandler
# from db.schema.dbo.tipo_variedad.handler import TipoVariedadHandler
# from db.schema.dbo.usuario.handler import UsuarioHandler, UsuarioEmailRelationBuilder
# from dominio.cabaña import Cabaña
# from dominio.contacto.direccion import Direccion
# from dominio.contacto.email import Email
# from dominio.contacto.telefono import Telefono
# from dominio.enums.tipos import TiposPerfil, TiposSexo, TiposRaza, TiposRegistro, TiposColor, TiposCuerno, \
#     TiposVariedad, TiposParto, TiposPompe, TiposDenticion, TiposServicio
# from dominio.establecimiento import Establecimiento
# from dominio.mediciones import Mediciones
# from dominio.perfil import Perfil
# from dominio.producto import Producto, Raza, Registro, Color, Cuerno, Variedad, Parto, Pompe, Sexo, Denticion
# from dominio.productor import Productor
# from dominio.provincia import Provincia
# from dominio.servicio import Servicio, TipoServicio
# from dominio.usuario import Usuario
# from page_objects.base.driver.factory import LocalDriverFactory
# from page_objects.base.driver.handler import DriverHandler
# from page_objects.base.page.factory import PageHandlerFactory
#
# from page_objects.flexibilizacion.solicitudes.servicios import SolicitudFlexibilizacionServicioPageHandler
# from page_objects.home.home import HomePageHandler
# from page_objects.login.login import LoginPageHandler
# from utils.date import now, now_plus, now_minus
# #
# count = 29
# # region db
# db = MSSQLConnection("ola")
# # db = MockConnection()
# # region Productor
# productor = Productor(f"Razon {count}", "Cuit", 569, "Obs de prueba")
# productor.id = PersonaJuridicaHandler(db).create(productor)
#
# direccion_p = Direccion(
#     Provincia(1, "CAPITAL FEDERAL"), "Localidad P", "Calle P",
#     "Cp P", "Nro Puerta P", "Piso P",
#     "Departamento P", "Oficina P", "Observacion P", "Parti2 P", None, None)
# direccion_p.id = DireccionHandler(db).create(direccion_p)
#
# telefono_p = Telefono("cod pais P", "cod int P", "num P", "int P", "observacion P", None, None)
# telefono_p.id = TelefonoHandler(db).create(telefono_p)
#
# mail_p = Email("Email P", 0, 0, None)
# mail_p.id = EmailHandler(db).create(mail_p)
#
# PersonaJuridicaDireccionRelationBuilder(db).create(direccion_p, productor)
# PersonaJuridicaTelefonoRelationBuilder(db).create(telefono_p, productor)
# PersonaJuridicaEmailRelationBuilder(db).create(mail_p, productor)
#
# # endregion
#
# # region Cabaña
# cabaña = Cabaña(f"Cabaña {count}", "PRM", "PRH", productor, 999)
# cabaña.id = CabañaHandler(db).create(cabaña)
#
# direccion_c = Direccion(
#     Provincia(1, "CAPITAL FEDERAL"), "Localidad C", "Calle C",
#     "Cp C", "Nro Puerta C", "Piso C",
#     "Departamento C", "Oficina C", "Observacion C", "Parti2 C", None, None)
# direccion_c.id = DireccionHandler(db).create(direccion_c)
#
# telefono_c = Telefono("cod pais C", "cod int C", "num C", "int C", "obs C", None, None)
# telefono_c.id = TelefonoHandler(db).create(telefono_c)
#
# mail_c = Email("Email C", 0, 0, None)
# mail_c.id = EmailHandler(db).create(mail_c)
#
# CabañaDireccionRelationBuilder(db).create(direccion_c, cabaña)
# CabañaTelefonoRelationBuilder(db).create(telefono_c, cabaña)
# CabañaEmailRelationBuilder(db).create(mail_c, cabaña)
# # endregion
#
# # region Usuario
# rol = Perfil(TiposPerfil.PRODUCTOR, None)
#
# handler = SecProfileHandler(db)
# with handler.fetch(rol) as q:
#     q: SecProfileHandler
#     q.with_descripcion()
# rol.id = handler.results[0].id_profile
#
# email_usuario = Email("jrodriguez+usuario@cys.com.ar", 0, 0, None)
#
# usuario = Usuario("Usuario", "De prueba", f"usuario{count}",
#                   cabaña, email_usuario, rol)
# usuario.id_sec = SecUserHandler(db).create(usuario)
# SecProfileUserRelationBuilder(db).create(usuario, usuario.rol)
# usuario.id_usuario = UsuarioHandler(db).create(usuario)
# usuario.email.id = EmailHandler(db).create(usuario.email)
# UsuarioEmailRelationBuilder(db).create(usuario.email, usuario)
# # endregion
#
# # region Establecimiento
# email_e = Email("jrodriguez+establecimiento@cys.com.ar", 0, 0, None)
# telefono_e = Telefono("cod pais E", "cod int E", "num E", "int E", "obs E", None, None)
# direccion_e = Direccion(
#     Provincia(1, "CAPITAL FEDERAL"), "Localidad E", "Calle E",
#     "Cp E", "Nro Puerta E", "Piso E",
#     "Departamento E", "Oficina E", "Observacion E", "Parti2 E", None, None)
# establecimiento = Establecimiento(f"Establecimiento 1 de {count}", cabaña, "Renspa", email_e, telefono_e,
#                                   direccion_e)
#
# establecimiento.id = EstablecimientoHandler(db).create(establecimiento)
# establecimiento.email.id = EmailHandler(db).create(establecimiento.email)
# establecimiento.telefono.id = TelefonoHandler(db).create(establecimiento.telefono)
# establecimiento.direccion.id = DireccionHandler(db).create(establecimiento.direccion)
# EstablecimientoEmailRelationBuilder(db).create(email_e, establecimiento)
# EstablecimientoDireccionRelationBuilder(db).create(direccion_e, establecimiento)
# EstablecimientoTelefonoRelationBuilder(db).create(telefono_e, establecimiento)
# # endregion
#
# # region producto 1
# # porque tiene tantas cosas esta mierda dios ayuda
# denticion = Denticion(None, TiposDenticion.DL.value)
# handler = TipoDenticionHandler(db)
# with handler.fetch(denticion) as q:
#     q: TipoDenticionHandler
#     q.with_descripcion()
# denticion.id = handler.results[0].id
# # estoy orgulloso de lo feo que es esto
# mediciones = Mediciones(*[None for _ in range(14)], denticion, None, 0, *[None for _ in range(4)])
# mediciones.id = MedicionHandler(db).create(mediciones)
#
# # dep = DEP(*[None for _ in range(25)]) todo: usar esto algun dia
# # todo: generic fetcher o algo del estilo,
# #  recibe un handler y una query (uno o varios lambdas del estilo q -> q.with_*())
# #  podria recibir un callback para hacer algo con esos resultados, o exponerlos como hace el handler :thinking:
# raza = Raza(None, TiposRaza.BRAFORD)
# handler = TipoRazaHandler(db)
# with handler.fetch(raza) as q:
#     q: TipoRazaHandler
#     q.with_descripcion()
# raza.id = handler.results[0].id
#
# registro = Registro(None, TiposRegistro.DEFINITIVO)
# handler = TipoRegistroHandler(db)
# with handler.fetch(registro) as q:
#     q: TipoRegistroHandler
#     q.with_descripcion()
# registro.id = handler.results[0].id
#
# color = Color(None, TiposColor.BARCINO)
# handler = TipoColorHandler(db)
# with handler.fetch(color) as q:
#     q: TipoColorHandler
#     q.with_nombre()
# color.id = handler.results[0].id
#
# cuerno = Cuerno(None, TiposCuerno.ASTADO)
# handler = TipoCuernoHandler(db)
# with handler.fetch(cuerno) as q:
#     q: TipoCuernoHandler
#     q.with_descripcion()
# cuerno.id = handler.results[0].id
#
# variedad = Variedad(None, TiposVariedad.BRAFORD)
# handler = TipoVariedadHandler(db)
# with handler.fetch(variedad) as q:
#     q: TipoVariedadHandler
#     q.with_descripcion()
# variedad.id = handler.results[0].id
#
# parto = Parto(None, TiposParto.NORMAL)
# handler = TipoPartoHandler(db)
# with handler.fetch(parto) as q:
#     q: TipoPartoHandler
#     q.with_descripcion()
# parto.id = handler.results[0].id
#
# pompe = Pompe(None, TiposPompe.SIN_ANALISIS)
# handler = TipoPompeHandler(db)
# with handler.fetch(pompe) as q:
#     q: TipoPartoHandler
#     q.with_descripcion()
# pompe.id = handler.results[0].id
#
# sexo = Sexo(None, TiposSexo.MACHO)
# handler = TipoSexoHandler(db)
# with handler.fetch(sexo) as q:
#     q: TipoSexoHandler
#     q.with_descripcion()
# sexo.id = handler.results[0].id
#
# producto1 = Producto("RP", f"macho {count}", "Apodo2", "tat",
#                     raza, registro, color, cuerno,
#                     variedad, sexo, 12545 + count, pompe, mediciones, None,
#                     datetime.now(), parto, establecimiento)
# producto1.id = ProductoHandler(db).create(producto1)
# ProductoCabañaRelationBuilder(db).create(cabaña, producto1)
# ProductoEstablecimientoRelationBuilder(db).create(producto1, establecimiento)
#
# # endregion
#
# # region producto 2
#
# denticion = Denticion(None, TiposDenticion.DL)
# handler = TipoDenticionHandler(db)
# with handler.fetch(denticion) as q:
#     q: TipoDenticionHandler
#     q.with_descripcion()
# denticion.id = handler.results[0].id
# # estoy orgulloso de lo feo que es esto
# mediciones = Mediciones(*[None for _ in range(14)], denticion, None, 0, *[None for _ in range(4)])
# mediciones.id = MedicionHandler(db).create(mediciones)
#
# raza = Raza(None, TiposRaza.BRAFORD)
# handler = TipoRazaHandler(db)
# with handler.fetch(raza) as q:
#     q: TipoRazaHandler
#     q.with_descripcion()
# raza.id = handler.results[0].id
#
# registro = Registro(None, TiposRegistro.DEFINITIVO)
# handler = TipoRegistroHandler(db)
# with handler.fetch(registro) as q:
#     q: TipoRegistroHandler
#     q.with_descripcion()
# registro.id = handler.results[0].id
#
# color = Color(None, TiposColor.BARCINO)
# handler = TipoColorHandler(db)
# with handler.fetch(color) as q:
#     q: TipoColorHandler
#     q.with_nombre()
# color.id = handler.results[0].id
#
# cuerno = Cuerno(None, TiposCuerno.ASTADO)
# handler = TipoCuernoHandler(db)
# with handler.fetch(cuerno) as q:
#     q: TipoCuernoHandler
#     q.with_descripcion()
# cuerno.id = handler.results[0].id
#
# variedad = Variedad(None, TiposVariedad.BRAFORD)
# handler = TipoVariedadHandler(db)
# with handler.fetch(variedad) as q:
#     q: TipoVariedadHandler
#     q.with_descripcion()
# variedad.id = handler.results[0].id
#
# parto = Parto(None, TiposParto.NORMAL)
# handler = TipoPartoHandler(db)
# with handler.fetch(parto) as q:
#     q: TipoPartoHandler
#     q.with_descripcion()
# parto.id = handler.results[0].id
#
# pompe = Pompe(None, TiposPompe.SIN_ANALISIS)
# handler = TipoPompeHandler(db)
# with handler.fetch(pompe) as q:
#     q: TipoPartoHandler
#     q.with_descripcion()
# pompe.id = handler.results[0].id
#
# sexo = Sexo(None, TiposSexo.HEMBRA)
# handler = TipoSexoHandler(db)
# with handler.fetch(sexo) as q:
#     q: TipoSexoHandler
#     q.with_descripcion()
# sexo.id = handler.results[0].id
#
# producto2 = Producto(f"RP{count}", f"hembra {count}", f"Apodo{count}", f"tat{count}",
#                     raza, registro, color, cuerno,
#                     variedad, sexo, 12545 + count, pompe, mediciones, None,
#                     datetime.now(), parto, establecimiento)
# producto2.id = ProductoHandler(db).create(producto2)
# ProductoCabañaRelationBuilder(db).create(cabaña, producto2)
# ProductoEstablecimientoRelationBuilder(db).create(producto2, establecimiento)
# # endregion
# tipo_servicio = TipoServicio(None, TiposServicio.INDIVIDUAL)
# handler = TipoServicioHandler(db)
# with handler.fetch(tipo_servicio) as q:
#     q: TipoServicioHandler
#     q.with_nombre()
# tipo_servicio.id = handler.results[0].id
#
# servicio = Servicio(tipo_servicio, True,
#                     fecha_inicio=now_minus(250),
#                     fecha_fin=now_plus(1),
#                     fecha_carga=now_minus(250),
#                     cabaña=cabaña)
# servicio.id = ServicioHandler(db).create(servicio)
# servicio.agregar_hembra(producto2)
# servicio.agregar_macho(producto1)
# for hembra in servicio.hembras:
#     hembra.id = HembraEnServicioHandler(db).create(hembra)
# for macho in servicio.machos:
#     macho.id = MachosEnServicioHandler(db).create(macho)
#
# db.commit()
# # endregion
#
#
# # region selenium
#
# options = Options()
# options.headless = False
# options.add_argument('--window-size=1920,1080')
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--lang=es_AR")
# options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
# options.set_capability('version', "83.0.4103.39")
# options.set_capability('enableLog', True)
#
# driver_handler = DriverHandler("http://localhost:51939/Web/Login.aspx",
#                               LocalDriverFactory("Chrome"))
# driver_handler.build_main_driver()
#
# factory = PageHandlerFactory()
# factory.set_driver(driver_handler.main_driver)
#
# page: LoginPageHandler = factory.get_login()
# page.iniciar_sesion(usuario)
#
# page: HomePageHandler = factory.create(HomePageHandler)
# page.ir_servicios_a_flexibilizar()
#
# page: SolicitudFlexibilizacionServicioPageHandler = factory.create(SolicitudFlexibilizacionServicioPageHandler)
# page.with_numero_servicio(servicio.id)
# page.click_buscar()
# print(page.informacion_resultado(servicio))
# page.click_check_flexibilizar(servicio)
# page.solicitar_flexibilizacion()
# print(page.get_mensaje_ok())
# breakpoint()
# # endregion
#
# driver_handler.quit()
from datetime import datetime, timedelta

from utils.date import now_minus, now

"""
        "Fecha Inicio": now_minus(267),
        "Fecha Fin": now_minus(250),
        "Fecha Carga": now(),"""

fecha_inicio = now_minus(266)
fecha_carga = now_minus(104)
fecha_fin = now_minus(234)

fecha_obtenida = fecha_fin + timedelta(days=122)
dias_vencido = (abs(fecha_carga - fecha_obtenida).days) - 1
print(dias_vencido)