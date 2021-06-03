## SuperPy Requirements

### Well-structured and documented code:

-   [x] Clear and effective variable and function names
-   [x] Use of comments where the code does not speak for itself
-   [x] Clear and effective separation of code into separate functions and possibly files

### Use of modules:

-   [x] csv
-   [x] argparse
-   [x] datetime

### Additionally used modules:

-   [x] calendar (https://docs.python.org/3/library/calendar.html)
-   [x] os.path (https://docs.python.org/3/library/os.path.html)
-   [x] python-barcode (https://pypi.org/project/python-barcode/)
        `pip install python-barcode`
        `pip install "python-barcode[images]"`
-   [x] rich (https://rich.readthedocs.io/en/stable/introduction.html) [only for clean debug output]
        `pip install rich`
-   [x] sys (https://docs.python.org/3/library/sys.html)
-   [x] tabulate (https://pypi.org/project/tabulate/)
        `pip install tabulate`
-   [x] unittest (https://docs.python.org/3/library/unittest.html)
-   [x] xlsxwriter (https://xlsxwriter.readthedocs.io/)
        `pip install XlsxWriter`

### Requirements

-   [x] Use of external text files (CSV) to read and write data
-   [x] A well-structured and user friendly command-line interface
-   [x] Clear descriptions of each argument in the --help section
-   [x] A text file containing a usage guide aimed with peers as the target audience
-   [x] The usage guide should include plenty of examples

### The application must support:

-   [x] Setting and advancing the date that the application perceives as ‘today’
-   [x] Recording the buying and selling of products on certain dates
-   [x] Reporting revenue and profit over specified time periods
-   [x] Exporting selections of data to CSV files
-   [x] Two other additional non-trivial features of your choice
-   [x] A short, 300-word report that highlights three technically notable elements

### Additional non-trivial features

-   [x] 1: Export report as a JSON or Excel file
-   [x] 2: Generate a unique EAN-13 barcode for a new product and store products in a separate database
-   [x] 3: Store new barcodes in a barcodes directory
