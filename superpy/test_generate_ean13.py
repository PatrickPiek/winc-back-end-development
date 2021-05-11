import unittest
import math

from functions import generate_ean13


class test_generate_ean13(unittest.TestCase):

    def test1(self):
        assert generate_ean13(
            [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]) == '9780141026626'

    def test2(self):
        assert generate_ean13('978014102662') == '9780141026626'

    def test3(self):
        assert generate_ean13(978014102662) == '9780141026626'

    def test4(self):
        self.assertRaises(TypeError, generate_ean13, 'abc')

    def test5(self):
        self.assertRaises(TypeError, generate_ean13, {1})

    def test6(self):
        self.assertRaises(TypeError, generate_ean13, math.pi)
