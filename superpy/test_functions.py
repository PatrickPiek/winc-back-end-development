import unittest

from functions import generate_ean13


class test_generate_ean13(unittest.TestCase):

    def test1_generate_ean13(self):
        assert generate_ean13(
            [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]) == '9780141026626'

    def test2_generate_ean13(self):
        assert generate_ean13('978014102662') == '9780141026626'

    def test3_generate_ean13(self):
        assert generate_ean13(978014102662) == '9780141026626'

    def test4_generate_ean13(self):
        self.assertRaises(TypeError, generate_ean13, 'abc')
