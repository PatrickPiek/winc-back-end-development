# Database field definitions

BOUGHT_FILE = 'db_bought.csv'
BOUGHT_FIELDS = [
    'id',               # number, auto increment from 1
    'product_name',     # string
    'buy_date',         # date in yyyy-mm-dd
    'buy_price',        # float
    'expiration_date',  # date in yyyy-mm-dd
]
BOUGHT_REPORT_FIELDS = [
    'product_name',
    'count',
    'buy_price',
    'expiration_date',
]
BOUGHT_REPORT_COLUMN_NAMES = [
    'Product Name',
    'Count',
    'Buy Price',
    'Expiration Date',
]

SOLD_FILE = 'db_sold.csv'
SOLD_FIELDS = [
    'id',               # number, auto increment from 1
    'bought_id',        # string
    'sell_date',        # date in yyyy-mm-dd
    'sell_price',       # float
]

TODAY_FILE = 'db_today.csv'
TODAY_FIELDS = [
    'today',            # date in yyyy-mm-dd
]

DATE_FIELDS = [
    'buy_date',
    'sell_date',
    'expiration_date',
]

DATE_FORMAT = '%Y-%m-%d'
