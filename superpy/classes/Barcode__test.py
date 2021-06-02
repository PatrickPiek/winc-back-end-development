import unittest
import math

from classes.Barcode import Barcode


class Test(unittest.TestCase):

    def test1(self):
        code = Barcode([9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2])
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test2(self):
        code = Barcode('978014102662')
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test3(self):
        code = Barcode(978014102662)
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test4(self):
        self.assertRaises(TypeError, Barcode, 'abc')

    def test5(self):
        self.assertRaises(TypeError, Barcode, {1})

    def test6(self):
        self.assertRaises(TypeError, Barcode, math.pi)
