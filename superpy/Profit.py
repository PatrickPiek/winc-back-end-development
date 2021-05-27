# super.py --advance-time 2

from datetime import datetime
from datetime import timedelta

import config
from Database import Database
from format_date import format_date


class Profit():

    def __init__(self, args):

        self.args = args
        self.database = Database(config.DATE_FILE, config.DATE_FIELDS)

    def report(self):

        print(self.args)

        today = datetime.now()

        days = self.args['advance_time']

        if days > 0:
            today = today + timedelta(days=days)

        self.database.data = [{'date': format_date(today)}]
        self.database.save()

        print('OK')


def main():
    pass


if __name__ == '__main__':
    main()
