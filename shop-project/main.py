from product import Product
from cart import Cart
from order import Order, save_order_to_json

p1 = Product("1", "python book", 150000, 12)
p2 = Product("2", "mouse", 320000, 30)
p3 = Product("3", "headphone", 540000, 8)
p4 = Product("4", "phone", 1000, 10)

products = [p1, p2, p3, p4]

my_cart = Cart(products)
order_history = []  # لیست همه‌ی سفارش‌های ثبت‌شده در طول اجرای برنامه

while True:

    print("\n=== our online shop ===")
    print("1. products")
    print("2. shopping")
    print("3. remove product from shop list")
    print("4. your shop list")
    print("5. checkout / place order")
    print("6. view previous orders")
    print("7. exit")

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
        if len(my_cart.Products) == 0:
            print("your shop list is empty, nothing to order")
        else:
            code_input = input("code takhfif dari?(age dari bezan): ").strip()
            discount_code = code_input if code_input else None

            new_order = Order(my_cart, discount_code=discount_code)
            save_order_to_json(new_order)
            order_history.append(new_order)  # نگه‌داشتن سفارش در تاریخچه

            my_cart.Products = []
            new_order.show_order()
            print("Your order has been placed and your cart is now empty.")

    elif choice == 6:
        if len(order_history) == 0:
            print("cart is empty")
        else:
            print(f"\nتعداد کل سفارش‌های ثبت‌شده: {len(order_history)}")
            for order in order_history:
                order.show_order()

    elif choice == 7:
        print("Good Bye")
        break

    else:
        print("invalid choice")
