# python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01

import config
from classes.Database import Database
from classes.Today import Today
from classes.Barcode import Barcode
from functions import format_date
from functions import filter_list


class Buy():

    def __init__(self, args):

        self.args = args
        self.database_bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)
        self.database_products = Database(
            config.PRODUCTS_FILE, config.PRODUCTS_FIELDS)
        self.product_name = args['product_name']

    def run(self):

        product = filter_list(
            self.database_products.data, 'product_name', [self.product_name])
        barcode = ''
        if len(product) == 0:
            barcode = Barcode(config.BRANCH_BARCODE_PREFIX)
            self.database_products.add({
                'product_name':     self.product_name,
                'full_name':        self.product_name.title(),
                'ean13':            barcode,
            })
        else:
            barcode = product[0]['ean13']

        self.database_bought.add(
            {
                'id':               self.database_bought.rowcount + 1,
                'product_name':     self.product_name,
                'buy_date':         Today().get_date(),
                'buy_price':        self.args['price'],
                'expiration_date':  format_date(self.args['expiration_date']),
                'ean13':            barcode
            })

        return 'OK'


def main():
    pass


if __name__ == '__main__':
    main()
