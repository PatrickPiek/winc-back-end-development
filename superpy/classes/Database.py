from os import makedirs
from os.path import abspath, exists

import csv

import config

from datetime import datetime
from functions.export import make_missing_dir


class Database():

    def __init__(self, filename='', columns=[]):

        if filename == '':
            raise ValueError('The ‘filename’ argument is required')
        elif len(columns) == 0:
            raise ValueError(
                'The ‘columns’ argument requires at least one column')

        self.filename = filename

        make_missing_dir(config.DATABASES_DIR)

        self.filepath = abspath(f'./{config.DATABASES_DIR}/{self.filename}')
        self.columns = columns
        self.columncount = len(columns)

        self.create()
        self.read()

    def read(self):

        data = []

        try:
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

        except OSError:
            raise OSError(
                f'Unable to read database file from ‘{self.filepath}’')
        except:
            raise Exception(
                f'Unable to process database file ‘{self.filepath}’')

        self.data = data
        self.rowcount = len(data)

    def save(self):

        try:
            with open(self.filepath, mode='w+') as csv_file:

                file_ref = csv.DictWriter(
                    csv_file, fieldnames=self.columns, delimiter=',', doublequote=True, escapechar='\\',
                    lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True,
                    strict=True)

                file_ref.writeheader()

                for row in self.data:
                    file_ref.writerow(row)

        except OSError:
            raise OSError(
                f'Unable to save database file to ‘{self.filepath}’')
        except:
            raise Exception(
                f'Unable to process database file ‘{self.filepath}’')

    def add(self, row={}):

        if not isinstance(row, dict):
            raise TypeError('The ‘row’ argument is a dictionary of properties')

        for column in row:
            if column not in self.columns:
                raise ValueError(
                    f'Column ‘{column}’ is not a valid property for this database')

        for column in self.columns:
            if column not in row:
                raise ValueError(
                    f'Column ‘{column}’ is a required property for this database')

        self.data.append(row)
        self.rowcount = len(self.data)

        try:
            with open(self.filepath, mode='a') as csv_file:

                file_ref = csv.DictWriter(
                    csv_file, fieldnames=self.columns, delimiter=',', doublequote=True, escapechar='\\',
                    lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True,
                    strict=True)

                file_ref.writerow(row)

        except OSError:
            raise OSError(
                f'Unable to add data to database file ‘{self.filepath}’')
        except:
            raise Exception(
                f'Unable to process database file ‘{self.filepath}’')

    def create(self):

        try:
            if not exists(self.filepath):

                self.data = []
                self.save()

        except OSError:
            raise OSError(
                f'Unable to process database file ‘{self.filepath}’')


def main():
    pass


if __name__ == '__main__':
    main()
