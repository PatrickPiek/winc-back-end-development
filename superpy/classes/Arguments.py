from datetime import datetime
import argparse
import sys

import config

from functions.parse import parse_price
from functions.validate import validate_date
from functions.validate import validate_expiration_date


class Arguments():
    """Parses commandline arguments for SuperPy
    Validates date input from --date and --expiration-date arguments
    Parses price input from --price argument
    Formats and displays SuperPy help (-h, --help) under certain conditions
    """

    def __init__(self):

        parser = argparse.ArgumentParser(
            description='SuperPy', prefix_chars='--')

        parser.add_argument('action',
                            action='store',
                            choices=['buy', 'sell', 'report', 'export'],
                            help='the action to perform: buy, sell, report or export',
                            metavar='action',
                            nargs='?',
                            type=str,
                            )

        parser.add_argument('report',
                            action='store',
                            choices=['inventory', 'revenue', 'profit'],
                            help='the report action to perform: inventory, revenue or profit',
                            metavar='report',
                            nargs='?',
                            type=str,
                            )

        parser.add_argument('--database',
                            action='store',
                            choices=['bought', 'sold', 'products'],
                            help='the database to export: bought, sold or products',
                            metavar='',
                            type=str,
                            )

        parser.add_argument('--product-name',
                            action='store',
                            help='the short name of the product to buy or sell (e.g. ‘orange’)',
                            metavar='',
                            type=str,
                            )

        parser.add_argument('--price',
                            action='store',
                            help='the price of the product to buy or sell (e.g. ‘2.95’)',
                            metavar='',
                            type=str,
                            )

        parser.add_argument('--expiration-date',
                            action='store',
                            help='the expiration date of the product to buy or sell; format as ‘yyyy-mm-dd’',
                            metavar='',
                            type=str,
                            )

        parser.add_argument('--advance-time',
                            action='store',
                            help='advance the time by n days; where n >= 0; 0 will reset to today’s date',
                            metavar='',
                            type=int,
                            )

        parser.add_argument('--now',
                            action='store_true',
                            help='create report based on current data; relative to ‘today’ setting',
                            )

        parser.add_argument('--today',
                            action='store_true',
                            help='create report on today’s data; relative to ‘today’ setting',
                            )

        parser.add_argument('--yesterday',
                            action='store_true',
                            help='create report based on yesterday’s data; relative to ‘today’ setting',
                            )

        parser.add_argument('--date',
                            action='store',
                            help='report argument; format as ‘yyyy’, ‘yyyy-mm’ or ‘yyyy-mm-dd’',
                            metavar='',
                            type=str,
                            )

        parser.add_argument('--export-format',
                            action='store',
                            choices=['csv', 'json', 'xlsx'],
                            help='export inventory: csv, json or xlsx',
                            metavar='',
                            type=str,
                            )

        self.args = parser.parse_args()
        self.vars = vars(self.args)

        # validate date inputs
        validate_expiration_date(self.vars['expiration_date'])
        validate_date(self.vars['date'])

        # parse price inputs
        self.vars['price'] = parse_price(self.vars['price'])

        # display help under certain conditions
        if self.vars['action'] == None and self.vars['advance_time'] == None:
            self.__display_help(parser)

        elif self.vars['action'] == 'report' and self.vars['report'] == None:
            self.__display_help(parser)

        elif self.vars['action'] == 'export' and self.vars['database'] == None:
            self.__display_help(parser)

    def __display_help(self, parser):
        parser.print_help()
        sys.exit(0)


def main():
    pass


if __name__ == '__main__':
    main()
