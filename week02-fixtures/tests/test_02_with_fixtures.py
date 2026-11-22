"""AFTER: the setup lives in one fixture (see conftest.py)."""
import pytest


def test_add_user(store):
    store.add("sara@example.com", "Sara")
    assert store.count() == 1


def test_each_test_gets_a_fresh_store(store):
    # The user added in the test above is gone: the fixture runs again.
    assert store.count() == 0


def test_get_user(store_with_users):
    assert store_with_users.get("ali@example.com")["name"] == "Ali"


def test_email_is_case_insensitive(store_with_users):
    assert store_with_users.get("SARA@Example.com") is not None


def test_deactivate_user(store_with_users):
    store_with_users.deactivate("sara@example.com")
    assert store_with_users.get("sara@example.com")["active"] is False


def test_invalid_email_is_rejected(store):
    with pytest.raises(ValueError):
        store.add("not-an-email", "Nobody")
