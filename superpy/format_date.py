from datetime import datetime
from is_valid_date import is_valid_date


def format_date(date):

    if isinstance(date, datetime):
        return date.strftime('%Y-%m-%d')
    raise ValueError


def main():
    pass


if __name__ == '__main__':
    main()
