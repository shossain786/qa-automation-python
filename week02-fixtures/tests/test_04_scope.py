"""Fixture scope: how often a fixture is created."""
import pytest

CALLS = {"function": 0, "module": 0}


@pytest.fixture
def per_test():
    CALLS["function"] += 1
    return CALLS["function"]


@pytest.fixture(scope="module")
def once_per_file():
    """Expensive setup (a browser, a server) you only want to do once per file."""
    CALLS["module"] += 1
    return CALLS["module"]


def test_first(per_test, once_per_file):
    assert per_test == 1
    assert once_per_file == 1


def test_second(per_test, once_per_file):
    assert per_test == 2        # function scope: created again
    assert once_per_file == 1   # module scope: reused
