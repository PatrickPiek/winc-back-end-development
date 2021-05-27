from FileDatabase import FileDatabase
from make_date import make_date
from format_date import format_date
from datetime import datetime
from datetime import timedelta
import config


class Route():

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
            return

    def buy(self):

        # python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01

        bought = FileDatabase(config.BOUGHT_FILENAME, config.BOUGHT_FIELDS)

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

        bought = FileDatabase(config.BOUGHT_FILENAME, config.BOUGHT_FIELDS)
        sold = FileDatabase(config.SOLD_FILENAME, config.SOLD_FIELDS)

        bought_id = None
        for b in bought.data:
            if b['product_name'] == self.args['product_name']:
                if sold.rowcount == 0:
                    bought_id = b['id']
                    break
                else:
                    sold_state = False
                    for s in sold.data:
                        if b['id'] == s['bought_id']:
                            sold_state = True
                    if sold_state == False:
                        bought_id = b['id']
                        break

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

        date = FileDatabase(config.DATE_FILENAME, config.DATE_FIELDS)

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
