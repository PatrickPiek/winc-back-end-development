# python super.py sell --product-name orange --price 2

import sys
import config
from Database import Database
from Today import Today


class Sell():

    def __init__(self, args):

        self.args = args
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
        bought_id = None

        for b in self.database_bought.data:
            if b['product_name'] == self.args['product_name']:
                if self.database_sold.rowcount == 0:
                    bought_id = b['id']
                    break
                else:
                    sold_state = False
                    for s in self.database_sold.data:
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
