from product import Product
class Cart():
    def __init__ (self,item):
        self.Products = []
        self.item = item

    def add_product(self, Product):
        self.Products.append(Product)

    def remove_product(self,Item):
        if Item in self.Products:
            self.Products.remove(Item)
            print(f"the {Item} has removed from the list")
        else:
            print(f"{Item} is not in your shop List:")

    def get_total(self):
        return sum(p.price for p in self.Products)


p1 = Product("python bokk", 150000, 12)
p2 = Product("mouse", 320000, 30)
p3 = Product("hedphone", 540000, 8)

products = [p1,p2,p3]

my_cart = Cart(products)
my_cart.add_product(p1)
my_cart.add_product(p2)
my_cart.add_product(p3)

print("your shop List")
for item in my_cart.item:
    print(item)

print(f"get total : {my_cart.get_total():} toman")

my_cart.remove_product(p2)
print(f"after deleting mouse the finall price will be: {my_cart.get_total():} tooman")