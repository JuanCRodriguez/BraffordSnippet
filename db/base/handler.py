from abc import ABC
from contextlib import contextmanager

from pypika import Table

from db.base.conn import Connection
from db.base.mapper import Mapper
from db.base.query_builder import QueryBuilder, RelationQueryBuilder


class QueryHandler(ABC):
    _mapper: Mapper
    _qb: QueryBuilder

    def __init__(self, db):
        self.conn: Connection = db
        self._wheres = 0
        self.results = []

    def create(self, o):
        self._reset()
        return self._insert(
            self._qb.insert(
                self._mapper.in_(o)
            )
        )

    def _insert(self, query):
        print(repr(query))
        self.conn.execute(repr(query))
        return int(self.conn.last_insert_id())

    @contextmanager
    def fetch(self, o):
        self._o = self._mapper.in_(o)
        self._reset()
        self._qb.select()

        yield self

        if self._wheres == 0:
            raise ValueError("Empty where")

        self.conn.execute(repr(self._qb))
        self.results = [self._mapper.out(r) for r in self.conn.fetch_all()]

    def _reset(self):
        self._qb.reset()
        self._wheres = 0
        self.results = []

    def save(self, *args):
        raise NotImplementedError()


class Relation:
    _table: Table
    _left_mapper: Mapper
    _right_mapper: Mapper

    def __init__(self, db):
        self.conn: Connection = db
        self._qb = RelationQueryBuilder(self._table)

    def left(self, l):
        return self._left_mapper.in_(l).id

    def right(self, r):
        return self._right_mapper.in_(r).id

    def create(self, l, r):
        l = self.left(l)
        r = self.right(r)

        if not l or not r:
            raise ValueError()

        self.conn.execute(
            repr(
                self._qb.insert(l, r)
            )
        )

