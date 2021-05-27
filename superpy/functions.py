from datetime import datetime
import config


def is_valid_date(value=''):
    try:
        return datetime.strptime(value, "%Y")
    except ValueError:
        try:
            return datetime.strptime(value, "%Y-%m")
        except ValueError:
            try:
                return datetime.strptime(value, config.DATE_FORMAT)
            except ValueError:
                msg = "Not a valid date: '{0}'.".format(value)
                raise ValueError(msg)


def is_valid_price(value):
    try:
        return int(value)

    except ValueError:
        try:
            return float(value)

        except ValueError:
            msg = "Not a valid price: '{0}'.".format(value)
            raise ValueError(msg)


def format_date(date):
    if isinstance(date, datetime):
        return date.strftime(config.DATE_FORMAT)
    raise ValueError('date is a valid datetime object')


def make_date():
    return datetime.today().strftime(config.DATE_FORMAT)


def main():
    pass


if __name__ == '__main__':
    main()
