"""A tiny shopping cart: the code we are going to test."""


class Cart:
    def __init__(self):
        self.items = {}

    def add(self, name, price, quantity=1):
        if price < 0:
            raise ValueError("price cannot be negative")
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove(self, name):
        del self.items[name]

    def count(self):
        return sum(item["quantity"] for item in self.items.values())

    def total(self):
        return round(sum(i["price"] * i["quantity"] for i in self.items.values()), 2)

    def apply_discount(self, percent):
        """Return the total after a percentage discount (0-100)."""
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return round(self.total() * (1 - percent / 100), 2)
