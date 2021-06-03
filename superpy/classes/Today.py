# super.py --advance-time 2

from datetime import datetime
from datetime import timedelta

import config

from classes.Database import Database

from functions.date import format_date


class Today():

    def __init__(self, args={}):

        self.args = args
        self.today = Database(config.TODAY_FILE, config.TODAY_FIELDS)

        try:
            hasattr(self.today.data[0], 'today')
        except:
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

        if hasattr(self.args, 'init'):
            return ''

        return 'OK'

    def get_date(self):

        return self.today.data[0]['today']


def main():
    pass


if __name__ == '__main__':
    main()
