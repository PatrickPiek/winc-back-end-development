# python ./super.py report inventory --now
# python ./super.py report inventory --today
# python ./super.py report inventory --today --export-format csv
# python ./super.py report inventory --today --export-format xlsx
# python ./super.py report inventory --today --export-format json

from datetime import datetime
from datetime import timedelta
from rich import print
from tabulate import tabulate

import config

from classes.Database import Database
from classes.Today import Today

from functions.date import format_date
from functions.export import make_filename
from functions.export import report_csv
from functions.export import report_json
from functions.export import report_xlsx
from functions.filter import filter_list
from functions.filter import filter_list_by_date
from functions.sort import sort_list


class Inventory():
    """Report on inventory and return a table report to CLI
    Exports the same report data to a file with the --export-format argument
    Uses the bought, sold and products database
    Products that are bought, but not sold, are in inventory
    Products that are in inventory, but are expired, are listed as expired
    Products in inventory with the same buy_price and expiration_date
      are listed once and counted
    Barcodes are listed for each unique product in inventory
    """

    def __init__(self, args):

        self.args = args

        self.database_bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)

        self.database_sold = Database(
            config.SOLD_FILE, config.SOLD_FIELDS)

        self.database_products = Database(
            config.PRODUCTS_FILE, config.PRODUCTS_FIELDS)

        # parse --now, --today and --yesterday
        today = Today().get_date()
        today = datetime.strptime(today, config.DATE_FORMAT)

        if self.args['yesterday'] == True:
            today = Today().get_date()
            today = datetime.strptime(today, config.DATE_FORMAT)
            today = today + timedelta(days=-1)

        self.today = today

        # --export-format
        self.export = self.args['export_format']

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

                # check if product_name is already in inventory list
                in_report = filter_list(
                    inventory, 'product_name', [item['product_name']])

                # check if product_name and buy_price is already in inventory list
                in_report = filter_list(
                    in_report, 'buy_price', [item['buy_price']])

                # check if product_name, buy_price and expiration_date is already in inventory list
                in_report = filter_list(
                    in_report, 'expiration_date', [item['expiration_date']])

                if len(in_report) > 0:
                    # increase count if product is indeed in the list
                    index = inventory.index(in_report[0])
                    inventory[index]['count'] = inventory[index]['count'] + 1

                else:
                    # add to inventory list
                    inventory.append({
                        'product_name': item['product_name'],
                        'count': 1,
                        'buy_price': item['buy_price'],
                        'expiration_date': item['expiration_date'],
                    })

        if len(inventory) == 0:
            return 'ERROR: Inventory is empty'

        inventory = sort_list(inventory, 'product_name')

        report = []
        for item in inventory:

            # get full product name from products database
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
            filename = make_filename('report_inventory_', '.csv')
            report_csv(filename, config.INVENTORY_REPORT_FIELDS, report)

        elif self.export == 'xlsx':
            filename = make_filename('report_inventory_', '.xlsx')
            report_xlsx(filename, config.INVENTORY_REPORT_FIELDS, report)

        elif self.export == 'json':
            filename = make_filename('report_inventory_', '.json')
            report_json(filename, report)

        return tabulate(
            report,
            headers='keys',
            tablefmt='fancy_grid',
            colalign=('left', 'right', 'right', 'right', 'right', 'left')
        )


def main():
    pass


if __name__ == '__main__':
    main()
