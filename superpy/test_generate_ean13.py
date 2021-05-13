import unittest
import math

from class__Ean13Code import Ean13Code


class test_generate_ean13(unittest.TestCase):

    def test1(self):
        code = Ean13Code([9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2])
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test2(self):
        code = Ean13Code('978014102662')
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test3(self):
        code = Ean13Code(978014102662)
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test4(self):
        self.assertRaises(TypeError, Ean13Code, 'abc')

    def test5(self):
        self.assertRaises(TypeError, Ean13Code, {1})

    def test6(self):
        self.assertRaises(TypeError, Ean13Code, math.pi)
