class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

        product1 = Product("book ", 200000, 14)
        product2 = Product("keyboard", 350000, 45)
        product3 = Product("car", 4550000, 23)

        products = [product1, product2, product3]
        print("لیست محصولات فروشگاه:")
        for i in products:
            print(i)
    

    def __str__(self):
        return f"{self.name} - {self.price:,} price - stock: {self.stock}"
        
    