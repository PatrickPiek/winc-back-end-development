import unittest
import math

from EAN13_Barcode import EAN13_Barcode


class Test(unittest.TestCase):

    def test1(self):
        code = EAN13_Barcode([9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2])
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test2(self):
        code = EAN13_Barcode('978014102662')
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test3(self):
        code = EAN13_Barcode(978014102662)
        assert code.code == [9, 7, 8, 0, 1, 4, 1, 0, 2, 6, 6, 2]
        assert code.checksum == [6]
        assert code.ean == '9780141026626'

    def test4(self):
        self.assertRaises(TypeError, EAN13_Barcode, 'abc')

    def test5(self):
        self.assertRaises(TypeError, EAN13_Barcode, {1})

    def test6(self):
        self.assertRaises(TypeError, EAN13_Barcode, math.pi)
