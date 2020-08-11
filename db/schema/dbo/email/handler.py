from typing import List

from db.base.handler import QueryHandler
from db.schema.dbo.email.mapper import EmailMapper, EmailDataClass
from db.schema.dbo.email.query import EmailQueryBuilder


class EmailHandler(QueryHandler):

    _o: EmailDataClass
    _qb = EmailQueryBuilder()
    _mapper = EmailMapper()
    results: List[EmailDataClass]
