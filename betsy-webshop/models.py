from peewee import *
import datetime

import logging
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# db = peewee.SqliteDatabase(':memory:')
db = SqliteDatabase('db.sqlite3', pragmas={'foreign_keys': 1})


class BaseModule(Model):
    class Meta:
        database = db


class Tag(BaseModule):
    name = CharField()


class User(BaseModule):
    name = CharField()
    address = CharField()
    zipcode = CharField()
    city = CharField()
    state = CharField()
    country = CharField()
    billing_name = CharField()
    billing_account = CharField()
    username = CharField()
    password = CharField()


class Product(BaseModule):
    name = CharField()
    description = CharField()
    price_per_unit = IntegerField()
    quantity_in_stock = IntegerField()


class Transaction(BaseModule):
    buyer = ForeignKeyField(User)
    seller = ForeignKeyField(User)
    timestamp = TimestampField(default=datetime.datetime.now)
    product = ForeignKeyField(Product)
    quantity = IntegerField()
    price_total = IntegerField()


class UserProduct(BaseModule):
    user = ForeignKeyField(User, backref='products')
    product = ForeignKeyField(Product, backref='products')


class ProductTag(BaseModule):
    product = ForeignKeyField(Product, backref='tags')
    tag = ForeignKeyField(Tag, backref='tags')
