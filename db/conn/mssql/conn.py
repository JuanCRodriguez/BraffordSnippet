from random import randint

import pyodbc as pyodbc
from pyodbc import Connection as Connection_

from db.base.conn import Connection


class MSSQLConnection(Connection):

    def __init__(self, conn_string):
        super().__init__()
        self.conn: Connection_ = pyodbc.connect(conn_string)
        self.cursor: pyodbc.Cursor = self.conn.cursor()

    def execute(self, q):
        self.cursor.execute(q)

    def commit(self):
        self.cursor.commit()

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_many(self, size):
        return self.cursor.fetchmany(size)

    def fetch_all(self):
        return self.cursor.fetchall()

    def exit(self):
        self.cursor.close()
        self.conn.close()

    def last_insert_id(self):
        self.cursor.execute("SELECT @@IDENTITY")
        id_ = self.cursor.fetchval()
        return id_


class MockConnection(Connection):

    def last_insert_id(self):
        return randint(1, 5000)

    def execute(self, q):
        print(q)

    def fetch_all(self):
        return []

    def fetch_one(self):
        return "ola"