import argparse

from db import DBFactory
from loader import DataLoad

parser = argparse.ArgumentParser()

parser.add_argument(
    '-d',
    '--dbtype',
    type = str,
    dest='db_type',
    required=True
)

parser.add_argument(
    '-i',
    '--init',
    action='store_true',
    dest='init'
)


if __name__ == '__main__':

    args = parser.parse_args()
    db_type = args.db_type
    init = args.init

    db = DBFactory.create(db_type, init)

    loader = DataLoad(db)
    loader.execute()

    print 'done'

