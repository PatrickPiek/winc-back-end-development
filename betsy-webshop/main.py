__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import peewee


def main():

    # create database and tables
    # create_tables()

    # insert test data (raw sql) #
    # insert_test_data()

    # test queries #
    # print(search('imac'))
    # print(list_user_products(1))
    # print(list_products_per_tag(1))
    # print(add_product_to_catalog(1, {
    #     'name': 'Magic Mouse',
    #     'description': 'iMagic Mouse',
    #     'price_per_unit': 79000,
    #     'quantity_in_stock': 100
    # }))
    # print(remove_product(3))
    # print(update_stock(2, 999))
    # print(purchase_product(1, 1, 1))

    pass


def insert_test_data():
    queries = (
        'INSERT INTO "main"."user" ("name", "address", "zipcode", "city", "state", "country", "billing_name", "billing_account", "username", "password") VALUES("Leon", "Rustburg 50", "3253VK", "Ouddorp", "", "Netherlands", "L.A.H.  Rijsdam", "1234567890", "leon", "");',
        'INSERT INTO "main"."product" ("name", "description", "price_per_unit", "quantity_in_stock") VALUES("iMac", "iMac 27 inch", "2100", "1");',
        'INSERT INTO "main"."product" ("name", "description", "price_per_unit", "quantity_in_stock") VALUES("Keyboard", "iMac Extended Keyboard", "99000", "100");',
        'INSERT INTO "main"."tag" ("name") VALUES("Apple");',
        'INSERT INTO "main"."tag" ("name") VALUES("iMac");',
        'INSERT INTO "main"."tag" ("name") VALUES("27 inch");',
        'INSERT INTO "main"."producttag" ("product_id", "tag_id") VALUES("1", "1");',
        'INSERT INTO "main"."producttag" ("product_id", "tag_id") VALUES("1", "2");',
        'INSERT INTO "main"."producttag" ("product_id", "tag_id") VALUES("1", "3");',
        'INSERT INTO "main"."userproduct" ("user_id", "product_id") VALUES("1", "1");',
        'INSERT INTO "main"."userproduct" ("user_id", "product_id") VALUES("1", "2");'
    )
    for q in queries:
        print('test data query: ', q)
        db.execute_sql(q)


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
             .order_by(Product.name))
    print('search: ', query)
    result = query.execute()
    return result


def list_user_products(user_id):
    query = (Product
             .select()
             .join(UserProduct, on=(Product.id == UserProduct.product))
             .join(User, on=(User.id == UserProduct.user))
             .where(User.id == user_id)
             )
    print('list_user_products: ', query)
    result = query.execute()
    return result


def list_products_per_tag(tag_id):
    query = (Product
             .select()
             .join(ProductTag, on=(Product.id == ProductTag.product))
             .join(Tag, on=(Tag.id == ProductTag.tag))
             .where(Tag.id == tag_id)
             )
    print('list_products_per_tag: ', query)
    result = query.execute()
    return result


def add_product_to_catalog(user_id, product):
    query_add_product = Product(
        name=product['name'],
        description=product['description'],
        price_per_unit=product['price_per_unit'],
        quantity_in_stock=product['quantity_in_stock']
    )

    query_add_product.save()
    print('add_product_to_catalog: ', query_add_product)

    query_add_userproduct = UserProduct(
        user=user_id,
        product=query_add_product.id
    )

    query_add_userproduct.save()
    print('add_product_to_catalog: ', query_add_userproduct)

    return query_add_product.id


def remove_product(product_id):
    query = (UserProduct
             .delete()
             .where(UserProduct.product == product_id)
             )
    print('remove_product: ', query)
    result = query.execute()
    return result


def update_stock(product_id, new_quantity):
    query = (Product
             .update({Product.quantity_in_stock: new_quantity})
             .where(Product.id == product_id)
             )
    print('update_stock: ', query)
    result = query.execute()
    return result


def purchase_product(product_id, buyer_id, quantity):
    query = (User
             .select(User.id)
             .join(UserProduct, on=(User.id == UserProduct.user))
             .join(Product, on=(Product.id == UserProduct.product))
             .where(Product.id == product_id)
             )
    print('purchase_product, seller:', query)
    seller = query.execute()

    query = (Product
             .select()
             .where(Product.id == product_id)
             )
    print('purchase_product, product:', query)
    product = query.execute()

    price_total = product[0].price_per_unit * quantity

    query = Transaction(
        buyer_id=buyer_id,
        seller_id=seller[0].id,
        product_id=product[0].id,
        quantity=quantity,
        price_total=price_total
    )
    transaction = query.save()
    print('purchase_product, transaction:', query)

    new_quantity_in_stock = product[0].quantity_in_stock - quantity
    update_stock(product_id, new_quantity_in_stock)

    query = (Transaction
             .select()
             .where(Transaction.id == transaction)
             )
    print('transaction:', query)
    result = query.execute()
    return result


if __name__ == '__main__':
    main()
