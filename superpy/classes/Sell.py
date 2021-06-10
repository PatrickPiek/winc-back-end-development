# python ./super.py sell --product-name orange --price 2
# python ./super.py sell --product-name peach --price 3.95

import sys

import config

from classes.Database import Database
from classes.Today import Today

from functions.filter import filter_list
from functions.sort import sort_list
from functions.args import check_required_arguments


class Sell():
    """Handles the SuperPy sell action
    Uses the bought and products database to record the sell action
    Sold products that are in inventory are stored in the sold database
    The product with the earliest expiration date is sold first
    """

    def __init__(self, args):

        self.args = args

        check_required_arguments(
            args, ('product_name', 'price'))

        self.database_bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)

        self.database_sold = Database(
            config.SOLD_FILE, config.SOLD_FIELDS)

    def run(self):

        bought_id = self.get_bought_id()

        if bought_id == None:
            return 'ERROR: Product not in stock'

        self.database_sold.add(
            {
                'id': self.database_sold.rowcount + 1,
                'bought_id': bought_id,
                'sell_date': Today().get_date(),
                'sell_price': self.args['price'],
            })

        return 'OK'

    def get_bought_id(self):

        inventory = filter_list(
            self.database_bought.data, 'product_name', [self.args['product_name']])

        if len(inventory) == 0:
            return None

        # sell the product with the earliest expiration date
        inventory = sort_list(inventory, 'expiration_date')

        if len(inventory) == 1:
            return inventory[0]['id']

        for item in inventory:
            is_sold = filter_list(
                self.database_sold.data, 'bought_id', [item['id']])

            if len(is_sold) == 0:
                return item['id']

        return None


def main():
    pass


if __name__ == '__main__':
    main()
