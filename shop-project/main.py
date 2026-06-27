from product import Product
from cart import  Cart

p1 = Product("python bokk", 150000, 12)
p2 = Product("mouse", 320000, 30)
p3 = Product("hedphone", 540000, 8)

products = [p1,p2,p3]
my_cart = Cart(products)
while True: 
    print("=== our online shop ===")
    print("1. products")
    print("2. shopping")
    print("3. your shop list")
    print("4. exit")

    choice = input("enter the number you choice: ")
    choice = int(choice)

    if choice == 1:
        for p in products:
            print(p)
        break
    if choice == 2:
        # print("comming sooooooooo sooon")
        for i in products:
            print(i)
        print(input("enter the number of the product you want to add to your shop list: "))
        if 1 <= choice <= len(products):
            my_cart.add_product(products[choice - 1])
            print(products)
        pass
    if choice == 3:
        for item in my_cart.item:
            print(item)
        else: 
            print("the number you entered isn't in the products list!!")
        break
    if choice == 4:
        print("goreto gom kon boro dige naya")
        break
    if choice > 4:
        print("halet khobe? chi keshidi?")