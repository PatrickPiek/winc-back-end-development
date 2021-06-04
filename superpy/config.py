# Directories
BARCODES_DIR = 'barcodes'
DATABASES_DIR = 'databases'
REPORTS_DIR = 'reports'
EXPORTS_DIR = 'exports'

# Database names and fields
BOUGHT_FILE = 'bought.csv'
BOUGHT_FIELDS = [
    'id',               # number, auto increment from 1
    'product_name',     # string
    'buy_date',         # date in yyyy-mm-dd
    'buy_price',        # float
    'expiration_date',  # date in yyyy-mm-dd
    'ean13'             # generated ean13 barcode
]

PRODUCTS_FILE = 'products.csv'
PRODUCTS_FIELDS = [
    'product_name',     # string, short name of product
    'full_name',        # string, full name of product
    'ean13',            # string, 13 digits (12 + 1 checksum)
]

SOLD_FILE = 'sold.csv'
SOLD_FIELDS = [
    'id',               # number, auto increment from 1
    'bought_id',        # string
    'sell_date',        # date in yyyy-mm-dd
    'sell_price',       # float
]

TODAY_FILE = 'today.csv'
TODAY_FIELDS = [
    'today',            # date in yyyy-mm-dd
]

# Date fields to process with datetime
DATE_FIELDS = [
    'buy_date',
    'sell_date',
    'expiration_date',
]

# Date formats
DATE_FORMAT = '%Y-%m-%d'
YEAR_MONTH_FORMAT = '%Y-%m'
YEAR_FORMAT = '%Y'

REPORT_DATE_FORMAT = '%B %d %Y'
REPORT_YEAR_MONTH_FORMAT = '%B %Y'
REPORT_YEAR_FORMAT = YEAR_FORMAT

DATE_FORMAT_FILENAME = '%Y%m%d_%H%M%S'

# Report fieldnames
INVENTORY_REPORT_FIELDS = [
    'Product Name',
    'Count',
    'Buy Price',
    'Sum Price',
    'Expiration Date',
    'Expired',
    'EAN13'
]

# Unique prefix for barcodes generated for this supermarket
STORE_BARCODE_PREFIX = '123456'
