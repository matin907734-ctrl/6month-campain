from product import Product

class Cart():
    def __init__(self, item):
        self.Products = []
        self.Shop_List = []
        self.item = item

    def add_product(self, Product):
        for item in self.Products:
            if item["product"] == Product:
                if item["quantity"] < Product.stock:
                    item["quantity"] += 1
                    print(f"{Product.name} quantity = {item['quantity']}")
                else:
                    print("Stock is not enough.")
                return

        self.Products.append({
            "product": Product,
            "quantity": 1
        })
        print(f"{Product.name} added to cart")

    def remove_product(self, Item):
        for item in self.Products:
            if item["product"] == Item:
            # اگر بیشتر از یکی وجود دارد فقط یکی کم کن
                if item["quantity"] > 1:
                    item["quantity"] -= 1
                    print(f"One {Item.name} removed.")
                    return
                # اگر فقط یکی مانده بود، کامل حذف شود
                elif item["quantity"] == 1:
                    self.Products.remove(item)
                    print(f"{Item.name} removed from cart.")
                    return
        print("Product not found.")

    def decrease_quantity(self, Item):
        for item in self.Products:
            if item["product"] == Item:
                item["quantity"] -= 1
                if item["quantity"] <= 0:
                    self.Products.remove(item)
                return

    def get_total(self):
        total = 0
        for item in self.Products:
            total += item["product"].price * item["quantity"]
        return total