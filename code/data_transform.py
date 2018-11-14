import argparse

from utils.db import DBFactory
from utils.transformer import DataTransform

parser = argparse.ArgumentParser()

parser.add_argument(
    '-d',
    '--dbtype',
    type=str,
    dest='db_type',
    required=True
)


if __name__ == '__main__':

    args = parser.parse_args()
    db_type = args.db_type

    db = DBFactory.create(db_type)

    transformer = DataTransform(db)
    transformer.execute()

    db.close()

    print 'done'
