from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.medicion.mapper import MedicionMapper, MedicionDataClass
from db.schema.dbo.medicion.query import MedicionQueryBuilder


class MedicionHandler(QueryHandler):
    _o: MedicionDataClass
    _mapper = MedicionMapper()
    _qb = MedicionQueryBuilder()
    results: List[MedicionDataClass]