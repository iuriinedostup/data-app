import psycopg2


class DataLoad(object):

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='app_db',
            user='app_user',
            password=123456,
            host='db',
            port=5432
        )

        self.cursor = self.conn.cursor()

    def execute(self):

        query = '''
            CREATE TABLE DEPARTMENT(
               id INT PRIMARY KEY      NOT NULL,
               name          CHAR(50)  NOT NULL,
               email         INT       NOT NULL,
               inserted_at   TIMESTAMPTZ DEFAULT NOW(),
               updated_at    TIMESTAMPTZ DEFAULT NOW()
);
        '''

        self.cursor.execute(query)
        self.conn.commit()


if __name__ == '__main__':
    loader = DataLoad()
    loader.execute()
    print 'done'

