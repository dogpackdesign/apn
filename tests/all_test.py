import unittest

from validate_test import TestStateValidation


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestStateValidation))
    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)
