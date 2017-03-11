import unittest

from apn import validate


class TestStateValidation(unittest.TestCase):
    def test_state_abbrev(self):
        self.assertEqual(len(validate.validate('123456-1234', state='WA')), 1)

    def test_state_abbrev_lower(self):
        self.assertEqual(len(validate.validate('123456-1234', state='wa')), 1)

    def test_state_abbrev_camel(self):
        self.assertEqual(len(validate.validate('123456-1234', state='wA')), 1)

    def test_state(self):
        self.assertEqual(len(validate.validate('123456-1234', state='Washington')), 1)

    def test_state_lower(self):
        self.assertEqual(len(validate.validate('123456-1234', state='washington')), 1)

    def test_state_camel(self):
        self.assertEqual(len(validate.validate('123456-1234', state='wAsHinGTon')), 1)

    def test_state_misspell(self):
        validate_validate = validate.validate('123456-1234', state='washingto')
        self.assertEqual(len(validate_validate), 1)
        self.assertEqual(validate_validate[0].state, 'Washington')

    def test_state_misspell_2(self):
        validate_validate = validate.validate('123456-1234', state='warhsington')
        self.assertEqual(len(validate_validate), 1)
        self.assertEqual(validate_validate[0].state, 'Washington')

    def test_nation(self):
        self.assertIsNotNone(validate.validate('123456-1234'))
