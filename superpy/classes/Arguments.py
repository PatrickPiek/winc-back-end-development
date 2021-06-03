import argparse
import sys

from functions import convert_to_date
from functions import convert_to_price
from functions import is_valid_export_type


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
                            )

        parser.add_argument('--product-name',
                            type=str,
                            action='store',
                            help='the short name of the product to buy or sell (e.g. ‘orange’)',
                            )

        parser.add_argument('--price',
                            type=convert_to_price,
                            action='store',
                            help='the price of the product to buy or sell (e.g. ‘2.95’)',
                            )

        parser.add_argument('--expiration-date',
                            type=convert_to_date,
                            action='store',
                            help='the expiration date of the product to buy or sell; format as ‘yyyy-mm-dd’',
                            )

        parser.add_argument('--advance-time',
                            type=int,
                            action='store',
                            help='advance the time by n days; where n >= 0; 0 will reset to today’s date',
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
                            )

        parser.add_argument('--export-format',
                            type=is_valid_export_type,
                            action='store',
                            help='export inventory: csv, json or xlsx',
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
