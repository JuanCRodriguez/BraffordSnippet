from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.machosenservicio.mapper import MachosEnServicioMapper, MachosEnServicioDataClass
from db.schema.dbo.machosenservicio.query import MachosEnServicioQueryBuilder


class MachosEnServicioHandler(QueryHandler):
    _o: MachosEnServicioDataClass
    _mapper = MachosEnServicioMapper()
    _qb = MachosEnServicioQueryBuilder()
    results: List[MachosEnServicioDataClass]
