# python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01

import config
from Database import Database
from format_date import format_date
from is_valid_price import is_valid_price


class Buy():

    def __init__(self, args):

        self.args = args
        self.bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)
        self.today = Database(
            config.TODAY_FILE, config.TODAY_FIELDS)

    def execute(self):

        self.bought.add(
            {
                'id':               self.bought.rowcount + 1,
                'product_name':     self.args['product_name'],
                'buy_date':         self.today.data[0]['today'],
                'buy_price':        self.args['price'],
                'expiration_date':  format_date(self.args['expiration_date']),
            })

        print('OK')


def main():
    pass


if __name__ == '__main__':
    main()
