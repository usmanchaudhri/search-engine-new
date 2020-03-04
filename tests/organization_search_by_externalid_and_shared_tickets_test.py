import unittest
import logging

from models import Organization

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class OrganizationalSearchTests(unittest.TestCase):
    def setUp(self):
        self.organizationData = Organization.materialize_data('../data/')

    def test_run(self):
        input = [('external_id', '9270ed79-35eb-4a38-a46f-35725197ea8d'), ('shared_tickets', 'false')]

        query = '&'.join([f'{key}=="{value}"' for key, value in input if value != ''])
        result = self.organizationData.query(query)

        assert(result is not None)

if __name__ == '__main__':
    unittest.main()

