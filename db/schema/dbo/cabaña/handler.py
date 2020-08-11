from typing import List

from db.base.handler import QueryHandler, Relation
from db.schema.dbo.cabaña.mapper import CabañaDataClass, CabañaMapper
from db.schema.dbo.cabaña.query import CabañaQueryBuilder
from db.schema.dbo.cabaña.table import CabañaDireccionRelation, CabañaTelefonoRelation, CabañaEmailRelation
from db.schema.dbo.direccion.mapper import DireccionMapper
from db.schema.dbo.email.mapper import EmailMapper
from db.schema.dbo.telefono.mapper import TelefonoMapper


class CabañaHandler(QueryHandler):

    _o: CabañaDataClass
    _mapper = CabañaMapper()
    _qb = CabañaQueryBuilder()
    results: List[CabañaDataClass]


class CabañaDireccionRelationBuilder(Relation):

    _table = CabañaDireccionRelation()
    _left_mapper = DireccionMapper()
    _right_mapper = CabañaMapper()



class CabañaTelefonoRelationBuilder(Relation):
    _table = CabañaTelefonoRelation()
    _left_mapper = TelefonoMapper()
    _right_mapper = CabañaMapper()


class CabañaEmailRelationBuilder(Relation):

    _table = CabañaEmailRelation()
    _left_mapper = EmailMapper()
    _right_mapper = CabañaMapper()
