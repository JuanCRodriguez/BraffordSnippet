from dataclasses import dataclass

from selenium.webdriver.common.by import By

from page_objects.base.page.base_page import Locator


class ServiciosFlexibilizadosPageProps:

    class ColumnasTabla:
        CABAÑA = 1
        NUMERO_SERVICIO = 2
        TIPO_SERVICIO = 3
        H_EMB = 4
        VENCIDO_POR_DIAS = 5
        FECHA_DE_SOLICITUD = 6
        COSTO_EN_KG = 7
        FACTURADO = 7
        REVERTIR = 8

    class Messages:
        TITULO_HOME = "Administración de Servicios Flexibilizados"

    class Locators:
        BTN_GUARDAR = Locator(By.ID, "ctl00_Contenido_lnkGuardar")
        SELECT_TIPO_SERVICIO = Locator(By.ID, "ctl00_Contenido_ddlTipoServicio")
        BTN_EXPORTAR = Locator(By.ID, "ctl00_Contenido_lnkExportarBusqueda")
        LBL_TITULO_HOME = Locator(By.CSS_SELECTOR, "h2 > span:nth-of-type(2)")
        TXT_NUMERO_SERVICIO = Locator(By.ID, "ctl00_Contenido_nroServicio")
        BTN_BUSCAR = Locator(By.ID, "ctl00_Contenido_btnBuscar")
        TABLA = Locator(By.ID, "ctl00_Contenido_gvServicioFlexibilizado")
        FILAS = Locator(By.CSS_SELECTOR, "tbody > tr:not(:first-child)")
        FILA = Locator(By.CSS_SELECTOR, "tbody > tr:nth-of-type({0})")
        CHK_FACTURADO = Locator(By.ID, "ctl00_Contenido_gvServicioFlexibilizado_ctl{:02}_chkFacturado")
        CHK_REVERTIR = Locator(By.ID, "ctl00_Contenido_gvServicioFlexibilizado_ctl{:02}_chkRevertirFlexibilizacion")
        COLUMNA_CABAÑA = Locator(By.CSS_SELECTOR, f"td:nth-of-type(1)")
        COLUMNA_NUMERO_SERVICIO = Locator(By.CSS_SELECTOR, "td:nth-of-type(2) > a")
        COLUMNA_TIPO_SERVICIO = Locator(By.CSS_SELECTOR, "td:nth-of-type(3)")
        COLUMNA_H_EMB = Locator(By.CSS_SELECTOR, "td:nth-of-type(4)")
        COLUMNA_VENCIDO_DIAS = Locator(By.CSS_SELECTOR, "td:nth-of-type(5)")
        COLUMNA_FECHA_SOLICITUD = Locator(By.CSS_SELECTOR, "td:nth-of-type(6)")
        COLUMNA_COSTO_KG_INML = Locator(By.CSS_SELECTOR, "td:nth-of-type(7)")