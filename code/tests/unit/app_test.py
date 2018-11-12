import unittest2
import mock

from data_load import DataLoad


class AppTest(unittest2.TestCase):

    def create_object_test(self):
        db = mock.Mock()
        loader = DataLoad(db)
        loader.execute()

        db.execute.assert_called_once_with('SELECT * FROM users')


