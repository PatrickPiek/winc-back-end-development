# Betsy Webshop

### Scope of Assignment

* Functions and arguments
* SQL joins
* Database modelling
	* Model
	* Constraints
	* Run in "models.py"

### Model

#### User
- id as int
- name as varchar(256)
- address as varchar(512)
- zipcode as varchar(32)
- city as varchar(256)
- country as varchar(256)
- billing_name as varchar(256)
- billing_account as varchar(32)
- username as varchar(1024)
- email as varchar(1024)
- password as varchar(1024)

#### UserProduct
- id as int
- user_id as int
- product_id as int

#### Product
- name as varchar(256)
- description as varchar(1024)
- price_per_unit in cents as int
- qantity_in_stock as int

#### ProductTag
- id as int
- product_id as int
- tag_id as int

#### Tag
- id as int
- name as varchar(256)

#### Transaction
- id as int
- user_id as int
- timestamp as timestamp
- product_id as int
- quantity as int
- price_total in cents as int


### Querying
* Run in "main.py"
* Search in product name, case insensitive: `search(keyword)`
* Products for user: `products_of_user(user)`
* Products for tag: `products_with_tag(tag)`
* Add product to user: `add_product_to_user(user, product)`
* Remove product from user: `remove_product_from_user(user, product)`
* Update stock quantity of a product: `update_product_quantity(product, quantity)`
* Handle purchase between buyer and seller: `purchase_product(buyer, seller, product, quantity)`

	#### Bonus
* Search in description field as well
* Products should be indexed
* Search auto correct spelling mistakes
