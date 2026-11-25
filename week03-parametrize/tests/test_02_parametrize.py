"""AFTER: one test, many inputs."""
import pytest

from app.pricing import apply_discount


@pytest.mark.parametrize("price, percent, expected", [
    (100, 10, 90.0),
    (100, 0, 100.0),
    (100, 100, 0.0),
    (59.99, 25, 44.99),
    (19.99, 15, 16.99),
])
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected


@pytest.mark.parametrize("percent", [-5, 101, 150])
def test_invalid_percent_is_rejected(percent):
    with pytest.raises(ValueError):
        apply_discount(100, percent)
