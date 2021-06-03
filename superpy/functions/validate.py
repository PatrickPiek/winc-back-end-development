from datetime import datetime

import config


def validate_action(action):
    if action != None:
        if action not in ('buy', 'sell', 'report', 'export'):
            raise ValueError(
                'The argument ‘action’ requires one of: buy, sell, report or export')


def validate_report(report):
    if report != None:
        if report not in ('inventory', 'revenue', 'profit'):
            raise ValueError(
                'The argument ‘report’ requires one of: inventory, revenue or profit')


def validate_database(database):
    if database != None:
        if database not in ('bought', 'sold', 'products'):
            raise ValueError(
                'The argument ‘--database’ requires one of: bought, sold or products')


def validate_export_format(export_format):
    if export_format != None:
        if export_format not in ('csv', 'json', 'xlsx'):
            raise ValueError(
                'The ‘--export_format’ argument requires one of: csv, json or xlsx')


def validate_expiration_date(date):
    if date != None:
        if len(date) != 10:
            raise ValueError(
                'The ‘--expiration-date’ argument is not valid')
        try:
            datetime.strptime(date, config.DATE_FORMAT)
        except ValueError:
            raise ValueError(
                'The ‘--expiration-date’ argument is not valid')


def validate_date(date):
    if date != None:
        if len(date) not in (4, 7, 10):
            raise ValueError(
                'The ‘--date’ argument is not valid')
        try:
            datetime.strptime(date, config.YEAR_FORMAT)
        except ValueError:
            try:
                datetime.strptime(date, config.YEAR_MONTH_FORMAT)
            except ValueError:
                try:
                    datetime.strptime(date, config.DATE_FORMAT)
                except ValueError:
                    raise ValueError('The ‘--date’ argument is not valid')


def main():
    pass


if __name__ == '__main__':
    main()
