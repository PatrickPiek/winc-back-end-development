from calendar import monthrange
from datetime import datetime

import config


def convert_to_date(value=''):
    """Function called by argparse to validate CLI date input

    Requires to be:
    a valid year, see config.YEAR_FORMAT,
    a valid year and month, see config.YEAR_MONTH_FORMAT
    or a valid full date, see config.DATE_FORMAT

    Returns:
    a datetime object used for date calculations
    """
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
    """Formats a date string from a datetime object, see config.DATE_FORMAT"""
    if isinstance(date, datetime):
        return date.strftime(config.DATE_FORMAT)
    raise ValueError('We need a a valid datetime object')


def make_date():
    """Formats a date string from today’s date, see config.DATE_FORMAT"""
    return datetime.today().strftime(config.DATE_FORMAT)


def last_day_of_month(date=''):
    """Calculates the last day of the current month

    Requires:
    a valid datetime object

    Returns:
    a datetime object

    Used for:
    date calculations between two dates
    """
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    year = int(date.strftime('%Y'))
    month = int(date.strftime('%m'))
    day = monthrange(year, month)[1]

    return datetime(year, month, day)


def last_day_of_year(date=''):
    """Calculates the last day of the current year

    Requires:
    a valid datetime object

    Returns:
    a datetime object

    Used for:
    date calculations between two dates
    """
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    year = int(date.strftime('%Y'))

    return datetime(year, 12, 31)


def main():
    pass


if __name__ == '__main__':
    main()
