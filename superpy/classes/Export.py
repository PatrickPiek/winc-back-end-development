# super.py export --database bought --today --export-format csv
# super.py export --database bought --yesterday --export-format csv
# super.py export --database bought --date 2021-06 --export-format csv
# super.py export --database sold --date 2021-06 --export-format xlsx
# super.py export --database products --date 2021 --export-format json

from datetime import datetime
from datetime import timedelta

import config

from classes.Database import Database
from classes.Today import Today

from functions import export_csv
from functions import export_json
from functions import export_xlsx

from functions import convert_to_date
from functions import filter_list_by_date
from functions import filter_list_by_date_range
from functions import format_date
from functions import last_day_of_month
from functions import last_day_of_year
from functions import make_filename


class Export():

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

        # --now, --today and --yesterday
        today = Today().get_date()
        today = datetime.strptime(today, config.DATE_FORMAT)

        if self.args['yesterday'] == True:
            today = Today().get_date()
            today = datetime.strptime(today, config.DATE_FORMAT)
            today = today + timedelta(days=-1)

        self.today = today

        # --date <date>
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

        # --export
        self.export = self.args['export_format']

        # filter
        self.filter = None
        if self.args['now'] == True or \
                self.args['today'] == True or \
                self.args['yesterday'] == True:
            self.filter = 'date'
        elif self.date != None:
            self.filter = 'range'

    def run(self):

        data = []

        if self.database_name == 'bought':
            if self.filter == 'range':
                data = filter_list_by_date_range(
                    self.database.data, 'buy_date', self.date_start, self.date_end)
            elif self.filter == 'date':
                data = filter_list_by_date(
                    self.database.data, 'buy_date', self.today)
            else:
                data = self.database.data

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
            data = self.database.data

        if len(data) == 0:
            return 'WARNING: No data to export'

        processed = []
        for row in data:
            rowdata = {}
            for column in self.database.columns:
                if column in config.DATE_FIELDS:
                    rowdata[column] = format_date(row[column])
                else:
                    rowdata[column] = row[column]
            processed.append(rowdata)
        data = processed

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
