__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

from classes.Today import Today
from classes.Router import Router
from classes.Arguments import Arguments

import config

import sys
# comment when debugging
# sys.tracebacklimit = 0


def main():

    Today().get_date()

    arguments = Arguments()
    router = Router(arguments.vars)
    router.route()


if __name__ == '__main__':
    main()
