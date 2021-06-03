from datetime import datetime

from os import makedirs
from os.path import abspath, exists

import config
import csv
import json
import xlsxwriter


def make_filename(prefix='', suffix=''):
    return f'{prefix}{datetime.today().strftime(config.DATE_FORMAT_FILENAME)}{suffix}'


def export_csv(filename, fieldnames, data):
    directory = config.EXPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_csv_file(filepath, fieldnames, data)


def export_xlsx(filename, fieldnames, data):
    directory = config.EXPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_xlsx_file(filepath, fieldnames, data)


def export_json(filename, data):
    directory = config.EXPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_json_file(filepath, data)


def report_csv(filename, fieldnames, data):
    directory = config.REPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_csv_file(filepath, fieldnames, data)


def report_xlsx(filename, fieldnames, data):
    directory = config.REPORTS_DIR
    make_missing_dir(directory)
    filepath = abspath(f'./{directory}/{filename}')
    create_xlsx_file(filepath, fieldnames, data)


def report_json(filename, data):
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
