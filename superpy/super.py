__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

import csv

from CommandLineArgs import CommandLineArgs
from Route import Route


def main():

    args = CommandLineArgs()
    route = Route(args.vars)
    route.route()


if __name__ == '__main__':
    main()
