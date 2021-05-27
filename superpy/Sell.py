# python super.py sell --product-name orange --price 2

from Database import Database
from make_date import make_date
import config
import sys


class Sell():

    def __init__(self, args):

        self.args = args
        self.bought = Database(
            config.BOUGHT_FILE, config.BOUGHT_FIELDS)
        self.sold = Database(
            config.SOLD_FILE, config.SOLD_FIELDS)

    def execute(self):

        bought_id = self.get_bought_id()

        if bought_id == None:
            print('ERROR: Product not in stock')
            sys.exit(1)

        self.sold.add(
            {
                'id':               self.sold.rowcount + 1,
                'bought_id':        bought_id,
                'sell_date':        make_date(),
                'sell_price':       self.args['price'],
            })

        print('OK')

    def get_bought_id(self):
        bought_id = None

        for b in self.bought.data:
            if b['product_name'] == self.args['product_name']:
                if self.sold.rowcount == 0:
                    bought_id = b['id']
                    break
                else:
                    sold_state = False
                    for s in self.sold.data:
                        if b['id'] == s['bought_id']:
                            sold_state = True
                    if sold_state == False:
                        bought_id = b['id']
                        break

        return bought_id


def main():
    pass


if __name__ == '__main__':
    main()
