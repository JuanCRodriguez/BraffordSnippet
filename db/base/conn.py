from abc import ABC


class Connection(ABC):

    def execute(self, q):
        raise NotImplementedError()

    def commit(self):
        raise NotImplementedError()

    def fetch_one(self):
        raise NotImplementedError()

    def fetch_many(self, size):
        raise NotImplementedError()

    def fetch_all(self):
        raise NotImplementedError()

    def exit(self):
        raise NotImplementedError()

    def last_insert_id(self):
        raise NotImplementedError()