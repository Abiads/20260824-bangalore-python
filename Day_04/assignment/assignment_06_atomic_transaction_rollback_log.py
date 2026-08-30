"""
Assignment 6: Atomic Transaction processing with Log Rollback

Scenario:
Process a batch of banking transactions atomically. If any error occurs, rollback all balances and log the error.

Problem Description:
1. Define custom exceptions:
   - `AccountNotFoundError`
   - `OverdraftError`
   - `InvalidTransactionError`
2. `process_transaction_batch(accounts, batch_list, log_path)`:
   - Deep copy `accounts` as backup.
   - For each tx: validate acc existence, type ("deposit"/"withdraw"), positive amt, and sufficient funds.
   - On error: rollback `accounts` to backup, log `[ROLLBACK] Batch aborted: <Class> - <Msg>\n`, and re-raise.
   - On success: log `[SUCCESS] Batch completed. <N> transaction(s) processed.\n` and return updated accounts.
"""

class AccountNotFoundError(Exception):
    pass

class OverdraftError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

def process_transaction_batch(accounts: dict, batch_list: list, log_path: str) -> dict:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    accounts = {"ACC01": 100.0, "ACC02": 50.0}
    log_file = "transactions.log"
    # Test batch processing and rollback

