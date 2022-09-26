# Class-Shoe

# ATTRIBUTES
#  *Brand
#  *wear/activity type
#  *price
#  *Stock status

# METHODS
#  *Sold out(changes the stock status to "False")
#  *Rebrand(updates the shoe brand name)
#  *On sale(decrease th price by a percentage)





class Shoe:
    def __init__(self):
        self.brand = "Adidas"
        self.type = "Tennis Shoe"
        self.price = 45.99
        self.in_stock = True

    def rebrand(self, new_brand): 
        
