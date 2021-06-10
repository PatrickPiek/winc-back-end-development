from datetime import datetime

from os import makedirs
from os.path import abspath, exists

import config
import csv
import json
import xlsxwriter


def make_filename(prefix='', suffix=''):
    """Generates a filename using today’s date and time,
    see (config.DATE_FORMAT_FILENAME
    Prepends a string prefix
    Appends a string suffix
    Returns a string: export_sold_20210610_090523.json where
    'export_sold_' is the prefix and '.json' the suffix
    """
    return f'{prefix}{datetime.today().strftime(config.DATE_FORMAT_FILENAME)}{suffix}'


def export_csv(filename, fieldnames, data):
    """Exports fields in data, defined in fieldnames, as CSV to a file"""
    directory = config.EXPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_csv_file(filepath, fieldnames, data)


def export_xlsx(filename, fieldnames, data):
    """Exports fields in data, defined in fieldnames, as Excel XML to a file"""
    directory = config.EXPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_xlsx_file(filepath, fieldnames, data)


def export_json(filename, data):
    """Exports fields in data, defined in fieldnames, as JSON data to a file"""
    directory = config.EXPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_json_file(filepath, data)


def report_csv(filename, fieldnames, data):
    """Exports a report with fields in data, defined in fieldnames, as CSV to a file"""
    directory = config.REPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_csv_file(filepath, fieldnames, data)


def report_xlsx(filename, fieldnames, data):
    """Exports a report with fields in data, defined in fieldnames, as Excel XML to a file"""
    directory = config.REPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_xlsx_file(filepath, fieldnames, data)


def report_json(filename, data):
    """Exports a report with fields in data, defined in fieldnames, as JSON data to a file"""
    directory = config.REPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_json_file(filepath, data)


def create_csv_file(filepath, fieldnames, data):
    with open(filepath, mode='w+') as f:
        file_ref = csv.DictWriter(
            f, fieldnames=fieldnames, delimiter=',', doublequote=True, escapechar='\\',
            lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True,
            strict=True)
        file_ref.writeheader()
        for row in data:
            file_ref.writerow(row)


def create_xlsx_file(filepath, headers, data):
    with xlsxwriter.Workbook(filepath) as w:
        worksheet = w.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers)
        for index, item in enumerate(data):
            row = map(lambda field_id: item.get(field_id, ''), headers)
            worksheet.write_row(row=index + 1, col=0, data=row)


def create_json_file(filepath, data):
    with open(filepath, 'w+') as j:
        json.dump(data, j, sort_keys=True, indent=4, ensure_ascii=False)


def make_missing_dir(dir=''):
    """Checks if a directory is missing and creates one when needed"""
    if dir == '':
        raise ValueError('A valid directory name is required')
    try:
        if not exists(abspath(f'./{dir}')):
            makedirs(abspath(f'./{dir}'))
    except:
        raise OSError(f'Unable to create directory ‘./{dir}’')


def main():
    pass


if __name__ == '__main__':
    main()
