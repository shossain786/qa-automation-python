"""Readable case names with ids, and a known bug marked xfail."""
import pytest

from app.validators import is_valid_email


@pytest.mark.parametrize("email, valid", [
    ("sara@example.com", True),
    ("SARA@Example.com", True),
    ("sara.example.com", False),
    ("sara@@example.com", False),
    ("sara @example.com", False),
    pytest.param("sara@example", False,
                 marks=pytest.mark.xfail(reason="bug: no dot in domain")),
], ids=["normal", "uppercase", "no-at", "two-ats", "space", "no-dot"])
def test_is_valid_email(email, valid):
    assert is_valid_email(email) == valid
