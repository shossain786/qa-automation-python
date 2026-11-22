import pytest

from cart import Cart


# Step 1: the smallest possible test
def test_new_cart_is_empty():
    cart = Cart()
    assert cart.count() == 0


# Step 2: Arrange, Act, Assert
def test_add_one_item():
    cart = Cart()                     # Arrange
    cart.add("apple", 0.50)           # Act
    assert cart.count() == 1          # Assert


def test_total_with_quantities():
    cart = Cart()
    cart.add("apple", 0.50, quantity=4)
    cart.add("bread", 2.25)
    assert cart.total() == 4.25


def test_adding_same_item_twice_increases_quantity():
    cart = Cart()
    cart.add("apple", 0.50)
    cart.add("apple", 0.50)
    assert cart.items["apple"]["quantity"] == 2


def test_discount():
    cart = Cart()
    cart.add("headphones", 80.00)
    assert cart.apply_discount(25) == 60.00


# Step 3: test that bad input is rejected
def test_negative_price_is_rejected():
    cart = Cart()
    with pytest.raises(ValueError, match="negative"):
        cart.add("apple", -1)


def test_discount_over_100_is_rejected():
    cart = Cart()
    cart.add("apple", 1.00)
    with pytest.raises(ValueError):
        cart.apply_discount(150)


# Step 4: a failing test, on purpose, to read pytest's output
@pytest.mark.demo_fail
def test_total_wrong_on_purpose():
    cart = Cart()
    cart.add("apple", 0.50, quantity=4)
    assert cart.total() == 3.00, "4 apples at 0.50 should cost 2.00, not 3.00"
