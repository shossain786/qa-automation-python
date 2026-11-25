"""A parametrized fixture: every test that uses it runs once per country."""
import pytest

from app.pricing import shipping_cost


@pytest.fixture(params=["US", "UK", "IN"])
def country(request):
    return request.param


def test_shipping_is_positive(country):
    assert shipping_cost(country, 1) > 0


def test_heavier_parcels_cost_more(country):
    assert shipping_cost(country, 5) > shipping_cost(country, 1)
