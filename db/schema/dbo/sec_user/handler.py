from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.sec_user.mapper import SecUserMapper, SecUserDataClass
from db.schema.dbo.sec_user.query import SecUserQueryBuilder


class SecUserHandler(QueryHandler):
    _o: SecUserDataClass
    _mapper = SecUserMapper()
    _qb = SecUserQueryBuilder()
    results: List[SecUserDataClass]
