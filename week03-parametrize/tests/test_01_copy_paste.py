"""BEFORE: the same test, copied for every input."""
from app.pricing import apply_discount


def test_discount_10_percent():
    assert apply_discount(100, 10) == 90.0


def test_discount_zero():
    assert apply_discount(100, 0) == 100.0


def test_discount_everything():
    assert apply_discount(100, 100) == 0.0


def test_discount_on_cents():
    assert apply_discount(59.99, 25) == 44.99
