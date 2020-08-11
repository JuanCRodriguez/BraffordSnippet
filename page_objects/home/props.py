from selenium.webdriver.common.by import By

from page_objects.base.page.base_page import Locator


class HomePageProps:
    class Messages:
        TITULO_HOME = "Bienvenido"
        TITULO_DROPDOWN_PRODUCTOS = "Productos"
        TITULO_DROPDOWN_FLEXIBILIZACION = "Flexibilización"

    class Locators:
        LBL_TITULO_HOME = Locator(By.CSS_SELECTOR, "h2 > span:nth-of-type(2)")
        DROPDOWN = Locator(By.CSS_SELECTOR, "ul:nth-of-type({0}) > li.mega-dropdown > a")
        MENU_DROPDOWN = Locator(By.CSS_SELECTOR, ".open .mega-dropdown-menu.row")
        LBL_TITULO_SUB_MENU = Locator(By.CSS_SELECTOR, ".open ul:nth-of-type({0}) .dropdown-header")
        LBL_OPCION_SUB_MENU = Locator(By.CSS_SELECTOR,".open li:nth-of-type({0}) "
                                                      "li:not(.dropdown-header):nth-of-type({1}) > a")
    class Dropdowns:
        PRODUCTOS = 1
        FLEXIBILIZACION = 7

    class SubMenues:
        class Flexibilizacion:
            SOLICITUDES_SERVICIOS = (1, 2) # (x, y)
            SOLICITUDES_NACIMIENTOS = (1, 3)
            ADMINISTRACION_SERVICIOS = (2, 2)
            ADMINISTRACION_NACIMIENTOS = (2, 3)