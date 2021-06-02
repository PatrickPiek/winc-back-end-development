import argparse
import sys

from functions import convert_to_date
from functions import convert_to_price


class Arguments():

    def __init__(self):

        parser = argparse.ArgumentParser(
            description='SuperPy', prefix_chars='--')

        parser.add_argument('action',
                            type=str,
                            action='store',
                            metavar='action',
                            help='the action to perform (buy, sell, report)',
                            nargs='?',
                            )

        parser.add_argument('report',
                            type=str,
                            action='store',
                            metavar='report',
                            help='the report action to perform (revenue, profit, inventory)',
                            nargs='?',
                            )

        parser.add_argument('--product-name',
                            type=str,
                            action='store',
                            metavar='',
                            help='the name of the product to buy or sell',
                            )

        parser.add_argument('--price',
                            type=convert_to_price,
                            action='store',
                            metavar='',
                            help='the price of the product to buy or sell',
                            )

        parser.add_argument('--expiration-date',
                            type=convert_to_date,
                            action='store',
                            metavar='',
                            help='the expiration date of the product to buy or sell (yyyy-mm-dd)',
                            )

        parser.add_argument('--advance-time',
                            type=int,
                            action='store',
                            metavar='',
                            help='advance the time by n days',
                            )

        parser.add_argument('--now',
                            action='store_true',
                            help='report argument',
                            )

        parser.add_argument('--yesterday',
                            action='store_true',
                            help='report argument',
                            )

        parser.add_argument('--today',
                            action='store_true',
                            help='report argument',
                            )

        parser.add_argument('--date',
                            type=convert_to_date,
                            action='store',
                            metavar='',
                            help='report argument (yyyy-mm-dd)',
                            )

        self.args = parser.parse_args()
        self.vars = vars(self.args)

        if self.vars['action'] == None and self.vars['advance_time'] == None:
            self.display_help(parser)

        if self.vars['action'] == 'report' and self.vars['report'] == None:
            self.display_help(parser)

    def display_help(self, parser):
        parser.print_help()
        sys.exit(0)


def main():
    pass


if __name__ == '__main__':
    main()
