from datetime import datetime
import config


def convert_to_date(value=''):
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


def convert_to_price(value):
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


def filter_list(data=[], column='', keys=[]):
    if len(keys) == 0 or len(data) == 0:
        return []
    return list(filter(lambda row: row[column] in keys, data))


def filter_list_by_date(data=[], column='', date=''):
    if len(data) == 0 or not isinstance(date, datetime):
        return []
    return [d for d in data if d[column] <= date]


def sort_list(data=[], column=''):
    if len(data) == 0:
        return []
    if len(data) == 1:
        return data
    return sorted(data, key=lambda key: key[column])


def main():
    pass


if __name__ == '__main__':
    main()
