"""
### Assignment 6: Atomic Transaction processing with Log Rollback
#### Scenario
A bank updates user balances in a database dictionary based on transaction files. To ensure accounting consistency, if *any* single transaction in a batch contains an error (such as a negative transfer amount, an unrecognized account number, or an overdraft), the *entire batch* must fail, all accounts must be restored to their initial states, and a rollback action must be logged to a text file.

#### Problem Description
1. Define three custom exception classes inheriting from `Exception`:
   - `AccountNotFoundError` (raised when an account ID is missing from the registry).
   - `OverdraftError` (raised when a withdrawal amount exceeds the account balance).
   - `InvalidTransactionError` (raised when the transaction type is unrecognized or if transaction amounts are non-positive).
2. Write a function `process_transaction_batch(accounts, batch_list, log_path)`:
   - `accounts` is a dictionary where keys are account numbers (strings) and values are balances (floats), e.g., `{"ACC01": 500.0, "ACC02": 200.0}`.
   - `batch_list` is a list of dictionaries representing transactions, e.g.:
     ```python
     [
         {"acc": "ACC01", "type": "deposit", "amt": 150.0},
         {"acc": "ACC02", "type": "withdraw", "amt": 50.0}
     ]
     ```
   - `log_path` is a string referencing the path of the transaction log file.
   - **Atomicity Requirements**:
     - Create a deep copy of the `accounts` dictionary before starting any transaction modifications to act as a restore point (backup).
     - Iterate through `batch_list` and apply the changes to `accounts`:
       - If the transaction `"acc"` does not exist in `accounts`, raise `AccountNotFoundError` with message: `"Account '<acc>' not found."`
       - If transaction `"type"` is not `"deposit"` or `"withdraw"`, raise `InvalidTransactionError` with message: `"Invalid transaction type '<type>'."`
       - If transaction `"amt"` is less than or equal to `0`, raise `InvalidTransactionError` with message: `"Transaction amount must be positive."`
       - If transaction `"type"` is `"withdraw"` and the account balance is less than `"amt"`, raise `OverdraftError` with message: `"Insufficient funds. Account <acc> has balance <bal>, requested <amt>."`
     - **Exception Handling & Rollback**:
       - If any exception is raised during the processing of the list, catch the exception:
         - Restore the `accounts` dictionary to the exact state saved in your backup.
         - Open the file at `log_path` (create it if it doesn't exist, append to it if it does) and write the following entry:
           `[ROLLBACK] Batch aborted: <Exception Class Name> - <Exception Message>\n`
         - Re-raise the caught exception so that the calling program knows the transaction batch failed.
       - If all transactions in the batch are executed successfully:
         - Open the file at `log_path` and write:
           `[SUCCESS] Batch completed. <number_of_transactions> transaction(s) processed.\n`
         - Return the updated `accounts` dictionary.
     - **Constraint**: Ensure all file operations are safely cleaned up. Use context managers (`with open(...)`) or `try...finally` to write to the log file.

#### Example Walkthrough
```python
accounts = {"ACC01": 100.0, "ACC02": 50.0}
log_file = "transactions.log"

# Batch 1: Valid transactions
batch_1 = [
    {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
    {"acc": "ACC02", "type": "deposit", "amt": 20.0}
]
accounts = process_transaction_batch(accounts, batch_1, log_file)
# Result: accounts changes to {"ACC01": 70.0, "ACC02": 70.0}
# transactions.log writes: "[SUCCESS] Batch completed. 2 transaction(s) processed."

# Batch 2: Invalid transaction (triggers rollback)
batch_2 = [
    {"acc": "ACC01", "type": "deposit", "amt": 50.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 200.0} # Overdraft!
]
try:
    accounts = process_transaction_batch(accounts, batch_2, log_file)
except OverdraftError as e:
    print(f"Caught: {e}")

# Verify Rollback: ACC01 must remain 70.0, NOT updated to 120.0.
print(accounts) # Output: {"ACC01": 70.0, "ACC02": 70.0}
# transactions.log writes: "[ROLLBACK] Batch aborted: OverdraftError - Insufficient funds. Account ACC02 has balance 70.0, requested 200.0."
```
"""

import copy

class AccountNotFoundError(Exception):
    pass

class OverdraftError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass


def process_transaction_batch(accounts: dict, batch_list: list, log_path: str) -> dict:
    # 1. Create a deep copy backup of accounts for rollback safety
    backup_accounts = copy.deepcopy(accounts)
    
    try:
        for tx in batch_list:
            acc_id = tx.get("acc")
            tx_type = tx.get("type")
            amt = tx.get("amt", 0)
            
            # Validations
            if acc_id not in accounts:
                raise AccountNotFoundError(f"Account '{acc_id}' not found.")
            if tx_type not in ("deposit", "withdraw"):
                raise InvalidTransactionError(f"Invalid transaction type '{tx_type}'.")
            if amt <= 0:
                raise InvalidTransactionError(f"Transaction amount must be positive. Got: {amt}")
            if tx_type == "withdraw" and accounts[acc_id] < amt:
                raise OverdraftError(
                    f"Insufficient funds in {acc_id}. Balance: {accounts[acc_id]}, Requested: {amt}."
                )
                
            # Perform transaction on accounts
            if tx_type == "deposit":
                accounts[acc_id] += amt
            else:
                accounts[acc_id] -= amt
                
        # 2. If all succeed, log success
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[SUCCESS] Batch completed. {len(batch_list)} transaction(s) processed.\n")
            
        return accounts
        
    except Exception as e:
        # 3. Rollback state to original backup on failure
        accounts.clear()
        accounts.update(backup_accounts)
        
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[ROLLBACK] Batch aborted: {e.__class__.__name__} - {e}\n")
            
        raise


if __name__ == "__main__":
    bank_accounts = {"ACC01": 100.0, "ACC02": 50.0}
    log_file = "transactions.log"
    
    # Test 1: Successful Batch
    batch_1 = [
        {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
        {"acc": "ACC02", "type": "deposit", "amt": 20.0}
    ]
    bank_accounts = process_transaction_batch(bank_accounts, batch_1, log_file)
    print("Accounts after Batch 1:", bank_accounts)
    
    # Test 2: Failing Batch (Overdraft on ACC02)
    batch_2 = [
        {"acc": "ACC01", "type": "deposit", "amt": 50.0},
        {"acc": "ACC02", "type": "withdraw", "amt": 200.0}
    ]
    try:
        process_transaction_batch(bank_accounts, batch_2, log_file)
    except OverdraftError as e:
        print("Caught expected OverdraftError:", e)
        
    print("Accounts after rollback (should remain ACC01: 70.0, ACC02: 70.0):", bank_accounts)
