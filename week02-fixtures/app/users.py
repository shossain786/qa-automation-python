"""A small user store backed by SQLite: the code we test with fixtures."""
import sqlite3


class UserStore:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            " id INTEGER PRIMARY KEY,"
            " email TEXT UNIQUE NOT NULL,"
            " name TEXT NOT NULL,"
            " active INTEGER NOT NULL DEFAULT 1)"
        )

    def add(self, email, name):
        if "@" not in email:
            raise ValueError("invalid email")
        cur = self.conn.execute(
            "INSERT INTO users (email, name) VALUES (?, ?)", (email.lower(), name)
        )
        self.conn.commit()
        return cur.lastrowid

    def get(self, email):
        row = self.conn.execute(
            "SELECT id, email, name, active FROM users WHERE email = ?", (email.lower(),)
        ).fetchone()
        if row is None:
            return None
        return {"id": row[0], "email": row[1], "name": row[2], "active": bool(row[3])}

    def deactivate(self, email):
        self.conn.execute("UPDATE users SET active = 0 WHERE email = ?", (email.lower(),))
        self.conn.commit()

    def count(self):
        return self.conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]

    def close(self):
        self.conn.close()
