import random
import csv
from os.path import abspath, exists, isdir, isfile


class Ean13Code():

    def __init__(self, prefix=[]):

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

    def __str__(self):
        ean13 = self.code
        ean13.append(self.calculate_checksum(self.code))
        return ''.join([str(digit) for digit in ean13])

    def calculate_checksum(self, code):
        odd = self.code[0] + self.code[2] + self.code[4] + \
            self.code[6] + self.code[8] + self.code[10]
        even = (self.code[1] + self.code[3] + self.code[5] +
                self.code[7] + self.code[9] + self.code[11]) * 3
        unit = (odd + even) % 10
        if unit != 0:
            return 10 - unit
        return 0


class FileSystemDB():

    def __init__(self, filename='', columns=[]):
        data = []

        if not isinstance(filename, str):
            raise TypeError('A filename is a string')
        elif filename == '':
            raise ValueError('A valid filename is required')

        if not isinstance(columns, list):
            raise TypeError('A list of column names is required')
        elif len(columns) == 0:
            raise ValueError('At least one column is required')

        filepath = abspath(f'./{filename}')

        if not exists(filepath):
            raise FileExistsError(filepath)

        elif not isfile(filepath):
            raise FileNotFoundError(filepath)

        else:
            with open(filepath, mode='r') as csv_file:
                file_ref = csv.DictReader(
                    csv_file, delimiter=',', doublequote=True, escapechar='\\', lineterminator='\r\n',
                    quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True, strict=True)
                for row in file_ref:
                    rowdata = {}
                    for column in columns:
                        rowdata[column] = row[column]
                    data.append(rowdata)

            self.data = data
            self.rowcount = len(data)
            self.filename = filename
            self.columns = columns
            self.columncount = len(columns)
            self.filepath = filepath


def main():

    code = Ean13Code('123')
    print(code)

    products = FileSystemDB('products.csv', ['name', 'department', 'birthday'])
    print(products.data, products.rowcount, products.filename,
          products.columns, products.columncount, products.filepath)


if __name__ == '__main__':
    main()
