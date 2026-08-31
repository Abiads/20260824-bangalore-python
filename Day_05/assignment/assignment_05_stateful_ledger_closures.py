"""
Assignment 5: Stateful Ledger Scope Machine (LEGB Scopes & Closures)

Scenario:
Stateful balance ledger tracker without using classes (using closures, nested functions, nonlocal, global).

Problem Description:
1. Global variable `AUDIT_TRANSACTION_COUNT = 0`.
2. `create_bank_account(owner_name, initial_balance)`:
   - Nested functions: `deposit(amount)`, `withdraw(amount)`, `get_statement()`.
   - Uses `nonlocal` for `balance` and `history`.
   - Uses `global` for `AUDIT_TRANSACTION_COUNT`.
   - Returns `{"deposit": deposit, "withdraw": withdraw, "statement": get_statement}`.
"""

AUDIT_TRANSACTION_COUNT = 0

def create_bank_account(owner_name: str, initial_balance: float) -> dict:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    print("Initial Global Count:", AUDIT_TRANSACTION_COUNT)
    acc = create_bank_account("Arham", 1000.0)
    # Test deposit, withdraw, and statement

