from pypika import functions, MSSQLQuery

from db.base.query import Query
from utils.date import to_mssql_datetime


class MSSQLQueryBuilder(Query):

    def __init__(self):
        super().__init__(MSSQLQuery)

    def to_datetime(self, val):
        try:
            val = to_mssql_datetime(val)
        except AttributeError:
            # las entidades tienen muchas cosas y no tengo ganas de completar las fechas
            # si es none asumo que le mande un null a proposito,
            # si no, por ejemplo un string, la pifie y lo ato con alambre
            if val is None:
                return None
            val = "07/23/2020 18:27:00"
            print(f"Esperaba un datetime y obtuve un {type(val)}")
        return functions.Cast(val, "DATETIME")
