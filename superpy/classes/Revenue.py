# super.py report revenue --now
# super.py report revenue --today
# super.py report revenue --yesterday
# super.py report revenue --date 2021
# super.py report revenue --date 2021-06
# super.py report revenue --date 2021-06-02

from datetime import datetime
from datetime import timedelta
from rich import print
from tabulate import tabulate

import config

from classes.Database import Database
from classes.Today import Today

from functions import convert_to_date
from functions import filter_list
from functions import filter_list_by_date
from functions import filter_list_by_date_range
from functions import format_currency
from functions import format_date
from functions import last_day_of_month
from functions import last_day_of_year


class Revenue():

    def __init__(self, args):

        self.args = args

        self.database_sold = Database(
            config.SOLD_FILE, config.SOLD_FIELDS)

        # --now, --today
        today = Today().get_date()
        today = datetime.strptime(today, config.DATE_FORMAT)

        # --yesterday
        if self.args['yesterday'] == True:
            today = Today().get_date()
            today = datetime.strptime(today, config.DATE_FORMAT)
            today = today + timedelta(days=-1)

        self.today = today

        # --date <date>
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

            revenue = 0
            for item in sold_today:
                revenue = revenue + float(item['sell_price'])

            if self.args['now'] == True or self.args['today'] == True:
                if revenue == 0:
                    return 'No revenue today so far'
                return f'Today’s revenue so far: {format_currency(revenue)}'

            if self.args['yesterday'] == True:
                if revenue == 0:
                    return 'No revenue for yesterday'
                return f'Yesterday’s revenue: {format_currency(revenue)}'

        sold = filter_list_by_date_range(
            self.database_sold.data, 'sell_date', self.date_start, self.date_end)

        revenue = 0
        for item in sold:
            revenue = revenue + float(item['sell_price'])

        return f'Revenue from {self.date_start.strftime(self.date_format)}: {format_currency(revenue)}'


def main():
    pass


if __name__ == '__main__':
    main()
