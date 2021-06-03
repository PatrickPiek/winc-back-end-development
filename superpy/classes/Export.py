# super.py export bought --today --format csv
# super.py export bought --yesterday --format csv
# super.py export bought --date 2021-06 --format csv
# super.py export sold --date 2021-06 --format xlsx
# super.py export products --date 2021 --format json

from datetime import datetime
from datetime import timedelta

import config

from classes.Database import Database
from classes.Today import Today

from functions import create_csv_file
from functions import create_json_file
from functions import create_xlsx_file

from functions import filter_list
from functions import filter_list_by_date
from functions import format_date
from functions import make_filename
from functions import sort_list


class Export():

    def __init__(self, args):

        self.args = args
        self.database_bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)
        self.database_sold = Database(
            config.SOLD_FILE, config.SOLD_FIELDS)
        self.database_products = Database(
            config.PRODUCTS_FILE, config.PRODUCTS_FIELDS)

        today = Today().get_date()
        today = datetime.strptime(today, config.DATE_FORMAT)

        if self.args['yesterday'] == True:
            today = Today().get_date()
            today = datetime.strptime(today, config.DATE_FORMAT)
            today = today + timedelta(days=-1)

        self.today = today

        self.export = self.args['export']

    def run(self):

        inventory = []

        sold_today = filter_list_by_date(
            self.database_sold.data, 'sell_date', self.today)

        bought_today = filter_list_by_date(
            self.database_bought.data, 'buy_date', self.today)

        for item in bought_today:

            is_sold = filter_list(
                sold_today, 'bought_id', [item['id']])

            if len(is_sold) == 0:

                in_report = filter_list(
                    inventory, 'product_name', [item['product_name']])

                in_report = filter_list(
                    in_report, 'buy_price', [item['buy_price']])

                in_report = filter_list(
                    in_report, 'expiration_date', [item['expiration_date']])

                if len(in_report) > 0:
                    index = inventory.index(in_report[0])
                    inventory[index]['count'] = inventory[index]['count'] + 1
                else:
                    inventory.append({
                        'product_name': item['product_name'],
                        'count': 1,
                        'buy_price': item['buy_price'],
                        'expiration_date': item['expiration_date'],
                    })

        if len(inventory) == 0:
            return 'WARNING: Inventory is empty'

        inventory = sort_list(inventory, 'product_name')

        report = []
        for item in inventory:
            product = filter_list(
                self.database_products.data, 'product_name', [item['product_name']])

            report.append({
                'Product Name':     product[0]['full_name'] if len(product) != 0 else item['product_name'],
                'Count':            item['count'],
                'Buy Price':        '€ {:,.2f}'.format(float(item['buy_price'])),
                'Sum Price':        '€ {:,.2f}'.format(int(item['count']) * float(item['buy_price'])),
                'Expiration Date':  format_date(item['expiration_date']),
                'Expired':          'Yes' if Today().get_date() > format_date(item['expiration_date']) else 'No',
                'EAN13':            product[0]['ean13'] if len(product) != 0 else '',
            })

        if self.export == 'csv':
            self.export_csv(report)
        elif self.export == 'xlsx':
            self.export_xlsx(report)
        elif self.export == 'json':
            self.export_json(report)

        return 'OK'

    def export_csv(self, data):
        filename = make_filename('report_inventory_', '.csv')
        create_csv_file(filename, config.INVENTORY_REPORT_FIELDS, data)

    def export_xlsx(self, data):
        filename = make_filename('report_inventory_', '.xlsx')
        create_xlsx_file(filename, config.INVENTORY_REPORT_FIELDS, data)

    def export_json(self, data):
        filename = make_filename('report_inventory_', '.json')
        create_json_file(filename, data)


def main():
    pass


if __name__ == '__main__':
    main()
