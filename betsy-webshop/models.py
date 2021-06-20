from peewee import *
import datetime

# db = peewee.SqliteDatabase(':memory:')
db = SqliteDatabase('db.sqlite3', pragmas={'foreign_keys': 1})


class BaseModule(Model):
    class Meta:
        database = db


class Tag(BaseModule):
    id = AutoField(primary_key=True)
    name = CharField(unique=True, null=False)


class User(BaseModule):
    id = AutoField(primary_key=True)
    username = CharField(unique=True, null=False)
    password = CharField(null=False)
    name = CharField(null=False)
    address = CharField()
    zipcode = CharField()
    city = CharField()
    state = CharField()
    country = CharField()
    billing_name = CharField()
    billing_account = CharField()


class Product(BaseModule):
    id = AutoField(primary_key=True)
    name = CharField(null=False)
    description = CharField(null=False)
    price_per_unit = IntegerField(
        null=False,
        default=0,
        constraints=[
            Check('price_per_unit >= 0')
        ])
    quantity_in_stock = IntegerField(
        null=False,
        default=0,
        constraints=[
            Check('quantity_in_stock >= 0')
        ])


class Transaction(BaseModule):
    id = AutoField(primary_key=True)
    buyer = ForeignKeyField(User, null=False)
    seller = ForeignKeyField(User, null=False)
    timestamp = TimestampField(default=datetime.datetime.now)
    product = ForeignKeyField(Product, null=False)
    quantity = IntegerField(
        null=False,
        constraints=[
            Check('quantity >= 1')
        ])
    price_total = IntegerField(
        null=False,
        constraints=[
            Check('price_total >= 0')
        ])


class UserProduct(BaseModule):
    user = ForeignKeyField(User, backref='products')
    product = ForeignKeyField(Product, backref='products')


class ProductTag(BaseModule):
    product = ForeignKeyField(Product, backref='tags')
    tag = ForeignKeyField(Tag, backref='tags')
