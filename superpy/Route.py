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
        pass

    def sell(self):
        pass

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
