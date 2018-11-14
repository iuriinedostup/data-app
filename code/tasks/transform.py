from utils.db import DBFactory
from models.transform import DataTransform


class TransformTaskFactory(object):
    @staticmethod
    def create():
        db = DBFactory.create('postgres')
        model = DataTransform(db)
        return model
