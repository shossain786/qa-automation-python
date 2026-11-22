"""Fixtures in conftest.py are shared by every test file in this folder."""
import pytest

from app.users import UserStore


@pytest.fixture
def store():
    s = UserStore()
    yield s          # the test runs here
    s.close()        # teardown: runs even if the test fails


@pytest.fixture
def store_with_users(store):
    store.add("sara@example.com", "Sara")
    store.add("ali@example.com", "Ali")
    return store
