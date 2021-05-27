import argparse
import sys

from is_valid_date import is_valid_date
from is_valid_price import is_valid_price


class Arguments():

    def __init__(self):

        cli = argparse.ArgumentParser(
            description='SuperPy', prefix_chars='--')

        cli.add_argument('action',
                         type=str,
                         action='store',
                         metavar='action',
                         help='the action to perform (buy, sell, report)',
                         nargs='?'
                         )

        cli.add_argument('report',
                         type=str,
                         action='store',
                         metavar='report',
                         help='the report action to perform (revenue, profit, inventory)',
                         nargs='?'
                         )

        cli.add_argument('--product-name',
                         type=str,
                         action='store',
                         metavar='',
                         help='the name of the product to buy or sell'
                         )

        cli.add_argument('--price',
                         type=is_valid_price,
                         action='store',
                         metavar='',
                         help='the price of the product to buy or sell'
                         )

        cli.add_argument('--expiration-date',
                         type=is_valid_date,
                         action='store',
                         metavar='',
                         help='the expiration date of the product to buy or sell (yyyy-mm-dd)'
                         )

        cli.add_argument('--advance-time',
                         type=int,
                         action='store',
                         metavar='',
                         help='advance the time by n days'
                         )

        cli.add_argument('--now',
                         action='store_true',
                         help='report argument'
                         )

        cli.add_argument('--yesterday',
                         action='store_true',
                         help='report argument'
                         )

        cli.add_argument('--today',
                         action='store_true',
                         help='report argument'
                         )

        cli.add_argument('--date',
                         type=is_valid_date,
                         action='store',
                         metavar='',
                         help='report argument (yyyy-mm-dd)'
                         )

        self.args = cli.parse_args()
        self.vars = vars(self.args)

        # print(self.vars)

        if self.vars['action'] == None and self.vars['advance_time'] == None:
            cli.print_help()
            sys.exit(0)


def main():
    pass


if __name__ == '__main__':
    main()
