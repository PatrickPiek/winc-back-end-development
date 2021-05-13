# Imports
import csv
from datetime import date
from class__Database import Database
from class__Ean13Code import Ean13Code
from parse_cli_arguments import parse_cli_arguments

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.

def main():

    # code = Ean13Code()
    # print(vars(code), code)

    # products = Database('products.csv', ['name', 'department', 'birthday'])
    # print(vars(products))
    # products.add(
    #     {'name': 'Leon Rijsdam 2', 'department': 'IT', 'birthday': '1977-07-23'})

    # print(vars(products))
    # products.save()

    args = parse_cli_arguments()
    print(vars(args))

    pass


if __name__ == '__main__':
    main()
