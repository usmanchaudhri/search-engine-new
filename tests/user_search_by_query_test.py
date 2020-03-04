import unittest
import pandas as pd
import logging

from models import User

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class UserSearchTest(unittest.TestCase):
    def setUp(self):
        self.userData = User.materialize_data('../data/')

    def test_run(self):
        input = [('_id', '1'), ('external_id', '74341f74-9c79-49d5-9611-87ef9b6eb75f'), ('name', 'Francisca Rasmussen')]
        query = '&'.join([f'{key}=="{value}"' for key, value in input if value != ''])

        result = self.userData.query(query)
        assert(result is not None), ('result is empty')

if __name__ == '__main__':
    unittest.main()

