# python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01

import config
from Database import Database
from Today import Today
from format_date import format_date


class Buy():

    def __init__(self, args):

        self.args = args
        self.bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)

    def execute(self):

        self.bought.add(
            {
                'id':               self.bought.rowcount + 1,
                'product_name':     self.args['product_name'],
                'buy_date':         Today({}).get(),
                'buy_price':        self.args['price'],
                'expiration_date':  format_date(self.args['expiration_date']),
            })

        print('OK')


def main():
    pass


if __name__ == '__main__':
    main()
