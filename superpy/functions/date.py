from calendar import monthrange
from datetime import datetime

import config


def convert_to_date(value=''):
    try:
        return datetime.strptime(value, config.YEAR_FORMAT)
    except ValueError:
        try:
            return datetime.strptime(value, config.YEAR_MONTH_FORMAT)
        except ValueError:
            try:
                return datetime.strptime(value, config.DATE_FORMAT)
            except ValueError:
                raise ValueError('Not a valid date: ‘{value}’')


def format_date(date):
    if isinstance(date, datetime):
        return date.strftime(config.DATE_FORMAT)
    raise ValueError('We need a a valid datetime object')


def make_date():
    return datetime.today().strftime(config.DATE_FORMAT)


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


def main():
    pass


if __name__ == '__main__':
    main()
