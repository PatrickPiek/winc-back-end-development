# super.py report inventory --now
# super.py report inventory --today

import config
from Database import Database
from Today import Today
from functions import format_date
from datetime import datetime
from datetime import timedelta
from tabulate import tabulate
from rich import print
from functions import filter_list
from functions import sort_list
from functions import filter_list_by_date


class Inventory():

    def __init__(self, args):

        self.args = args
        self.database_bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)
        self.database_sold = Database(
            config.SOLD_FILE, config.SOLD_FIELDS)

        today = Today().get_date()
        today = datetime.strptime(today, config.DATE_FORMAT)

        if self.args['yesterday'] == True:
            today = Today().get_date()
            today = datetime.strptime(today, config.DATE_FORMAT)
            today = today + timedelta(days=-1)

        self.today = today

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
                    inventory[0]['count'] = inventory[0]['count'] + 1
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
            report.append({
                'Product Name': item['product_name'].title(),
                'Count': item['count'],
                'Buy Price': '€ {:,.2f}'.format(float(item['buy_price'])),
                'Sum Price': '€ {:,.2f}'.format(int(item['count']) * float(item['buy_price'])),
                'Expiration Date': format_date(item['expiration_date']),
                'Expired': 'Yes' if Today().get_date() > format_date(item['expiration_date']) else 'No'})

        print(format_date(self.today))

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
