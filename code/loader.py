class DataLoad(object):

    def __init__(self, db_conn):

        self.db_conn = db_conn

    def execute(self):

        self.db_conn.execute(
            'SELECT * FROM users'
        )
