# adapted from: https://stackoverflow.com/questions/25470844/specify-date-format-for-python-argparse-input-arguments

from datetime import datetime


def is_valid_date(value=''):

    try:
        return datetime.strptime(value, "%Y")
    except ValueError:
        try:
            return datetime.strptime(value, "%Y-%m")
        except ValueError:
            try:
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                msg = "Not a valid date: '{0}'.".format(value)
                raise ValueError(msg)


def main():
    pass


if __name__ == '__main__':
    main()
