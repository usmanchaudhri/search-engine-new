from tests.organization_search_by_externalid_and_shared_tickets_test import OrganizationalSearchTests
from tests.user_load_data_test import UserLoadDataTest
from tests.case_sensitivity_for_user_data_test import CaseSensitivityForUserDataTest

import unittest

"""
test suite runner
"""
def suite():
    suite = unittest.TestSuite()
    suite.addTest(OrganizationalSearchTests('test_run'))
    suite.addTest(UserLoadDataTest('test_run'))
    suite.addTest(CaseSensitivityForUserDataTest('test_run'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
