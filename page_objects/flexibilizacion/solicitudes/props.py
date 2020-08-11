from dataclasses import dataclass

from selenium.webdriver.common.by import By

from page_objects.base.page.base_page import Locator


class SolicitudFlexibilizacionServicioPageProps:

    class ColumnasTabla:
        CABAÑA = 1
        NUMERO_SERVICIO = 2
        TIPO_SERVICIO = 3
        H_EMB = 4
        VENCIDO_POR_DIAS = 5
        FECHA_MAXIMA_FLEXIBILIZACION = 6
        COSTO_EN_KG = 7
        SOLICITAR_FLEXIBILIZACION = 7

    class Messages:
        TITULO_HOME = "Solicitud de Flexibilización de Plazos con Multa por Mora - Servicios"
        LBL_SIN_RESULTADOS = "La búsqueda no ha encontrado ningún resultado"

    class Locators:
        LOGO_HOME = Locator(By.CSS_SELECTOR, ".navbar-brand")
        LBL_TITULO_HOME = Locator(By.CSS_SELECTOR, "h2 > span:nth-of-type(2)")
        SELECT_CABAÑA = Locator(By.ID, "ctl00_Contenido_ddlCabania")
        SELECT_TIPO_SERVICIO = Locator(By.ID, "ctl00_Contenido_ddlTipoServicio")
        TXT_NUMERO_SERVICIO = Locator(By.ID, "ctl00_Contenido_nroServicio")
        TXT_OCURRIDO_DESDE = Locator(By.ID, "ctl00_Contenido_calOcurridoDesde_txtFecha")
        TXT_OCURRIDO_HASTA = Locator(By.ID, "ctl00_Contenido_calOcurridoHasta_txtFecha")
        BTN_BUSCAR = Locator(By.ID, "ctl00_Contenido_btnBuscar")
        BTN_EXPORTAR = Locator(By.ID, "ctl00_Contenido_lnkExportarBusqueda")
        TABLA_RESULTADOS = Locator(By.ID, "ctl00_Contenido_gvServicio")
        FILAS = Locator(By.CSS_SELECTOR, "tbody > tr:not(:first-child)")
        FILA = Locator(By.CSS_SELECTOR, "tbody > tr:nth-of-type({0})")
        COLUMNA_CABAÑA = Locator(By.CSS_SELECTOR, f"td:nth-of-type(1)")
        COLUMNA_NUMERO_SERVICIO = Locator(By.CSS_SELECTOR, "td:nth-of-type(2) > a")
        COLUMNA_TIPO_SERVICIO = Locator(By.CSS_SELECTOR, "td:nth-of-type(3)")
        COLUMNA_H_EMB = Locator(By.CSS_SELECTOR, "td:nth-of-type(4)")
        COLUMNA_VENCIDO_DIAS = Locator(By.CSS_SELECTOR, "td:nth-of-type(5)")
        COLUMNA_FECHA_MAXIMA = Locator(By.CSS_SELECTOR, "td:nth-of-type(6)")
        COLUMNA_COSTO_KG_INML = Locator(By.CSS_SELECTOR, "td:nth-of-type(7)")
        CHECK_FLEXIBILIZAR = Locator(By.ID, "ctl00_Contenido_gvServicio_ctl{0:02}_chkAgregarQuitar")
        FILA_COLUMNA_TABLA = Locator(By.CSS_SELECTOR, "tbody > tr:nth-of-type({0}) > td:nth-of-type({1})")
        NUMERO_SERVICIO_EN_RESULTADOS = Locator(By.CSS_SELECTOR, "a[href$='?id={0}']")
        CHECK_CONDICIONES = Locator(By.ID, "ctl00_Contenido_chkAceptarCondiciones")
        BTN_SOLICITAR_FLEXIBILIZACION = Locator(By.ID, "ctl00_Contenido_lnkSolicitar")
        LBL_MENSAJE_OK = Locator(By.ID, "ctl00_Contenido_UCNotifier_lbMensajeOk")
