from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.telefono.mapper import TelefonoMapper, TelefonoDataClass
from db.schema.dbo.telefono.query import TelefonoQueryBuilder


class TelefonoHandler(QueryHandler):

    _o: TelefonoDataClass
    _mapper = TelefonoMapper()
    _qb = TelefonoQueryBuilder()
    results: List[TelefonoDataClass]