"""pytest has built-in fixtures too. tmp_path = a new empty folder per test."""
import csv

from app.report import export_users


def test_export_users_to_csv(store_with_users, tmp_path):
    report = tmp_path / "users.csv"

    exported = export_users(store_with_users, report)

    assert exported == 2
    rows = list(csv.reader(report.open()))
    assert rows[0] == ["email", "name", "active"]
    assert rows[1][0] == "ali@example.com"
