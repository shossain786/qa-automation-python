"""Prices, discounts and shipping: the code we test with parametrize."""

SHIPPING_RATES = {"US": 5.00, "UK": 7.50, "IN": 2.00}


def apply_discount(price, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (100 - percent) / 100, 2)


def shipping_cost(country, weight_kg):
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    return round(SHIPPING_RATES[country] + weight_kg * 1.5, 2)
