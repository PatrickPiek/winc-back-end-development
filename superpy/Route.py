from FileDatabase import FileDatabase
from make_date import make_date
from format_date import format_date


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
            self.timewarp(self.args['advance_time'])
            return

    def buy(self):

        # super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01

        bought = FileDatabase(
            'bought.csv', [
                'id',               # number, auto increment from 1
                'product_name',     # string
                'buy_date',         # date in yyyy-mm-dd
                'buy_price',        # float
                'expiration_date',  # date in yyyy-mm-dd
            ])

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

        # super.py sell --product-name orange --price 2

        bought = FileDatabase(
            'bought.csv', [
                'id',               # number, auto increment from 1
                'product_name',     # string
                'buy_date',         # date in yyyy-mm-dd
                'buy_price',        # float
                'expiration_date',  # date in yyyy-mm-dd
            ])

        sold = FileDatabase(
            'sold.csv', [
                'id',               # number, auto increment from 1
                'bought_id',        # string
                'sell_date',        # date in yyyy-mm-dd
                'sell_price',       # float
            ])

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

    def inventory(self):
        pass

    def revenue(self):
        pass

    def profit(self):
        pass

    def timewarp(self, value=0):
        print(value)
        pass


def main():
    pass


if __name__ == '__main__':
    main()
