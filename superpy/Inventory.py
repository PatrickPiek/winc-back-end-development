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


class Inventory():

    def __init__(self, args):

        self.args = args
        self.bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)
        self.sold = Database(
            config.SOLD_FILE, config.SOLD_FIELDS)

        date = Today().get_date()
        date = datetime.strptime(date, config.DATE_FORMAT)

        if self.args['yesterday'] == True:
            date = Today().get_date()
            date = datetime.strptime(date, config.DATE_FORMAT)
            date = date + timedelta(days=-1)

        self.date = date

    def run(self):

        # collect all items that are not yet sold

        inventory = []

        print(self.bought.data)

        for b in self.bought.data:
            sold_state = False
            for s in self.sold.data:
                if b['id'] == s['bought_id']:
                    if self.date >= b['buy_date']:
                        sold_state = True
            if sold_state == False:
                b['count'] = 1
                b['id'] = None
                inventory.append({
                    'Product Name': b['product_name'],
                    'Count': 1,
                    'Buy Price': b['buy_price'],
                    'Expiration Date': format_date(b['expiration_date']),
                })

        # merge the same products and update counts

        # report = []

        # for inventory_item in inventory:
        #     if inventory_item not in report:
        #         report.append(inventory_item)
        #     else:
        #         for report_item in report:
        #             if inventory_item == report_item:
        #                 #  split array and merge arrays

        # print(self.date)

        return tabulate(
            inventory,
            headers='keys',
            tablefmt='grid'
        )


def main():
    pass


if __name__ == '__main__':
    main()
