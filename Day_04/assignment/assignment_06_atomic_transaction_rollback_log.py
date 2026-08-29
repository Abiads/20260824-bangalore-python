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

import copy

class AccountNotFoundError(Exception):
    pass

class OverdraftError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

def process_transaction_batch(accounts: dict, batch_list: list, log_path: str) -> dict:
    backup = copy.deepcopy(accounts)
    
    try:
        for tx in batch_list:
            acc = tx.get("acc")
            tx_type = tx.get("type")
            amt = tx.get("amt", 0)
            
            if acc not in accounts:
                raise AccountNotFoundError(f"Account '{acc}' not found.")
            if tx_type not in ("deposit", "withdraw"):
                raise InvalidTransactionError(f"Invalid transaction type '{tx_type}'.")
            if amt <= 0:
                raise InvalidTransactionError("Transaction amount must be positive.")
            if tx_type == "withdraw" and accounts[acc] < amt:
                raise OverdraftError(f"Insufficient funds. Account {acc} has balance {accounts[acc]}, requested {amt}.")
                
            if tx_type == "deposit":
                accounts[acc] += amt
            else:
                accounts[acc] -= amt
                
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[SUCCESS] Batch completed. {len(batch_list)} transaction(s) processed.\n")
            
        return accounts
        
    except Exception as e:
        accounts.clear()
        accounts.update(backup)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[ROLLBACK] Batch aborted: {e.__class__.__name__} - {e}\n")
        raise

if __name__ == "__main__":
    accounts = {"ACC01": 100.0, "ACC02": 50.0}
    log_file = "transactions.log"
    
    batch_1 = [
        {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
        {"acc": "ACC02", "type": "deposit", "amt": 20.0}
    ]
    accounts = process_transaction_batch(accounts, batch_1, log_file)
    print("After batch 1:", accounts)
    
    batch_2 = [
        {"acc": "ACC01", "type": "deposit", "amt": 50.0},
        {"acc": "ACC02", "type": "withdraw", "amt": 200.0}
    ]
    try:
        accounts = process_transaction_batch(accounts, batch_2, log_file)
    except OverdraftError as e:
        print("Caught expected OverdraftError:", e)
        
    print("Accounts after rollback (should remain ACC01: 70, ACC02: 70):", accounts)

