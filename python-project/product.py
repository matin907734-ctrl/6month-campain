class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

        product1 = Product("کتاب پایتون", 150000, 12)
        product2 = Product("ماوس بی‌سیم", 320000, 30)
        product3 = Product("هدفون", 540000, 8)

        products = [product1, product2, product3]
        print("📦 لیست محصولات فروشگاه:")
        for p in products:
            print(p)
    

    def __str__(self):
        return f"{self.name} - {self.price:,} تومان - موجودی: {self.stock}"
        
    