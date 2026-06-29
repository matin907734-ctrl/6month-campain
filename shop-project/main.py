from product import Product
from cart import Cart

p1 = Product("1", "python book", 150000, 12)
p2 = Product("2", "mouse", 320000, 30)
p3 = Product("3", "headphone", 540000, 8)
p4 = Product("4", "phone", 1000, 10)

products = [p1, p2, p3, p4]

my_cart = Cart(products)

while True:

    print("\n=== our online shop ===")
    print("1. products")
    print("2. shopping")
    print("3. remove product from shop list")
    print("4. your shop list")
    print("5. exit")

    choice = int(input("enter the number you choice: "))

    if choice == 1:
        for p in products:
            print(p)

    elif choice == 2:
        print("\nProducts:")
        for p in products:
            print(p)
        shop_choice = int(input("enter the number of the product you want to add: "))

        if 1 <= shop_choice <= len(products):
            my_cart.add_product(products[shop_choice - 1])

    elif choice == 3:
        if len(my_cart.Products) == 0:
            print("your shop list is empty")
        else:
            print("\n===== YOUR SHOP LIST =====")

        for index, item in enumerate(my_cart.Products, start=1):
            product = item["product"]
            quantity = item["quantity"]
            print(f"{index}. {product.name} × {quantity}")

        remove_choice = int(input("enter the number of the product you want to delete: "))

        if 1 <= remove_choice <= len(my_cart.Products):
            my_cart.remove_product(
                my_cart.Products[remove_choice - 1]["product"]
            )
        else:
            print("invalid choice")
    elif choice == 4:
        print("\n===== YOUR SHOP LIST =====")
        if len(my_cart.Products) == 0:
            print("cart is empty")
        else:
            for item in my_cart.Products:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product.name} × {quantity} = {product.price * quantity:,} toman")
            print(f"\nTotal Price : {my_cart.get_total():,} toman" )

    elif choice == 5:
        print("Good Bye")
        break

    else:
        print("invalid choice")