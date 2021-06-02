from datetime import datetime
from datetime import timedelta
from calendar import monthrange
from os.path import abspath, exists
import csv
import config
import xlsxwriter
import json


def convert_to_date(value=''):
    try:
        return datetime.strptime(value, '%Y')
    except ValueError:
        try:
            return datetime.strptime(value, '%Y-%m')
        except ValueError:
            try:
                return datetime.strptime(value, config.DATE_FORMAT)
            except ValueError:
                msg = 'Not a valid date: ‘{0}’.'.format(value)
                raise ValueError(msg)


def convert_to_price(value):
    try:
        return int(value)

    except ValueError:
        try:
            return float(value)

        except ValueError:
            msg = 'Not a valid price: ‘{0}’.'.format(value)
            raise ValueError(msg)


def is_valid_export_type(value=''):
    if value not in ('csv', 'json', 'xlsx'):
        raise ValueError('We need a valid export type: csv, json or xlsx')
    return value


def format_date(date):
    if isinstance(date, datetime):
        return date.strftime(config.DATE_FORMAT)
    raise ValueError('We need a a valid datetime object')


def make_date():
    return datetime.today().strftime(config.DATE_FORMAT)


def make_filename(prefix='', suffix=''):
    return f'{prefix}{datetime.today().strftime(config.DATE_FORMAT_FILENAME)}{suffix}'


def filter_list(data=[], column='', keys=[]):
    if len(keys) == 0 or len(data) == 0:
        return []
    return list(filter(lambda row: row[column] in keys, data))


def filter_list_by_date(data=[], column='', date=''):
    if len(data) == 0:
        return []

    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    return [d for d in data if d[column] <= date]


def filter_list_by_date_range(data=[], column='', start='', end=''):
    if len(data) == 0:
        return []

    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise ValueError('We need a valid datetime object')

    return [d for d in data if d[column] >= start and d[column] <= end]


def sort_list(data=[], column=''):
    if len(data) == 0:
        return []
    if len(data) == 1:
        return data
    return sorted(data, key=lambda key: key[column])


def last_day_of_month(date=''):
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    year = int(date.strftime('%Y'))
    month = int(date.strftime('%m'))
    day = monthrange(year, month)[1]

    return datetime(year, month, day)


def last_day_of_year(date=''):
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    year = int(date.strftime('%Y'))

    return datetime(year, 12, 31)


def format_currency(value=0):
    return '€ {:,.2f} '.format(float(value))


def date_as_string(date=''):
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')


def create_csv_file(filename, fieldnames, data):

    filepath = abspath(f'./{filename}')

    with open(filepath, mode='w+') as csv_file:

        file_ref = csv.DictWriter(
            csv_file, fieldnames=fieldnames, delimiter=',', doublequote=True, escapechar='\\',
            lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True,
            strict=True)

        file_ref.writeheader()

        for row in data:
            file_ref.writerow(row)


def create_xlsx_file(filename: str, headers: list, items: dict):

    # adapted from: https://stackoverflow.com/questions/14637853/how-do-i-output-a-list-of-dictionaries-to-an-excel-sheet/30357389

    filepath = abspath(f'./{filename}')

    with xlsxwriter.Workbook(filepath) as workbook:

        worksheet = workbook.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers)

        for index, item in enumerate(items):
            row = map(lambda field_id: item.get(field_id, ''), headers)
            worksheet.write_row(row=index + 1, col=0, data=row)


def create_json_file(filename: str, data: dict):
    filepath = abspath(f'./{filename}')

    with open(filepath, 'w+') as json_file:
        json.dump(data, json_file, sort_keys=True,
                  indent=4, ensure_ascii=False)


def main():
    pass


if __name__ == '__main__':
    main()
