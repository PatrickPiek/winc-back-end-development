from datetime import datetime


def filter_list(data=[], column='', keys=[]):
    """Filter a list of dictionaries by one or more keys

    data is a list of dictionaries
    column in the column to filter, e.g. product_name
    keys are one or more values to filter on, e.g. ‘orange’

    Returns the filtered list
    """
    if len(keys) == 0 or len(data) == 0:
        return []
    return list(filter(lambda row: row[column] in keys, data))


def filter_list_by_date(data=[], column='', date=''):
    """Filter a list of dictionaries by date

    data is a list of dictionaries
    column in the column to filter, e.g. sell_date
    date is a valid datetime object

    Returns the filtered list
    """
    if not isinstance(date, datetime):
        raise ValueError('We need a valid datetime object')

    if len(data) == 0:
        return []

    return [d for d in data if d[column] <= date]


def filter_list_by_date_range(data=[], column='', start='', end=''):
    """Filter a list of dictionaries by start and end date (range)

    data is a list of dictionaries
    column in the column to filter, e.g. sell_date
    start is a valid ‘start date’ datetime object
    end is a valid end date’ datetime object

    Returns the filtered list
    """
    if not isinstance(start, datetime) or not isinstance(end, datetime):
        raise ValueError('We need a valid datetime object')

    if len(data) == 0:
        return []

    return [d for d in data if d[column] >= start and d[column] <= end]


def main():
    pass


if __name__ == '__main__':
    main()
