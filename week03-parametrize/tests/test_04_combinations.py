"""Stack parametrize to test every combination."""
import pytest

from app.pricing import apply_discount


@pytest.mark.parametrize("price", [0.99, 19.99, 100, 2500])
@pytest.mark.parametrize("percent", [0, 15, 50, 100])
def test_discount_in_range(price, percent):
    result = apply_discount(price, percent)
    assert 0 <= result <= price
