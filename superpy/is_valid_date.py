from datetime import datetime

# adapted from: https://stackoverflow.com/questions/25470844/specify-date-format-for-python-argparse-input-arguments


def is_valid_date(date_string=''):

    try:
        return datetime.strptime(date_string, "%Y")
    except ValueError:
        try:
            return datetime.strptime(date_string, "%Y-%m")
        except ValueError:
            try:
                return datetime.strptime(date_string, "%Y-%m-%d")
            except ValueError:
                msg = "Not a valid date: '{0}'.".format(s)
                raise ValueError(msg)


def main():
    pass


if __name__ == '__main__':
    main()
