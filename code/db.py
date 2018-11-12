class CommonDB(object):

    def __init__(self, *args, **kwargs):
        self.conn = None
        self.cursor = None

    def execute(self, query):
        self.cursor.execute(query)

    def commit(self):
        self.conn.commit()

    def init(self):
        raise NotImplementedError


class PostgresDB(CommonDB):
    def __init__(self, db_name, user, password, host, port):

        super(PostgresDB, self).__init__()

        self.conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )

        self.cursor = self.conn.cursor()

    def init(self):
        query = '''
                    CREATE TABLE IF NOT EXISTS users (
                       id INT PRIMARY KEY  NOT NULL,
                       name          VARCHAR(50)  NOT NULL,
                       email         INT       NOT NULL,
                       inserted_at   TIMESTAMP DEFAULT NOW(),
                       updated_at    TIMESTAMP DEFAULT NOW()
        );
                '''

        self.execute(query)
        self.commit()


class SQLiteDB(CommonDB):
    def __init__(self, db_path):
        super(SQLiteDB, self).__init__()

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)

    def commit(self):
        self.conn.commit()

    def init(self):
        query = '''
                    CREATE TABLE IF NOT EXISTS users (
                       id INT PRIMARY KEY  NOT NULL,
                       name          VARCHAR(50)  NOT NULL,
                       email         INT       NOT NULL,
                       inserted_at   TIMESTAMP DEFAULT,
                       updated_at    TIMESTAMP DEFAULT
        );
                '''

        self.execute(query)
        self.commit()


class DBFactory(object):

    def __init__(self, config):
        self.config = config

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
            raise ValueError('Incorrect DB Type')

        if init == 'True':
            db.init()

        return db
