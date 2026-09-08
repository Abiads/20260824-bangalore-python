"""
### Assignment 5: Transactional Banking Ledger with SQLite & ACID Rollback Management
#### Scenario
A financial transaction engine executes fund transfers between accounts in a SQLite database. The engine must support ACID guarantees: if any part of a transfer fails (e.g. insufficient funds, invalid account), the entire transaction must roll back cleanly.

#### Problem Description
Create a custom exception `TransactionError(Exception)`.
Create a class `BankingLedger` that manages an `accounts` table (`account_id TEXT PRIMARY KEY`, `holder_name TEXT`, `balance REAL`) and an `audit_log` table (`tx_id INTEGER PRIMARY KEY AUTOINCREMENT`, `from_acc TEXT`, `to_acc TEXT`, `amount REAL`, `timestamp TEXT`):
1. **`create_account(account_id, holder_name, initial_deposit)`**: Adds a new account. Raises `ValueError` if `initial_deposit < 0`.
2. **`transfer_funds(from_acc, to_acc, amount)`**:
   - Executes an atomic transfer of `amount` from `from_acc` to `to_acc`.
   - Deducts `amount` from `from_acc` and adds `amount` to `to_acc`.
   - Records an entry in the `audit_log` table.
   - **Validation & Rollback Rules**:
     - `amount` must be strictly positive (> 0).
     - Both accounts must exist in the database.
     - `from_acc` must have a sufficient balance (>= amount).
     - If any condition fails, raise `TransactionError` and execute `conn.rollback()`.
     - If all checks pass, execute `conn.commit()`.
3. **`get_balance(account_id)`**: Returns the current balance for the given account.

#### Example Walkthrough
```python
bank = BankingLedger("bank.db")
bank.create_account("ACC101", "Arham", 5000.0)
bank.create_account("ACC102", "Lisa", 2000.0)

# Valid transfer
bank.transfer_funds("ACC101", "ACC102", 1500.0)
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0

# Invalid transfer (insufficient funds) -> rolled back
try:
    bank.transfer_funds("ACC101", "ACC102", 10000.0)
except TransactionError as e:
    print(e)  # Output: Insufficient funds in account ACC101

# Balances remain untouched
print(bank.get_balance("ACC101"))  # Output: 3500.0
print(bank.get_balance("ACC102"))  # Output: 3500.0
```
"""
import sqlite3
from datetime import datetime


class TransactionError(Exception):
    pass


class BankingLedger:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._init_tables()

    def _init_tables(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS accounts (
                    account_id TEXT PRIMARY KEY,
                    holder_name TEXT NOT NULL,
                    balance REAL NOT NULL
                )
                """
            )
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS audit_log (
                    tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    from_acc TEXT NOT NULL,
                    to_acc TEXT NOT NULL,
                    amount REAL NOT NULL,
                    timestamp TEXT NOT NULL
                )
                """
            )

    def create_account(self, account_id: str, holder_name: str, initial_deposit: float):
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be non-negative.")
        with self.conn:
            self.conn.execute(
                "INSERT INTO accounts (account_id, holder_name, balance) VALUES (?, ?, ?)",
                (account_id, holder_name, float(initial_deposit)),
            )

    def get_balance(self, account_id: str) -> float:
        cursor = self.conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        row = cursor.fetchone()
        if row is None:
            raise ValueError(f"Account {account_id} not found.")
        return float(row[0])

    def transfer_funds(self, from_acc: str, to_acc: str, amount: float):
        if amount <= 0:
            raise TransactionError("Transfer amount must be strictly positive.")

        cursor = self.conn.cursor()
        try:
            # Check from_acc
            cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_acc,))
            from_row = cursor.fetchone()
            if from_row is None:
                raise TransactionError(f"Account {from_acc} does not exist.")

            from_balance = float(from_row[0])
            if from_balance < amount:
                raise TransactionError(f"Insufficient funds in account {from_acc}")

            # Check to_acc
            cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (to_acc,))
            to_row = cursor.fetchone()
            if to_row is None:
                raise TransactionError(f"Account {to_acc} does not exist.")

            # Perform debit and credit
            cursor.execute(
                "UPDATE accounts SET balance = balance - ? WHERE account_id = ?",
                (float(amount), from_acc),
            )
            cursor.execute(
                "UPDATE accounts SET balance = balance + ? WHERE account_id = ?",
                (float(amount), to_acc),
            )

            # Record audit log
            now_iso = datetime.now().isoformat()
            cursor.execute(
                "INSERT INTO audit_log (from_acc, to_acc, amount, timestamp) VALUES (?, ?, ?, ?)",
                (from_acc, to_acc, float(amount), now_iso),
            )

            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    def close(self):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    pass
