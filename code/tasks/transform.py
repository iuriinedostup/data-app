from utils.db import DBFactory
from models.transform import DataTransform


class TransformTaskFactory(object):

    @staticmethod
    def create(parser):

        parser.add_argument(
            '--file-name',
            dest='file_name',
        )

        db = DBFactory.create('postgres')
        model = DataTransform(db)
        parser.set_defaults(func=model.execute)
