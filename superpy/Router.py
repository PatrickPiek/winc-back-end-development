import sys

from Buy import Buy
from Sell import Sell
from Inventory import Inventory
from Revenue import Revenue
from Profit import Profit
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
                Inventory(self.args).report()

            if self.report == 'revenue':
                Revenue(self.args).report()

            if self.report == 'profit':
                Profit(self.args).report()

        if self.args['advance_time'] is not None:
            Today(self.args).set()

        sys.exit(0)


def main():
    pass


if __name__ == '__main__':
    main()
