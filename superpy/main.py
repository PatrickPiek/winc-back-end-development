
import csv
from datetime import date

from FileDatabase import FileDatabase
from Barcode import Barcode
from CommandLineArgs import CommandLineArgs
from Route import Route

__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


def main():

    # code = Barcode()
    # print(vars(code), code)

    # products = FileDatabase('products.csv', ['name', 'department', 'birthday'])
    # print(vars(products))
    # products.add(
    #     {'name': 'Leon Rijsdam 2', 'department': 'IT', 'birthday': '1977-07-23'})
    # products.append(
    #     {'name': 'Leon Rijsdam 4', 'department': 'IT', 'birthday': '1977-07-23'})
    # print(vars(products))
    # products.save()

    # args = CommandLineArgs()
    # route = Route(args.vars)
    # route.route()


if __name__ == '__main__':
    main()
