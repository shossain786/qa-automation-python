"""Fixtures in conftest.py are shared by every test file in this folder."""
import pytest

from app.users import UserStore


@pytest.fixture
def store():
    """A fresh, empty database for each test. Closed after the test."""
    s = UserStore()
    yield s          # the test runs here
    s.close()        # teardown: runs even if the test fails


@pytest.fixture
def store_with_users(store):
    """Fixtures can use other fixtures: start from `store`, add test data."""
    store.add("sara@example.com", "Sara")
    store.add("ali@example.com", "Ali")
    return store
