from utils.db import DBFactory
from models.load import DataLoad


class LoadTaskFactory(object):

    @staticmethod
    def create():
        db = DBFactory.create('postgres')
        model = DataLoad(db)
        return model
