from typing import List

from db.base.handler import QueryHandler, Relation
from db.schema.dbo.sec_profile.mapper import SecProfileDataClass, SecProfileMapper
from db.schema.dbo.sec_profile.query import SecProfileQueryBuilder
from db.schema.dbo.sec_user.mapper import SecUserMapper
from db.schema.dbo.sec_user.table import SecProfileUserRelation
from dominio.perfil import Perfil
from dominio.usuario import Usuario


class SecProfileHandler(QueryHandler):
    _o: SecProfileDataClass
    _qb = SecProfileQueryBuilder()
    _mapper = SecProfileMapper()
    results: List[SecProfileDataClass]

    def create(self, o: Perfil):
        raise Exception("Protected table")

    def with_id_profile(self):
        self._wheres += 1
        self._qb.with_id_profile(self._o.id_profile)

    def with_descripcion(self):
        self._wheres += 1
        self._qb.with_name(self._o.name)

class SecProfileUserRelationBuilder(Relation):

    _table = SecProfileUserRelation()
    _left_mapper = SecUserMapper()
    _right_mapper = SecProfileMapper()

    def left(self, l: Usuario):
        return self._left_mapper.in_(l).id_user

    def right(self, r: Perfil):
        return self._right_mapper.in_(r).id_profile
