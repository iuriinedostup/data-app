import psycopg2
import sqlite3


class CommonDB(object):

    def __init__(self):

        self.conn = None
        self.cursor = None

    def execute(self, query):

        self.cursor.execute(query)

    def commit(self):

        self.conn.commit()

    def init(self):

        raise NotImplementedError


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

        query = '''
            CREATE TABLE IF NOT EXISTS users (
               id INT PRIMARY KEY      NOT NULL,
               name          CHAR(50)  NOT NULL,
               email         INT       NOT NULL,
               inserted_at   TIMESTAMPTZ DEFAULT NOW(),
               updated_at    TIMESTAMPTZ DEFAULT NOW()
            );
        '''

        self.execute(query)
        self.commit()


class SQLiteDB(CommonDB):

    def __init__(self, db_path):

        super(SQLiteDB, self).__init__()

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def init(self):

        query = '''
                    CREATE TABLE IF NOT EXISTS users (
                       id INT PRIMARY KEY      NOT NULL,
                       name          CHAR(50)  NOT NULL,
                       email         INT       NOT NULL,
                       inserted_at   TIMESTAMPTZ DEFAULT,
                       updated_at    TIMESTAMPTZ DEFAULT
                    );
                '''

        self.execute(query)
        self.commit()


class DBFactory(object):

    @staticmethod
    def create(db_type, init):

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

