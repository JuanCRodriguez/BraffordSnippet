from typing import List

from db.base.handler import QueryHandler, Relation
from db.schema.dbo.direccion.mapper import DireccionMapper
from db.schema.dbo.email.mapper import EmailMapper
from db.schema.dbo.establecimiento.mapper import EstablecimientoMapper, EstablecimientoDataClass
from db.schema.dbo.establecimiento.query import EstablecimientoQueryBuilder
from db.schema.dbo.establecimiento.table import EstablecimientoDireccionRelation, \
    EstablecimientoTelefonoRelation, EstablecimientoEmailRelation
from db.schema.dbo.telefono.mapper import TelefonoMapper


class EstablecimientoHandler(QueryHandler):
    _o: EstablecimientoDataClass
    _mapper = EstablecimientoMapper()
    _qb = EstablecimientoQueryBuilder()
    results: List[EstablecimientoDataClass]


class EstablecimientoDireccionRelationBuilder(Relation):

    _table = EstablecimientoDireccionRelation()
    _left_mapper = DireccionMapper()
    _right_mapper = EstablecimientoMapper()


class EstablecimientoTelefonoRelationBuilder(Relation):

    _table = EstablecimientoTelefonoRelation()
    _left_mapper = TelefonoMapper()
    _right_mapper = EstablecimientoMapper()


class EstablecimientoEmailRelationBuilder(Relation):

    _table = EstablecimientoEmailRelation()
    _left_mapper = EmailMapper()
    _right_mapper = EstablecimientoMapper()
