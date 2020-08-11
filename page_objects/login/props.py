from selenium.webdriver.common.by import By

from page_objects.base.page.base_page import Locator


class LoginPageProps:

    class Messages:
        TITULO_PANEL = "Ingreso al sistema"

    class Locators:
        TITULO_PANEL = Locator(By.CSS_SELECTOR, "#ctl00_Contenido_Login1_LoginPanel > h2")
        TXT_USER = Locator(By.ID, "ctl00_Contenido_Login1_UserName")
        TXT_CONTRASEÑA = Locator(By.ID, "ctl00_Contenido_Login1_Password")
        BTN_INICIAR_SESION = Locator(By.ID, "ctl00_Contenido_Login1_Login")



