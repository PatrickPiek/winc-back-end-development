# python ./super.py report profit --now
# python ./super.py report profit --today
# python ./super.py report profit --yesterday
# python ./super.py report profit --date 2021
# python ./super.py report profit --date 2021-06
# python ./super.py report profit --date 2021-06-02

from datetime import datetime
from datetime import timedelta
from rich import print
from tabulate import tabulate

import config

from classes.Database import Database
from classes.Today import Today

from functions.currency import format_currency
from functions.date import convert_to_date
from functions.date import format_date
from functions.date import last_day_of_month
from functions.date import last_day_of_year
from functions.filter import filter_list
from functions.filter import filter_list_by_date
from functions.filter import filter_list_by_date_range


class Profit():
    """Calculate profit and return the value to CLI
    Uses the bought and sold database
    Products that are bought and sold within a specific timeframe are calculated
    Calculation is based on the --now, --today --yesterday or --date argument
    """

    def __init__(self, args):

        self.args = args
        self.database_bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)
        self.database_sold = Database(
            config.SOLD_FILE, config.SOLD_FIELDS)

        # parse --now, --today and --yesterday
        today = Today().get_date()
        today = datetime.strptime(today, config.DATE_FORMAT)

        if self.args['yesterday'] == True:
            today = Today().get_date()
            today = datetime.strptime(today, config.DATE_FORMAT)
            today = today + timedelta(days=-1)

        self.today = today

        # parse --date <date>
        self.date_format = None
        self.date_start = None
        self.date_end = None

        self.date = self.args['date']
        if self.args['date'] != None:

            if(len(self.date) == 10):  # yyyy-mm-dd
                self.date_format = config.REPORT_DATE_FORMAT
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)

            elif len(self.date) == 7:  # yyyy-mm
                self.date_format = config.REPORT_YEAR_MONTH_FORMAT
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)
                self.date_end = last_day_of_month(self.date_end)

            elif len(self.date) == 4:  # yyyy
                self.date_format = config.REPORT_YEAR_FORMAT
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)
                self.date_end = last_day_of_year(self.date_end)

            if self.date_start == None:
                raise ValueError('We need a valid date or date range')

    def run(self):

        if self.args['now'] == True or self.args['today'] == True or self.args['yesterday'] == True:

            sold_today = filter_list_by_date(
                self.database_sold.data, 'sell_date', self.today)

            # calculate profit
            profit = 0
            for item in sold_today:
                bought_for = 0
                bought_item = filter_list(
                    self.database_bought.data, 'id', [item['bought_id']])

                if len(bought_item) > 0:
                    bought_for = bought_item[0]['buy_price']

                profit = profit + \
                    (float(item['sell_price']) - float(bought_for))

            if self.args['now'] == True or self.args['today'] == True:
                if profit == 0:
                    return 'No profit today so far'
                return f'Today’s profit so far: {format_currency(profit)}'

            if self.args['yesterday'] == True:
                if profit == 0:
                    return 'No profit for yesterday'
                return f'Yesterday’s profit: {format_currency(profit)}'

        sold = filter_list_by_date_range(
            self.database_sold.data, 'sell_date', self.date_start, self.date_end)

        profit = 0
        for item in sold:
            bought_for = 0
            bought_item = filter_list(
                self.database_bought.data, 'id', [item['bought_id']])

            if len(bought_item) > 0:
                bought_for = bought_item[0]['buy_price']

            profit = profit + (float(item['sell_price']) - float(bought_for))

        return f'Profit from {self.date_start.strftime(self.date_format)}: {format_currency(profit)}'


def main():
    pass


if __name__ == '__main__':
    main()
