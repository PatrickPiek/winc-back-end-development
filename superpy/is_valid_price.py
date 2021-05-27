# adapted from: https://pynative.com/python-check-user-input-is-number-or-string/

def is_valid_price(value):

    try:
        return int(value)

    except ValueError:
        try:
            return float(value)

        except ValueError:
            msg = "Not a valid price: '{0}'.".format(value)
            raise ValueError(msg)


def main():
    pass


if __name__ == '__main__':
    main()
