def parse_price(price):
    """Function called by argparse to validate CLI price input

    Requires to be:
    a valid int or float

    Returns:
    an int or float used for processing price data
    """
    if price != None:
        try:
            return int(price)
        except ValueError:
            try:
                return float(price)
            except ValueError:
                raise ValueError('The ‘--price’ argument is not valid')
    return price


def main():
    pass


if __name__ == '__main__':
    main()
