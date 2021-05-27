import sys

from Buy import Buy
from Sell import Sell

from Today import Today


class Router():

    def __init__(self, args={}):

        if not isinstance(args, dict):
            raise TypeError('args is a dictionary of commandline arguments')

        self.args = args
        self.action = args['action']
        self.report = args['report']

    def route(self):

        if self.action == 'buy':

            Buy(self.args).execute()

        if self.action == 'sell':

            Sell(self.args).execute()

        if self.action == 'report':
            if self.report == 'inventory':
                self.inventory()

            if self.report == 'revenue':
                self.revenue()

            if self.report == 'profit':
                self.profit()

        if self.args['advance_time'] is not None:

            Today(self.args).set()

        sys.exit(0)

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
