# Customer: represents a user who browses the menu and places orders.
# MenuItem: a single food/drink item with a name, price, category, and popularity rating.
# Order: a collection of menu items with quantities, a date, and a computed total cost.
# Payment: records how an order was paid, the amount, and whether processing succeeded.


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category  # e.g. "Burgers", "Drinks", "Desserts"
        self.popularity_rating = popularity_rating  # 0.0 – 5.0


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history = []  # list of Order objects


class Order:
    def __init__(self, datetime: str):
        self.datetime = datetime
        self.items = {}  # {MenuItem: quantity}

    def add_item(self, item, quantity: int = 1):
        self.items[item] = self.items.get(item, 0) + quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total(self) -> float:
        return sum(item.price * qty for item, qty in self.items.items())


class Payment:
    def __init__(self, order, method: str, amount: float, success: bool):
        self.order = order
        self.method = method   # e.g. "credit card", "cash"
        self.amount = amount
        self.success = success

    def get_receipt(self) -> str:
        lines = []
        for item, qty in self.order.items.items():
            lines.append(f"{item.name} x{qty}")
        lines.append(f"Total: ${self.order.total():.2f}")
        lines.append(f"Status: {'Approved' if self.success else 'Declined'}")
        return "\n".join(lines)
