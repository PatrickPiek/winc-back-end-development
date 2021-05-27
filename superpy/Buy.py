# python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01

import config
from Database import Database
from Today import Today
from functions import format_date


class Buy():

    def __init__(self, args):

        self.args = args
        self.database = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)

    def run(self):

        self.database.add(
            {
                'id':               self.database.rowcount + 1,
                'product_name':     self.args['product_name'],
                'buy_date':         Today().get_date(),
                'buy_price':        self.args['price'],
                'expiration_date':  format_date(self.args['expiration_date']),
            })

        return 'OK'


def main():
    pass


if __name__ == '__main__':
    main()
