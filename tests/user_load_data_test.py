import unittest
import pandas as pd
import logging

from models import User

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class UserLoadDataTest(unittest.TestCase):
    def setUp(self):
        self.userData = User.materialize_data('../data/')

    def test_run(self):
        assert(isinstance(self.userData, pd.DataFrame)), ('Error - not instance of DataFrame.')
        assert (len(self.userData.index) > 0), ('Error loading file.')

if __name__ == '__main__':
    unittest.main()

