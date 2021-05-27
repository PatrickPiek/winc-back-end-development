from Database import Database
from make_date import make_date
from format_date import format_date
from datetime import datetime
from datetime import timedelta
import db_config
from get_bought_id import get_bought_id


class Router():

    def __init__(self, args={}):

        if not isinstance(args, dict):
            raise TypeError('args is a dictionary of commandline arguments')

        self.args = args
        self.action = args['action']
        self.report = args['report']

    def route(self):

        if self.action == 'buy':
            self.buy()

        if self.action == 'sell':
            self.sell()

        if self.action == 'report':
            if self.report == 'inventory':
                self.inventory()

            if self.report == 'revenue':
                self.revenue()

            if self.report == 'profit':
                self.profit()

        if self.args['advance_time'] is not None:
            self.date(self.args['advance_time'])

    def buy(self):

        # python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01

        bought = Database(db_config.BOUGHT_FILE, db_config.BOUGHT_FIELDS)

        bought.add(
            {
                'id':               bought.rowcount + 1,
                'product_name':     self.args['product_name'],
                'buy_date':         make_date(),
                'buy_price':        self.args['price'],
                'expiration_date':  format_date(self.args['expiration_date']),
            })

        print('OK')

    def sell(self):

        # python super.py sell --product-name orange --price 2

        bought = Database(db_config.BOUGHT_FILE, db_config.BOUGHT_FIELDS)
        sold = Database(db_config.SOLD_FILE, db_config.SOLD_FIELDS)

        bought_id = get_bought_id(bought, sold, self.args)

        if bought_id == None:
            print('ERROR: Product not in stock')
            return

        sold.add(
            {
                'id':               sold.rowcount + 1,
                'bought_id':        bought_id,
                'sell_date':        make_date(),
                'sell_price':       self.args['price'],
            })

        print('OK')

    def date(self, value=0):

        # super.py --advance-time 2

        date = Database(db_config.DATE_FILE, db_config.DATE_FIELDS)

        today = datetime.now()

        if value > 0:
            today = today + timedelta(days=value)

        date.data = [{'date': format_date(today)}]
        date.save()

        print('OK')

    def inventory(self):
        pass

    def revenue(self):
        pass

    def profit(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
