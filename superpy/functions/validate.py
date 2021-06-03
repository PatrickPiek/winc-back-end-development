from datetime import datetime

import config


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
