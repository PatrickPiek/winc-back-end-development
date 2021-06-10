from os import makedirs
from os.path import abspath, exists

import csv

import config

from datetime import datetime
from functions.export import make_missing_dir


class Database():
    """Creates, reads from and writes to a database file in CSV format
    Database names and field/column names are stored in config.py
    Creates a databases directory if needed
    Creates a new database file if needed
    Appends data to an existing database file for quick writes
    Reads data from an existing file and converts dates
      stored as string to valid datetime objects for date calculations
    """

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

                # convert date fields/columns to valid datetime objects
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

        # validate column names
        for column in row:
            if column not in self.columns:
                raise ValueError(
                    f'Column ‘{column}’ is not a valid property for this database')

        # validate required columns
        for column in self.columns:
            if column not in row:
                raise ValueError(
                    f'Column ‘{column}’ is a required property for this database')

        self.data.append(row)
        self.rowcount = len(self.data)

        try:
            # append row to existing database file for quick writes
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
            # create a new database file if needed
            if not exists(self.filepath):

                self.data = []
                self.save()

        except OSError:
            raise OSError(
                f'Unable to save to database file ‘{self.filepath}’')


def main():
    pass


if __name__ == '__main__':
    main()
