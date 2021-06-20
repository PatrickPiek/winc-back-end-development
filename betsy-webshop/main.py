__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import peewee
from peewee import JOIN


def main():
    # create_tables()
    # insert test data #
    # test queries #
    purchase_product(1, 1, 1)


def create_tables():
    with db:
        db.create_tables(
            [User,
             Product,
             Tag,
             Transaction,
             UserProduct,
             ProductTag
             ]
        )


def search(term):
    query = (Product
             .select()
             .where(
                 Product.name ** term | Product.description ** term)
             .order_by(Product.name)
             ).execute()


def list_user_products(user_id):

    query = (Product
             .select()
             .join(UserProduct, on=(Product.id == UserProduct.product))
             .join(User, on=(User.id == UserProduct.user))
             .where(User.id == user_id)
             ).execute()


def list_products_per_tag(tag_id):
    query = (Product
             .select()
             .join(ProductTag, on=(Product.id == ProductTag.product))
             .join(Tag, on=(Tag.id == ProductTag.tag))
             .where(Tag.id == tag_id)
             ).execute()


def add_product_to_catalog(user_id, product):

    query_add_product = Product.create(
        name=product['name'],
        description=product['description'],
        price_per_unit=product['price_per_unit'],
        quantity_in_stock=product['quantity_in_stock']
    )

    UserProduct.create(
        user=user_id,
        product=query_add_product.id
    )


def remove_product(product_id):
    query = (UserProduct
             .delete()
             .where(UserProduct.product == product_id)
             .limit(1)
             ).execute()


def update_stock(product_id, new_quantity):
    query = (Product
             .update({Product.quantity_in_stock: new_quantity})
             .where(Product.id == product_id)
             ).execute()


def purchase_product(product_id, buyer_id, quantity):
    seller = (User
              .select(User.id)
              .join(UserProduct, on=(User.id == UserProduct.user))
              .join(Product, on=(Product.id == UserProduct.product))
              .where(Product.id == product_id)
              ).execute()

    product = Product.select().where(Product.id == product_id).execute()

    price_total = product[0].price_per_unit * quantity
    new_quantity_in_stock = product[0].quantity_in_stock - quantity

    transaction = Transaction.create(
        buyer_id=buyer_id,
        seller_id=seller[0].id,
        quantity=quantity,
        price_total=price_total)

    update_stock(product_id, new_quantity_in_stock)

    query = (Transaction
             .select(Transaction.id == transaction.id)
             ).execute()


if __name__ == '__main__':
    main()
