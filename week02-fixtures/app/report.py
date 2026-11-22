"""Writes a CSV report of users: tested with the built-in tmp_path fixture."""
import csv


def export_users(store, path):
    rows = store.conn.execute("SELECT email, name, active FROM users ORDER BY email").fetchall()
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["email", "name", "active"])
        writer.writerows(rows)
    return len(rows)
