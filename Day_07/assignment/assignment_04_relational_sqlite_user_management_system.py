"""
### Assignment 4: Relational SQLite User Management System
#### Scenario
An internal employee directory stores user contact details in a SQLite database. The application must search for users, display existing details, or register new users.

#### Problem Description
Create a class `UserDatabaseManager` that connects to a SQLite database file:
1. **`__init__(self, db_path)`**: Connects to the database and creates a table `users` if it doesn't already exist:
   - Columns: `id INTEGER PRIMARY KEY AUTOINCREMENT`, `username TEXT UNIQUE NOT NULL`, `address TEXT`, `mobile TEXT`, `email TEXT`.
2. **`find_user(self, username)`**:
   - Queries the database for the given `username` using a parameterized SQL query.
   - If found, returns a dictionary: `{"id": row[0], "username": row[1], "address": row[2], "mobile": row[3], "email": row[4]}`.
   - If not found, returns `None`.
3. **`add_or_update_user(self, username, address, mobile, email)`**:
   - Checks if `username` exists.
   - If user exists, updates their `address`, `mobile`, and `email` values and returns `"UPDATED"`.
   - If user does not exist, inserts a new record and returns `"INSERTED"`.
4. **`list_all_users(self)`**: Returns a list of dictionaries for all registered users ordered alphabetically by `username`.

#### Example Walkthrough
```python
db = UserDatabaseManager("company.db")

# Insert new user
status1 = db.add_or_update_user("arham_k", "Pune, MH", "9876543210", "arham@cdac.in")
print(status1)  # Output: INSERTED

# Search user
user_info = db.find_user("arham_k")
print(user_info["email"])  # Output: arham@cdac.in

# Update existing user
status2 = db.add_or_update_user("arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
print(status2)  # Output: UPDATED
```
"""
import sqlite3


class UserDatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    address TEXT,
                    mobile TEXT,
                    email TEXT
                )
                """
            )

    def find_user(self, username: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, username, address, mobile, email FROM users WHERE username = ?",
            (username,),
        )
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "username": row[1],
                "address": row[2],
                "mobile": row[3],
                "email": row[4],
            }
        return None

    def add_or_update_user(self, username: str, address: str, mobile: str, email: str) -> str:
        existing = self.find_user(username)
        with self.conn:
            if existing:
                self.conn.execute(
                    """
                    UPDATE users
                    SET address = ?, mobile = ?, email = ?
                    WHERE username = ?
                    """,
                    (address, mobile, email, username),
                )
                return "UPDATED"
            else:
                self.conn.execute(
                    """
                    INSERT INTO users (username, address, mobile, email)
                    VALUES (?, ?, ?, ?)
                    """,
                    (username, address, mobile, email),
                )
                return "INSERTED"

    def list_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, username, address, mobile, email FROM users ORDER BY username ASC"
        )
        rows = cursor.fetchall()
        return [
            {
                "id": r[0],
                "username": r[1],
                "address": r[2],
                "mobile": r[3],
                "email": r[4],
            }
            for r in rows
        ]

    def close(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    pass
