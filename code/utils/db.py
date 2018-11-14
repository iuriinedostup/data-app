import psycopg2
import sqlite3
import os


class CommonDB(object):

    def __init__(self):

        self.conn = None
        self.cursor = None

    def execute(self, query):

        self.cursor.execute(query)

    def commit(self):

        self.conn.commit()

    def copy_from(self, fh, table, sep):

        raise NotImplementedError

    def init(self):

        raise NotImplementedError

    def close(self):

        self.conn.close()


class PostgresDB(CommonDB):

    def __init__(self, dbname, user, password, host, port):

        super(PostgresDB, self).__init__()

        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        self.cursor = self.conn.cursor()

    def init(self):

        pwd = os.path.dirname(__file__)
        file_name = 'ddl.sql'
        file_path = os.path.join(
            pwd,
            '..',
            'sql',
            file_name
        )

        with open(file_path, 'r') as fh:
            reader = fh.read()
            self.execute(reader)

        self.commit()

    def copy_from(self, fh, table, sep):

        self.cursor.copy_from(fh, table, sep)


class SQLiteDB(CommonDB):

    def __init__(self, db_path):

        super(SQLiteDB, self).__init__()

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def init(self):

        raise NotImplementedError

    def copy_from(self, fh, table, sep):

        raise NotImplementedError


class DBFactory(object):

    @staticmethod
    def create(db_type, init=False):

        if db_type == 'postgres':

            db = PostgresDB(
            'app_db',
            'app_user',
            123456,
            'db',
            5432
            )

        elif db_type == 'sqlite':

            db = SQLiteDB('/data/app.db')

        else:

            raise ValueError('incorrect DB type')

        if init:

            db.init()

        return db

