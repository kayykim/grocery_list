
class Grocery_Trip:
    
    # MEMBER VARIABLES
    cart_size = 0
    store = ""
    cart_items = []
    price = 0

    # CONSTRUCTOR
    def __init__(self, cart_size, store cart_items, price):
        self.cart_size = cart_size
        self.store = store
        self.cart_items = cart_items
        self.price = price

    # SETTER - update from outside code
    def update_store(self, new_store):
        self.store = new_store

    # GETTER - specific functions
    def add_to_cart (self, items_to_add, item_price):
        self.cart_items = self.cart_items.append(items_to_add)
        self.price = self.price + item_price
        print ("Item added!")
    
    def display_items(self, cart_items, price):
        print ("Items:", self.cart_items)
        print ("Price (no tax):", self.price)
        print ("Price (tax):", (self.price * 0.13) + self.price)

# Depending on store --> fixed cart size, prices for categories
def ask_user():
    print ("1: Metro" + "\n" + "2: Walmart" + "\n" + "3: Superstore")
    loc_store = input("Which store are you going to? (1/2/3) ")
    
    # do an error check here
    if loc_store == 1:
        loc_cart_size = 10
        return loc_store, loc_cart_size
    
    elif loc_store == 2:
        loc_cart_size = 15
        return loc_store, loc_cart_size

    elif loc_store == 3:
        loc_cart_size = 20
        return loc_store, loc_cart_size

    else:
        print ("No store selected")


#MAIN PROGRAM
if __name__ == "__main__":
    glo_store, glo_cart_size = ask_user()

    # will be stored in the constructor
    to_do_trip = Grocery_Trip(glo_store, glo_cart_size, "", 0)

