import argparse
from function__is_valid_date import is_valid_date


def parse_cli_arguments():

    cli = argparse.ArgumentParser(description='SuperPy', prefix_chars='--')

    cli.add_argument('action', type=str, action='store', metavar='action',
                     help='the action to perform (buy, sell, report, time)',
                     choices=['buy', 'sell', 'report', 'time'], nargs='?')

    cli.add_argument('report', type=str, action='store', metavar='report',
                     help='the report action to perform (revenue, profit)',
                     choices=['revenue', 'profit'], nargs='?')

    cli.add_argument('--product-name', type=str, action='store', metavar='',
                     help='the name of the product to buy or sell')

    cli.add_argument('--price', type=str, action='store', metavar='',
                     help='the price of the product to buy or sell')

    cli.add_argument('--expiration-date', type=is_valid_date, action='store', metavar='',
                     help='the expiration date of the product to buy or sell (yyyy-mm-dd)')

    cli.add_argument('--forward', type=int, action='store', metavar='',
                     help='forward the time by n days')

    cli.add_argument('--reverse', type=int, action='store', metavar='',
                     help='reverse the time by n days')

    cli.add_argument('--yesterday', action='store_true',
                     help='report argument')

    cli.add_argument('--today', action='store_true',
                     help='report argument')

    cli.add_argument('--date', type=is_valid_date, action='store',
                     metavar='', help='report argument (yyyy-mm-dd)')

    return cli.parse_args()


def main():
    pass


if __name__ == '__main__':
    main()
