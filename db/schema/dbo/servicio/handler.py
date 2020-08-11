from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.servicio.mapper import ServicioDataClass, ServicioMapper
from db.schema.dbo.servicio.query import ServicioQueryBuilder


class ServicioHandler(QueryHandler):

    _o: ServicioDataClass
    _mapper = ServicioMapper()
    _qb = ServicioQueryBuilder()
    results: List[ServicioDataClass]