
class Grocery:

    def __init__ (self, product, price, category):
        self.product = product
        self.price = price
        self.category = category

        #start of cart
        self.cart_products = []
        self.cart_price = []


    def add_to_cart (self):
        self.cart_products.append(self.product)
        self.cart_price.append(self.price)

    def display_cart (self):
        print ("Items: ",self.cart_products)


#list of items
i1 = Grocery("apple", 2, "fruits")
i2 = Grocery("cherries", 3, "fruits")
i3 = Grocery("milk", 4, "dairy")

Grocery.add_to_cart(i1)
Grocery.add_to_cart(i2)

Grocery.display_cart(i1)
Grocery.display_cart(i2)


#seperate lists into categories of products, price, category in order
#next step: change coding so the list doesn't restart everytime 