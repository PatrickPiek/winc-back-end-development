
from make_date import make_date
from format_date import format_date
import sys
import config
from Buy import Buy
from Sell import Sell
from Date import Date


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
            self.date()

        sys.exit(0)

    def buy(self):

        buy = Buy(self.args)
        buy.execute()

    def sell(self):

        sell = Sell(self.args)
        sell.execute()

    def date(self, value=0):

        date = Date(self.args)
        date.execute()

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
