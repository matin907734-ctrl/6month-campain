from flask import Flask, request, jsonify

from product import Product
from cart import Cart
from order import Order, save_order_to_json

app = Flask(__name__)

# لیست محصولات نمونه که از طریق API در دسترس قرار می‌گیرند
products = [
    Product("1", "python book", 150000, 12),
    Product("2", "mouse", 320000, 30),
    Product("3", "headphone", 540000, 8),
    Product("4", "phone", 1000, 10),
]


@app.route("/")
def home():
    """صفحه‌ی اصلی - فقط یک پیام خوش‌آمدگویی ساده."""
    return "به فروشگاه آنلاین ما خوش اومدی! 🛒"


@app.route("/about")
def about():
    """صفحه‌ی درباره‌ی فروشگاه (تمرین بونوس ۱)."""
    return "فروشگاه آنلاین پایتون - یک پروژه‌ی آموزشی برای یادگیری OOP، Flask و ساخت API."


@app.route("/products", methods=["GET"])
def get_products():
    """برگرداندن لیست تمام محصولات به فرمت JSON."""
    result = []
    for p in products:
        result.append({
            "number": p.number,
            "name": p.name,
            "price": p.price,
            "stock": p.stock,
        })
    return jsonify(result)


@app.route("/product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """برگرداندن اطلاعات یک محصول بر اساس شناسه‌اش (تمرین بونوس ۲)."""
    for p in products:
        if str(product_id) == p.number:
            return jsonify({
                "number": p.number,
                "name": p.name,
                "price": p.price,
                "stock": p.stock,
            })
    return jsonify({"error": "محصولی با این شناسه یافت نشد."}), 404


@app.route("/products", methods=["POST"])
def add_product():
    """افزودن یک محصول جدید فقط در حافظه، بدون ذخیره‌ی دائمی (تمرین بونوس ۳)."""
    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "فیلدهای 'name' و 'price' الزامی هستند."}), 400

    new_number = str(len(products) + 1)
    new_product = Product(new_number, data["name"], data["price"], data.get("stock", 0))
    products.append(new_product)

    return jsonify({
        "message": "محصول با موفقیت اضافه شد.",
        "number": new_number,
        "name": new_product.name,
    }), 201


@app.route("/order", methods=["POST"])
def create_order_api():
    """
    نقطه پایانی API برای ثبت سفارش.

    داده ورودی مورد انتظار (JSON در بدنه درخواست):
    {
        "cart_items": [
            {"product": {"number": "1", "name": "...", "price": 150000, "stock": 12}, "quantity": 2},
            ...
        ],
        "total_price": 300000
    }
    """
    if not request.json:
        return jsonify({"error": "درخواست باید حاوی JSON باشد."}), 400

    cart_items_data = request.json.get("cart_items")
    total_price_from_request = request.json.get("total_price")

    if not cart_items_data or total_price_from_request is None:
        return jsonify({"error": "داده‌های 'cart_items' و 'total_price' الزامی هستند."}), 400

    # ساخت یک سبد خرید موقت از داده‌های دریافتی
    temp_cart = Cart([])
    for item_data in cart_items_data:
        product_data = item_data.get("product")
        quantity = item_data.get("quantity")
        if product_data and quantity is not None:
            product = Product(
                number=product_data.get("number"),
                name=product_data.get("name"),
                price=product_data.get("price"),
                stock=product_data.get("stock", quantity),
            )
            temp_cart.Products.append({"product": product, "quantity": quantity})

    # ساخت سفارش از روی سبد موقت
    new_order = Order(temp_cart)

    # اعتبارسنجی اختیاری قیمت کل ارسالی توسط کلاینت
    if abs(new_order.total_price - float(total_price_from_request)) > 0.01:
        print(
            f"هشدار: مجموع قیمت دریافتی ({total_price_from_request:,}) "
            f"با مجموع محاسبه‌شده ({new_order.total_price:,}) مطابقت ندارد."
        )

    # ذخیره سفارش در فایل JSON
    save_order_to_json(new_order)

    return jsonify(
        {
            "message": "سفارش با موفقیت ثبت شد.",
            "order_id": new_order.order_id,
            "total_price": new_order.total_price,
        }
    ), 201


if __name__ == "__main__":
    # اجرا: python api.py
    # تست با curl:
    # curl -X POST -H "Content-Type: application/json" -d '{
    #     "cart_items": [
    #         {"product": {"number": "1", "name": "python book", "price": 150000, "stock": 12}, "quantity": 2}
    #     ],
    #     "total_price": 300000
    # }' http://127.0.0.1:5000/order
    app.run(debug=True)
