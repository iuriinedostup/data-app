from db import DBFactory


class DataTransform(object):

    def __init__(self, db_conn):
        self.db_conn = db_conn

    def execute(self):
        users = self.db_conn.select('SELECT id, email, first_name, last_name FROM users')

        users_list = []

        for u in users:
            users_list.append(
                (u[0], u[1], "{} {}".format(u[2], u[3]))
            )

        return users_list


if __name__ == '__main__':

    db = DBFactory.create('postgres')

    loader = DataTransform(db)
    loader.execute()

    print 'done'

