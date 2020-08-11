from typing import List

from db.base.handler import QueryHandler, Relation
from db.schema.dbo.cabaña.mapper import CabañaMapper
from db.schema.dbo.establecimiento.mapper import EstablecimientoMapper
from db.schema.dbo.producto.mapper import ProductoMapper, ProductoDataClass
from db.schema.dbo.producto.query import ProductoQueryBuilder
from db.schema.dbo.producto.table import ProductoEstablecimientoRelation, ProductoCabañaRelation


class ProductoHandler(QueryHandler):
    _o: ProductoDataClass
    _mapper = ProductoMapper()
    _qb = ProductoQueryBuilder()
    results: List[ProductoDataClass]

class ProductoEstablecimientoRelationBuilder(Relation):

    _table = ProductoEstablecimientoRelation()
    _left_mapper = ProductoMapper()
    _right_mapper = EstablecimientoMapper()

class ProductoCabañaRelationBuilder(Relation):

    _table = ProductoCabañaRelation()
    _left_mapper = CabañaMapper()
    _right_mapper = ProductoMapper()