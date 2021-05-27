import csv
from os.path import abspath, exists
import config
from datetime import datetime


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
        self.filepath = abspath(f'./{self.filename}')
        self.columns = columns
        self.columncount = len(columns)

        self.create()
        self.read()

    def read(self):

        data = []

        with open(self.filepath, mode='r') as csv_file:

            file_ref = csv.DictReader(
                csv_file, delimiter=',', doublequote=True, escapechar='\\', lineterminator='\r\n',
                quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True, strict=True)

            for row in file_ref:
                rowdata = {}
                for column in self.columns:
                    if column in config.DATE_FIELDS:
                        rowdata[column] = datetime.strptime(
                            row[column], config.DATE_FORMAT)
                    else:
                        rowdata[column] = row[column]
                data.append(rowdata)

        self.data = data
        self.rowcount = len(data)

    def save(self):

        with open(self.filepath, mode='w+') as csv_file:

            file_ref = csv.DictWriter(
                csv_file, fieldnames=self.columns, delimiter=',', doublequote=True, escapechar='\\',
                lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True,
                strict=True)

            file_ref.writeheader()

            for row in self.data:
                file_ref.writerow(row)

    def add(self, row={}):

        if not isinstance(row, dict):
            raise TypeError('row is a dictionary of properties')

        for column in row:
            if column not in self.columns:
                raise ValueError(f'{column} is not a valid property')

        for column in self.columns:
            if column not in row:
                raise ValueError(f'{column} is a required property')

        self.data.append(row)
        self.rowcount = len(self.data)

        with open(self.filepath, mode='a') as csv_file:

            file_ref = csv.DictWriter(
                csv_file, fieldnames=self.columns, delimiter=',', doublequote=True, escapechar='\\',
                lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True,
                strict=True)

            file_ref.writerow(row)

    def create(self):

        if not exists(self.filepath):
            self.data = []
            self.save()


def main():
    pass


if __name__ == '__main__':
    main()
