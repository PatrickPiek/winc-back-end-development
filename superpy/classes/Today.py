# python ./super.py --advance-time 2
# python ./super.py --advance-time 0

from datetime import datetime
from datetime import timedelta

import config

from classes.Database import Database

from functions.date import format_date


class Today():
    """Handles the SuperPy --advance-time
    Updates the internal date representation of today’ date for use
      with date calculations in reporting inventory, revenue or profit
    """

    def __init__(self, args={}):

        self.args = args
        self.today = Database(config.TODAY_FILE, config.TODAY_FIELDS)

        # set today if database is empty
        if len(self.today.data) == 0:
            self.args['advance_time'] = 0
            self.args['init'] = True
            self.run()

    def run(self):

        today = datetime.now()

        days = self.args['advance_time']

        if days > 0:
            today = today + timedelta(days=days)

        self.today.data = [{'today': format_date(today)}]
        self.today.save()

        # suppress CLI output when initializing the today database
        if hasattr(self.args, 'init'):
            return ''

        if days == 0:
            return f'OK. The SuperPy internal date for ‘today’ is reset to today’s date: {format_date(today)}'

        return f'OK. The SuperPy internal date for ‘today’ is now: {format_date(today)} (+{days})'

    def get_date(self):

        return self.today.data[0]['today']


def main():
    pass


if __name__ == '__main__':
    main()
