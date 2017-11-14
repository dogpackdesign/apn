import unittest

import apn


class TestLookup(unittest.TestCase):
    def test_lookup_by_state_and_county(self):
        self.assertEqual(len(apn.lookup('WA', 'King')), 3)

    def test_lookup_by_state_and_county_wrong(self):
        self.assertGreater(len(apn.lookup('WA', 'Snohomish')), 0)
