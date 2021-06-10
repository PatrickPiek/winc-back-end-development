# python ./super.py buy --product-name orange --price 0.8 --expiration-date 2020-05-01
# python ./super.py buy --product-name peach --price 2.25 --expiration-date 2020-08-01

import config

from classes.Barcode import Barcode
from classes.Database import Database
from classes.Today import Today

from functions.date import format_date
from functions.filter import filter_list
from functions.args import check_required_arguments


class Buy():
    """Handles the SuperPy buy action
    Uses the bought and products database to record the buy action
    New products are added to the product database,
      complete with a new EAN13 barcode
    Bought products are then stored in the bought database
    """

    def __init__(self, args):

        self.args = args

        check_required_arguments(
            args, ('product_name', 'price', 'expiration_date'))

        self.database_bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)

        self.database_products = Database(
            config.PRODUCTS_FILE, config.PRODUCTS_FIELDS)

        self.product_name = args['product_name']

    def run(self):

        # check id product exists in product database
        product = filter_list(
            self.database_products.data, 'product_name', [self.product_name])

        barcode = ''

        if len(product) == 0:

            # generate a new barcode
            barcode = Barcode(config.STORE_BARCODE_PREFIX)

            # add product to products database
            self.database_products.add({
                'product_name':     self.product_name,
                'full_name':        self.product_name.title(),
                'ean13':            barcode,
            })
        else:

            # use preexisting barcode
            barcode = product[0]['ean13']

        # add buy to bought database
        self.database_bought.add(
            {
                'id':               self.database_bought.rowcount + 1,
                'product_name':     self.product_name,
                'buy_date':         Today().get_date(),
                'buy_price':        self.args['price'],
                'expiration_date':  self.args['expiration_date'],
                'ean13':            barcode
            })

        return 'OK'


def main():
    pass


if __name__ == '__main__':
    main()
