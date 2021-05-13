# Imports
import csv
from datetime import date
from classes import Ean13Code, Database
from functions import is_valid_date
from parse_cli_arguments import parse_cli_arguments

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.

def main():

    code = Ean13Code()
    print(vars(code), code)

    products = Database('products.csv', ['name', 'department', 'birthday'])
    print(vars(products))
    products.add(
        {'name': 'Leon Rijsdam 2', 'department': 'IT', 'birthday': '1977-07-23'})

    print(vars(products))
    products.write()

    args = parse_cli_arguments()
    print(vars(args))


if __name__ == '__main__':
    main()
