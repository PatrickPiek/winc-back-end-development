from datetime import datetime
import argparse

# source: https://stackoverflow.com/questions/25470844/specify-date-format-for-python-argparse-input-arguments


def is_valid_date(s):
    try:
        return datetime.strptime(s, "%Y")
    except ValueError:
        try:
            return datetime.strptime(s, "%Y-%m")
        except ValueError:
            try:
                return datetime.strptime(s, "%Y-%m-%d")
            except ValueError:
                msg = "Not a valid date: '{0}'.".format(s)
                raise argparse.ArgumentTypeError(msg)


def main():
    pass


if __name__ == '__main__':
    main()
