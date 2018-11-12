from db import DBFactory


class DataLoad(object):

    def __init__(self, db_conn):
        self.db_conn = db_conn

    def execute(self):
        self.db_conn.execute(
            'SELECT * FROM users'
        )

if __name__ == '__main__':

    db = DBFactory.create('sqlite')

    loader = DataLoad(db)
    loader.execute()

    print 'done'

