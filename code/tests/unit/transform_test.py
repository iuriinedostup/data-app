import unittest2
import mock

from code.utils.transformer import DataTransform


class AppTest(unittest2.TestCase):

    def execute_test(self):

        users = [
            (1, 'em1@domain1.extension1', 'John Doe', '123456', '134567'),
            (2, 'em2@domain1.extension2', 'Josh Doe', '123456', '134567'),
            (3, 'em3@domain2.extension1', 'John Deo', '123456', '134567'),
            (4, 'em4@domain2.extension2', 'Josh Ode', '123456', '134567')
        ]

        db = mock.Mock()
        db.select.return_value = users
        transform = DataTransform(db)
        transform.execute()
        users_result = transform.output

        expected = [
            ('extension1', '2'),
            ('extension2', '2'),
        ]

        self.assertEqual(
            expected,
            users_result
        )
