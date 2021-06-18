from barcode import EAN13 as ean13
from barcode.writer import ImageWriter

from os import makedirs
from os.path import abspath, exists

import random

import config

from functions.export import make_missing_dir


class Barcode():
    """Generates a valid EAN13 barcode with checksum
    Stores a barcode image in PNG-format to a barcodes directory
    for use in supermarket product display and Cash register
    """

    def __init__(self, prefix):

        # check prefix type
        if not isinstance(prefix, (str, int, list)):
            raise TypeError('Only string, list or int allowed')

        # convert int or str of digits into list of digits
        if isinstance(prefix, (str, int)):
            prefix = list(str(prefix))

        # start new ean code with up to 12 digits from prefix
        code = []

        if isinstance(prefix, list) and len(prefix) > 0:

            for digit in prefix:

                # if code = 12 digits, break
                if len(code) >= 12:
                    break

                # if digit is int, append
                if isinstance(digit, int):
                    code.append(digit)

                # if digit is str and is a digit, append as int
                elif isinstance(digit, str):
                    if digit.isdigit():
                        digit = code.append(int(digit))
                    else:
                        # raise TypeError if digit is some other character
                        raise TypeError('Only digits allowed')

        # add up to 12 random digits to complete code
        while len(code) < 12:
            code.append(random.randint(0, 9))

        self.prefix = prefix
        self.code = code
        self.checksum = [self.__calculate_checksum()]
        self.ean = ''.join([str(digit)
                           for digit in (self.code + self.checksum)])

        # generate barcode image
        self.__generate_barcode_image(self.ean)

    def __str__(self):
        return self.ean

    def __generate_barcode_image(self, ean=''):

        if ean == '':
            raise ValueError('A string of 13 digits is required')

        directory = config.BARCODES_DIR
        make_missing_dir(directory)
        filepath = abspath(f'./{directory}/{ean}.png')

        try:
            with open(filepath, 'wb') as f:
                ean13(ean, writer=ImageWriter()).write(f)

        except:
            raise Exception(
                f'Unable to save barcode to file ‘{filepath}’')

    def __calculate_checksum(self):
        odd = sum(self.code[0::2])
        even = sum(self.code[1::2]) * 3
        unit = (odd + even) % 10
        if unit != 0:
            return 10 - unit
        return 0


def main():
    pass


if __name__ == '__main__':
    main()
