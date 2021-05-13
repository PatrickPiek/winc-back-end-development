import unittest
from datetime import datetime
from is_valid_date import is_valid_date


class Test(unittest.TestCase):

    def test(self):
        assert is_valid_date('2021') == datetime(2021, 1, 1, 0, 0)
        assert is_valid_date('2021-05') == datetime(2021, 5, 1, 0, 0)
        assert is_valid_date('2021-05-25') == datetime(2021, 5, 25, 0, 0)

        self.assertRaises(ValueError, is_valid_date, '2021-05-32')
        self.assertRaises(ValueError, is_valid_date, '2021-13-01')
        self.assertRaises(ValueError, is_valid_date, '')
