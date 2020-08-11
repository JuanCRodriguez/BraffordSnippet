from typing import List

from db.base.handler import QueryHandler, Relation
from db.schema.dbo.direccion.mapper import DireccionMapper
from db.schema.dbo.email.mapper import EmailMapper
from db.schema.dbo.persona_juridica.mapper import PersonaJuridicaDataClass, PersonaJuridicaMapper
from db.schema.dbo.persona_juridica.query import PersonaJuridicaQueryBuilder
from db.schema.dbo.persona_juridica.table import PersonaJuridicaDireccionRelation, \
    PersonaJuridicaTelefonoRelation, PersonaJuridicaEmailRelation
from db.schema.dbo.telefono.mapper import TelefonoMapper


class PersonaJuridicaHandler(QueryHandler):
    _o: PersonaJuridicaDataClass
    _mapper = PersonaJuridicaMapper()
    _qb = PersonaJuridicaQueryBuilder()
    results: List[PersonaJuridicaDataClass]

class PersonaJuridicaDireccionRelationBuilder(Relation):

    _table = PersonaJuridicaDireccionRelation()
    _left_mapper = DireccionMapper()
    _right_mapper = PersonaJuridicaMapper()

class PersonaJuridicaTelefonoRelationBuilder(Relation):

    _table = PersonaJuridicaTelefonoRelation()
    _left_mapper = TelefonoMapper()
    _right_mapper = PersonaJuridicaMapper()

class PersonaJuridicaEmailRelationBuilder(Relation):

    _table = PersonaJuridicaEmailRelation()
    _left_mapper = EmailMapper()
    _right_mapper = PersonaJuridicaMapper()

