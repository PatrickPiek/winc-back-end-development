# SuperPy

A command-line tool that supermarkets use to keep track of their inventory.

## Used Modules

-   [x] csv
-   [x] argparse
-   [x] datetime
-   [x] calendar (https://docs.python.org/3/library/calendar.html)
-   [x] os.path (https://docs.python.org/3/library/os.path.html)
-   [x] python-barcode (https://pypi.org/project/python-barcode/)
    -   `pip install python-barcode`
    -   `pip install "python-barcode[images]"`
-   [x] rich (https://rich.readthedocs.io/en/stable/introduction.html) [only for clean debug output]
    -   `pip install rich`
-   [x] sys (https://docs.python.org/3/library/sys.html)
-   [x] tabulate (https://pypi.org/project/tabulate/)
    -   `pip install tabulate`
-   [x] unittest (https://docs.python.org/3/library/unittest.html)
-   [x] xlsxwriter (https://xlsxwriter.readthedocs.io/)
    -   `pip install XlsxWriter`

## Commandline Options

-   `python super.py -h` or `python super.py --help`

```
usage: super.py [-h] [--database] [--product-name] [--price] [--expiration-date] [--advance-time] [--now] [--today] [--yesterday] [--date] [--export-format]
                [action] [report]

SuperPy

positional arguments:
  action              the action to perform: buy, sell, report or export
  report              the report action to perform: inventory, revenue or profit

optional arguments:
  -h, --help          show this help message and exit
  --database          the database to export: bought, sold or products
  --product-name      the short name of the product to buy or sell (e.g. ‘orange’)
  --price             the price of the product to buy or sell (e.g. ‘2.95’)
  --expiration-date   the expiration date of the product to buy or sell; format as ‘yyyy-mm-dd’
  --advance-time      advance the time by n days; where n >= 0; 0 will reset to today’s date
  --now               create report based on current data; relative to ‘today’ setting
  --today             create report on today’s data; relative to ‘today’ setting
  --yesterday         create report based on yesterday’s data; relative to ‘today’ setting
  --date              report argument; format as ‘yyyy’, ‘yyyy-mm’ or ‘yyyy-mm-dd’
  --export-format     export inventory: csv, json or xlsx
```

### `--advance-time`

The internal conception of what day it is. Use `--advance-time 0` to reset the internal day to today’s date. This option does not require other arguments.

-   `python ./super.py --advance-time 2`
-   `python ./super.py --advance-time 0`

### `buy`

Record buys of products with `buy` and provide `product-name` (short name, lowercase, without spaces), `price` and `expiration-date`.

-   `python ./super.py buy --product-name orange --price 0.8 --expiration-date 2020-05-01`
-   `python ./super.py buy --product-name peach --price 2.25 --expiration-date 2020-08-01`

### `sell`

Record sells of products with `sell` and provide `product-name` (short name, lowercase, without spaces) and `price`.

-   `python ./super.py sell --product-name orange --price 2`
-   `python ./super.py sell --product-name peach --price 3.95`

### `report` `inventory`

Report inventory with `report` and `inventory` and provide an optional time argument.
Use `export-format <type>` to store the report in the format specified.

-   `python ./super.py report inventory`
-   `python ./super.py report inventory --now`
-   `python ./super.py report inventory --today`
-   `python ./super.py report inventory --today --export-format csv`
-   `python ./super.py report inventory --today --export-format xlsx`
-   `python ./super.py report inventory --today --export-format json`

### `report` `revenue`

Report revenue with `report` and `revenue` and provide a required time argument.

-   `python ./super.py report revenue --now`
-   `python ./super.py report revenue --today`
-   `python ./super.py report revenue --yesterday`
-   `python ./super.py report revenue --date 2021`
-   `python ./super.py report revenue --date 2021-06`
-   `python ./super.py report revenue --date 2021-06-02`

### `report` `profit`

Report revenue with `report` and `profit` and provide a required time argument.

-   `python ./super.py report profit --now`
-   `python ./super.py report profit --today`
-   `python ./super.py report profit --yesterday`
-   `python ./super.py report profit --date 2021`
-   `python ./super.py report profit --date 2021-06`
-   `python ./super.py report profit --date 2021-06-02`

### `export`

Export raw data with `export`, use `database` to set the database to export and provide an optional time argument.
Use `export-format <type>` to store the report in the format specified.

-   `python ./super.py export --database bought --today --export-format csv`
-   `python ./super.py export --database bought --yesterday --export-format csv`
-   `python ./super.py export --database bought --date 2021-06 --export-format csv`
-   `python ./super.py export --database sold --date 2021-06 --export-format xlsx`
-   `python ./super.py export --database products --date 2021 --export-format json`
