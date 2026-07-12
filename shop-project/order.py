import uuid
import datetime
import json


# دیکشنری کدهای تخفیف: کلید = کد تخفیف، مقدار = درصد تخفیف
DISCOUNT_CODES = {
    "OFF10": 10,
    "OFF20": 20,
}

# سقف تخفیف: مبلغ تخفیف هیچ‌وقت از این عدد بیشتر نمی‌شود (تومان)
MAX_DISCOUNT_AMOUNT = 50000


class Order:
    """کلاسی برای نگهداری اطلاعات یک سفارش، ساخته‌شده از روی یک Cart."""

    def __init__(self, cart, discount_code=None):
        """
        Args:
            cart (Cart): شیء سبد خریدی که قرار است تبدیل به سفارش شود.
                         باید دارای cart.Products (لیستی از
                         {"product": Product, "quantity": int}) و
                         متد cart.get_total() باشد.
            discount_code (str | None): کد تخفیفی که کاربر وارد کرده.
                         اگر None باشد یا در DISCOUNT_CODES پیدا نشود،
                         هیچ تخفیفی اعمال نمی‌شود.
        """
        self.order_id = str(uuid.uuid4())          # شناسه یکتای سفارش
        self.timestamp = datetime.datetime.now()   # تاریخ و زمان ثبت سفارش
        self.items = self._items_from_cart(cart)
        self.total_price = cart.get_total()
        self.status = "Pending"                    # وضعیت اولیه سفارش

        # --- بخش تخفیف ---
        self.discount_code = discount_code
        self.discount_percent = 0

        if discount_code:
            if discount_code in DISCOUNT_CODES:
                self.discount_percent = DISCOUNT_CODES[discount_code]
            else:
                print("این کد تخفیف معتبر نیست.")  # کد نامعتبر => بدون تخفیف

    def _items_from_cart(self, cart):
        """تبدیل آیتم‌های cart.Products به فرمت قابل ذخیره در JSON."""
        items = []
        for item in cart.Products:
            product = item["product"]
            quantity = item["quantity"]
            items.append({
                "product": {
                    "number": product.number,
                    "name": product.name,
                    "price": product.price,
                    "stock": product.stock,
                },
                "quantity": quantity,
            })
        return items

    def get_discount_amount(self) -> float:
        """محاسبه‌ی مبلغ تخفیف (با احتساب سقف تخفیف)."""
        raw_amount = self.total_price * self.discount_percent / 100
        return min(raw_amount, MAX_DISCOUNT_AMOUNT)

    def get_final_price(self) -> float:
        """قیمت نهایی سفارش بعد از کسر تخفیف."""
        return self.total_price - self.get_discount_amount()

    def show_order(self):
        """نمایش خوانای یک سفارش شامل قیمت اصلی، تخفیف و قیمت نهایی."""
        print(f"\n----- سفارش {self.order_id[:8]} -----")
        print(f"تاریخ: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        for entry in self.items:
            product = entry["product"]
            quantity = entry["quantity"]
            print(f"  - {product['name']} × {quantity} = {product['price'] * quantity:,} toman")

        print(f"the real price: {self.total_price:,} toman")
        if self.discount_percent > 0:
            print(f"takhfif code: {self.discount_code} ({self.discount_percent}%)")
            print(f"takhfif price: {self.get_discount_amount():,.0f} toman")
        print(f"last price: {self.get_final_price():,.0f} toman")
        print("-------------------------------")

    def to_dict(self) -> dict:
        """تبدیل سفارش به دیکشنری قابل ذخیره در JSON."""
        return {
            "order_id": self.order_id,
            "timestamp": self.timestamp.isoformat(),  # تبدیل datetime به رشته
            "items": self.items,
            "total_price": self.total_price,
            "discount_code": self.discount_code,
            "discount_percent": self.discount_percent,
            "final_price": self.get_final_price(),
            "status": self.status,
        }


ORDERS_FILE = "orders.json"


def load_orders_from_json(filepath: str = ORDERS_FILE) -> list:
    """خواندن لیست سفارشات ذخیره‌شده از فایل JSON."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # اگر فایل هنوز وجود ندارد، لیست خالی برگردان
    except json.JSONDecodeError:
        print(f"خطا در خواندن فایل {filepath}: فایل JSON معتبر نیست یا خالی است.")
        return []


def save_order_to_json(order: Order, filepath: str = ORDERS_FILE):
    """ذخیره یک سفارش جدید در فایل JSON (اضافه به لیست سفارشات قبلی)."""
    all_orders = load_orders_from_json(filepath)
    all_orders.append(order.to_dict())
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(all_orders, f, indent=4, ensure_ascii=False)
    print(f"سفارش با شناسه {order.order_id} با موفقیت در {filepath} ثبت شد.")
