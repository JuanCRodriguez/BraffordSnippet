from db.conn.mssql.conn import MSSQLConnection
from page_objects.base.driver.handler import DriverHandler
from page_objects.base.page.factory import PageHandlerFactory


class Context:
    db: MSSQLConnection
    driver_handler: DriverHandler
    page_factory: PageHandlerFactory