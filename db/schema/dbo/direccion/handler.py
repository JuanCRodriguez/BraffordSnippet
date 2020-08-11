from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.direccion.mapper import DireccionMapper, DireccionDataClass
from db.schema.dbo.direccion.query import DireccionQueryBuilder


class DireccionHandler(QueryHandler):

    _o: DireccionDataClass
    _qb = DireccionQueryBuilder()
    _mapper = DireccionMapper()
    results: List[DireccionDataClass]