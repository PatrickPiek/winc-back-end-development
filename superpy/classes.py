import random
import csv
from os.path import abspath
import sys
from functions import is_valid_date


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
        self.checksum = [self.__calculate_checksum()]
        self.ean = ''.join([str(digit)
                           for digit in (self.code + self.checksum)])

    def __str__(self):
        return self.ean

    def __calculate_checksum(self):
        odd = self.code[0] + self.code[2] + self.code[4] + \
            self.code[6] + self.code[8] + self.code[10]
        even = (self.code[1] + self.code[3] + self.code[5] +
                self.code[7] + self.code[9] + self.code[11]) * 3
        unit = (odd + even) % 10
        if unit != 0:
            return 10 - unit
        return 0


class Database():

    def __init__(self, filename='', columns=[]):

        if not isinstance(filename, str):
            raise TypeError('filename is a string')
        elif filename == '':
            raise ValueError('a valid filename is required')

        if not isinstance(columns, list):
            raise TypeError('columns is a list of names')
        elif len(columns) == 0:
            raise ValueError('a least one column is required')

        self.filename = filename
        self.filepath = self.__filepath()
        self.columns = columns
        self.columncount = len(columns)
        self.read()

    def __filepath(self):

        return abspath(f'./{self.filename}')

    def read(self):

        data = []

        with open(self.filepath, mode='r') as csv_file:

            file_ref = csv.DictReader(
                csv_file, delimiter=',', doublequote=True, escapechar='\\', lineterminator='\r\n',
                quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True, strict=True)

            for row in file_ref:
                rowdata = {}
                for column in self.columns:
                    rowdata[column] = row[column]
                data.append(rowdata)

        self.data = data
        self.rowcount = len(data)

    def write(self):

        with open(self.filepath, 'w') as csv_file:

            file_ref = csv.DictWriter(csv_file, fieldnames=self.columns)

            file_ref.writeheader()

            for row in self.data:
                file_ref.writerow(row)

    def add(self, data={}):

        if not isinstance(data, dict):
            raise TypeError('columns is a dictionary of properties')

        for column in data:
            if column not in self.columns:
                raise ValueError(f'{column} is not a valid property')

        for column in self.columns:
            if column not in data:
                raise ValueError(f'{column} is a required property')

        if data not in self.data:
            self.data.append(data)
            self.rowcount = self.rowcount + 1


def main():
    pass


if __name__ == '__main__':
    main()
