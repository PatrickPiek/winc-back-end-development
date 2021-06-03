import sys

from classes.Buy import Buy
from classes.Export import Export
from classes.Inventory import Inventory
from classes.Profit import Profit
from classes.Revenue import Revenue
from classes.Sell import Sell
from classes.Today import Today


class Router():

    def __init__(self, args):

        self.args = args
        self.action = args['action']
        self.report = args['report']

    def route(self):

        if self.action == 'buy':
            response = Buy(self.args).run()

        if self.action == 'sell':
            response = Sell(self.args).run()

        if self.action == 'report':
            if self.report == 'inventory':
                response = Inventory(self.args).run()

            if self.report == 'revenue':
                response = Revenue(self.args).run()

            if self.report == 'profit':
                response = Profit(self.args).run()

        if self.action == 'export':
            response = Export(self.args).run()

        if self.args['advance_time'] != None:
            response = Today(self.args).run()

        # return response
        if response != '':
            print(response)

        if response[:5] == 'ERROR':
            sys.exit(1)

        sys.exit(0)


def main():
    pass


if __name__ == '__main__':
    main()
