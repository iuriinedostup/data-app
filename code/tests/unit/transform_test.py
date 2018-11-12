import unittest2
import mock

from data_transform import DataTransform


class AppTest(unittest2.TestCase):

    def execute_test(self):

        users = [
            (1, 'em1@em.com', 'John', 'Doe'),
            (2, 'em2@em.com', 'Josh', 'Doe'),
        ]

        db = mock.Mock()
        db.select.return_value = users
        transform = DataTransform(db)
        users_result = transform.execute()

        expected = [
            (1, 'em1@em.com', 'John Doe'),
            (2, 'em2@em.com', 'Josh Doe'),
        ]

        self.assertEqual(
            expected,
            users_result
        )
