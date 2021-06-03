from datetime import datetime
import argparse
import sys

import config

from functions.parse import parse_price
from functions.validate import validate_action
from functions.validate import validate_database
from functions.validate import validate_date
from functions.validate import validate_expiration_date
from functions.validate import validate_export_format
from functions.validate import validate_report


class Arguments():

    def __init__(self):

        parser = argparse.ArgumentParser(
            description='SuperPy', prefix_chars='--')

        parser.add_argument('action',
                            type=str,
                            action='store',
                            help='the action to perform: buy, sell, report or export',
                            nargs='?',
                            )

        parser.add_argument('report',
                            type=str,
                            action='store',
                            help='the report action to perform: inventory, revenue or profit',
                            nargs='?',
                            )

        parser.add_argument('--database',
                            type=str,
                            action='store',
                            help='the database to export: bought, sold or products',
                            metavar='',
                            )

        parser.add_argument('--product-name',
                            type=str,
                            action='store',
                            help='the short name of the product to buy or sell (e.g. ‘orange’)',
                            metavar='',
                            )

        parser.add_argument('--price',
                            type=str,
                            action='store',
                            help='the price of the product to buy or sell (e.g. ‘2.95’)',
                            metavar='',
                            )

        parser.add_argument('--expiration-date',
                            type=str,
                            action='store',
                            help='the expiration date of the product to buy or sell; format as ‘yyyy-mm-dd’',
                            metavar='',
                            )

        parser.add_argument('--advance-time',
                            type=int,
                            action='store',
                            help='advance the time by n days; where n >= 0; 0 will reset to today’s date',
                            metavar='',
                            )

        parser.add_argument('--now',
                            action='store_true',
                            help='create report based on current data; relative to ‘today’ setting',
                            )

        parser.add_argument('--yesterday',
                            action='store_true',
                            help='create report based on yesterday’s data; relative to ‘today’ setting',
                            )

        parser.add_argument('--today',
                            action='store_true',
                            help='create report on today’s data; relative to ‘today’ setting',
                            )

        parser.add_argument('--date',
                            type=str,
                            action='store',
                            help='report argument; format as ‘yyyy’, ‘yyyy-mm’ or ‘yyyy-mm-dd’',
                            metavar='',
                            )

        parser.add_argument('--export-format',
                            type=str,
                            action='store',
                            help='export inventory: csv, json or xlsx',
                            metavar='',
                            )

        self.args = parser.parse_args()
        self.vars = vars(self.args)

        # validate inputs
        validate_action(self.vars['action'])
        validate_report(self.vars['report'])
        validate_database(self.vars['database'])
        validate_database(self.vars['database'])
        validate_export_format(self.vars['export_format'])
        validate_expiration_date(self.vars['expiration_date'])
        validate_date(self.vars['date'])

        # parse inputs
        self.vars['price'] = parse_price(self.vars['price'])

        # display help
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
