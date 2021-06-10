# python ./super.py export --database bought --today --export-format csv
# python ./super.py export --database bought --yesterday --export-format csv
# python ./super.py export --database bought --date 2021-06 --export-format csv
# python ./super.py export --database sold --date 2021-06 --export-format xlsx
# python ./super.py export --database products --date 2021 --export-format json

from datetime import datetime
from datetime import timedelta

import config

from classes.Database import Database
from classes.Today import Today

from functions.date import convert_to_date
from functions.date import format_date
from functions.date import last_day_of_month
from functions.date import last_day_of_year
from functions.export import export_csv
from functions.export import export_json
from functions.export import export_xlsx
from functions.export import make_filename
from functions.filter import filter_list_by_date
from functions.filter import filter_list_by_date_range


class Export():
    """Export raw data from CSV database files
    Uses bought, sold and products database
    Filters raw data based on CLI --date argument
    Outputs data to a CSV, XLSX or JSON file
      based on CLI --export-format argument
    """

    def __init__(self, args):

        self.args = args

        # --database
        self.database_name = args['database']

        if self.database_name == 'bought':
            self.database = Database(
                config.BOUGHT_FILE, config.BOUGHT_FIELDS)

        elif self.database_name == 'sold':
            self.database = Database(
                config.SOLD_FILE, config.SOLD_FIELDS)

        elif self.database_name == 'products':
            self.database = Database(
                config.PRODUCTS_FILE, config.PRODUCTS_FIELDS)

        # parse --now, --today and --yesterday
        today = Today().get_date()
        today = datetime.strptime(today, config.DATE_FORMAT)

        if self.args['yesterday'] == True:
            today = Today().get_date()
            today = datetime.strptime(today, config.DATE_FORMAT)
            today = today + timedelta(days=-1)

        self.today = today

        # parse --date <date>
        self.date_start = None
        self.date_end = None
        self.date = self.args['date']

        if self.date != None:

            if(len(self.date) == 10):  # yyyy-mm-dd
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)

            elif len(self.date) == 7:  # yyyy-mm
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)
                self.date_end = last_day_of_month(self.date_end)

            elif len(self.date) == 4:  # yyyy
                self.date_start = convert_to_date(self.date)
                self.date_end = convert_to_date(self.date)
                self.date_end = last_day_of_year(self.date_end)

            if self.date_start == None:
                raise ValueError('We need a valid date or date range')

        # --export-format
        self.export = self.args['export_format']

        # parse filter type
        self.filter = None
        if self.args['now'] == True or \
                self.args['today'] == True or \
                self.args['yesterday'] == True:
            self.filter = 'date'
        elif self.date != None:
            self.filter = 'range'

    def run(self):

        data = []

        # filter data from bought database
        if self.database_name == 'bought':
            if self.filter == 'range':
                data = filter_list_by_date_range(
                    self.database.data, 'buy_date', self.date_start, self.date_end)
            elif self.filter == 'date':
                data = filter_list_by_date(
                    self.database.data, 'buy_date', self.today)
            else:
                data = self.database.data

        # filter data from sold database
        elif self.database_name == 'sold':
            if self.filter == 'range':
                data = filter_list_by_date_range(
                    self.database.data, 'sell_date', self.date_start, self.date_end)
            elif self.filter == 'date':
                data = filter_list_by_date(
                    self.database.data, 'sell_date', self.today)
            else:
                data = self.database.data
        else:
            # use data from products database
            data = self.database.data

        if len(data) == 0:
            return 'ERROR: No data to export'

        # convert datetime objects to string dates for date fields
        # see config.DATE_FIELDS
        data_with_formatted_dates = []
        for row in data:
            columns = {}
            for column in self.database.columns:
                if column in config.DATE_FIELDS:
                    columns[column] = format_date(row[column])
                else:
                    columns[column] = row[column]
            data_with_formatted_dates.append(columns)
        data = data_with_formatted_dates

        # export data to a file in the required format
        if self.export == 'csv':
            filename = make_filename(f'export_{self.database_name}_', '.csv')
            export_csv(filename, self.database.columns, data)
        elif self.export == 'xlsx':
            filename = make_filename(f'export_{self.database_name}_', '.xlsx')
            export_xlsx(filename, self.database.columns, data)
        elif self.export == 'json':
            filename = make_filename(f'export_{self.database_name}_', '.json')
            export_json(filename, data)

        return 'OK'


def main():
    pass


if __name__ == '__main__':
    main()
