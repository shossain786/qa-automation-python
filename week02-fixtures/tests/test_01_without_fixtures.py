"""BEFORE: every test repeats the same setup, and nothing gets cleaned up."""
from app.users import UserStore


def test_add_user():
    store = UserStore()
    store.add("sara@example.com", "Sara")
    assert store.count() == 1


def test_get_user():
    store = UserStore()
    store.add("sara@example.com", "Sara")
    assert store.get("sara@example.com")["name"] == "Sara"


def test_deactivate_user():
    store = UserStore()
    store.add("sara@example.com", "Sara")
    store.deactivate("sara@example.com")
    assert store.get("sara@example.com")["active"] is False
