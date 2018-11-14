import argparse

from utils.db import DBFactory
from models.load import DataLoad


class LoadTaskFactory(object):

    @staticmethod
    def create(parser):
        parser.add_argument(
            '--start-date',
            dest='start_date',
        )

        parser.add_argument(
            '--end-date',
            dest='end_date',
        )

        db = DBFactory.create('postgres')
        model = DataLoad(db)

        parser.set_defaults(func=model.execute)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Loader')

    LoadTaskFactory.create(parser)
    args = parser.parse_args()
    args.func(args)
