class Product:
    def __init__(self, number, name, price, stock):
        self.number = number
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.number}. {self.name} | Price: {self.price:,} toman | Stock: {self.stock}"