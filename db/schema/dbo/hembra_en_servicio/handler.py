from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.hembra_en_servicio.mapper import HembraEnServicioMapper, HembraEnServicioDataClass
from db.schema.dbo.hembra_en_servicio.query import HembraEnServicioQueryBuilder


class HembraEnServicioHandler(QueryHandler):
    _o: HembraEnServicioDataClass
    _mapper = HembraEnServicioMapper()
    _qb = HembraEnServicioQueryBuilder()
    results: List[HembraEnServicioDataClass]
