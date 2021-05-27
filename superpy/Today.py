# super.py --advance-time 2

from datetime import datetime
from datetime import timedelta

import config
from Database import Database
from format_date import format_date


class Today():

    def __init__(self, args):

        self.args = args
        self.database = Database(config.TODAY_FILE, config.TODAY_FIELDS)

        try:
            hasattr(self.database.data[0], 'today')
        except:
            self.args['advance_time'] = 0
            self.args['init'] = True
            self.set()

    def set(self):

        today = datetime.now()

        days = self.args['advance_time']

        if days > 0:
            today = today + timedelta(days=days)

        self.database.data = [{'today': format_date(today)}]
        self.database.save()

        if hasattr(self.args, 'init'):
            return

        print('OK')

    def get(self):

        return self.database.data[0]['today']


def main():
    pass


if __name__ == '__main__':
    main()
