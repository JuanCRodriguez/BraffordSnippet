import allure
import pytest

from db.conn.mssql.conn import MSSQLConnection
from page_objects.base.driver.factory import LocalDriverFactory, RemoteDriverFactory
from page_objects.base.driver.handler import DriverHandler
from page_objects.base.page.factory import PageHandlerFactory
from utils.context import Context


@pytest.fixture
def context(request, target, worker_id):

    context = Context()

    front, db_conn_string = target
    context.db = MSSQLConnection(db_conn_string)
    if command_executor := request.config.getoption("--remote-server", None) is None:
        driver_factory = LocalDriverFactory("Chrome")
    else:
        driver_factory = RemoteDriverFactory(command_executor)

    context.driver_handler = DriverHandler(front, driver_factory)
    context.page_factory = PageHandlerFactory(context.driver_handler.build_main_driver())

    # init_data(context, worker_id, cant_cajeros)

    yield context

    try:
        if request.node.rep_call.failed:
            for driver in context.driver_handler:
                url = driver.current_url.replace(front, '')
                allure.attach(driver.get_screenshot_as_png(),
                              name=f'screenshot {context.driver_handler.drivers.index(driver)} - {url}',
                              attachment_type=allure.attachment_type.PNG)
    except AttributeError as e:
        print(f"No se pudo sacar una screenshot, posiblemente haya fallado en el setup, {e}")

    for driver in context.driver_handler:
        print("\n")
        for entry in driver.get_log('browser'):
            print(entry)
        print("\n")
    context.driver_handler.quit()



@pytest.fixture
def target(request):
    driver = "ODBC Driver 17 for SQL Server"
    username = 'sa'
    password = 'Factory.2020'
    if request.config.getoption("localhost", default=False):
        front = "http://localhost:51939/Web/Login.aspx"
        db = f'DRIVER={driver};SERVER=(localdb)\MSSQLLocalDB;DATABASE=ABA_TEST;Trusted_Connection=yes'
    else:
        target = request.config.getoption("ambiente")
        front = f"https://{target}/login"
        db = f'DRIVER={driver};SERVER=(localdb)\MSSQLLocalDB;DATABASE=ABA_TEST;;UID={username};PWD={password}'

    return front, db


def pytest_addoption(parser):
    help_ambiente = "Ambiente sobre el cual se van a ejecutar las pruebas"
    help_headless = "Si esta presente, el driver se va a instanciar en modo headless"
    help_remote = "Si esta presente, se utilizara el driver remoto, en caso contrario se utilizara Chromedriver"
    parser.addoption('--localhost', action='store_true', dest='localhost')
    parser.addoption('--headless', action='store_true', dest='headless', help=help_headless)
    parser.addoption('--remote-server', default=None, action='store', dest='remote', help=help_remote)


pytest_plugins = [
    "fixtures.producto",
    "fixtures.servicio",
    "fixtures.establecimiento",
    "fixtures.usuario"
]