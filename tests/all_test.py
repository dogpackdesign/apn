import unittest

import validate_test


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(validate_test.TestStateValidation)
    return test_suite


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
