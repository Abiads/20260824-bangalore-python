"""
### Assignment 5: SQLite Contact Synchronizer with JSON Transaction Log
#### Scenario
You are writing a database synchronization daemon that reconciles client contact profiles with a central server. The daemon receives contact changes as a JSON formatted transaction log. The changes must be processed atomically: if *any* single transaction in the batch fails, the entire batch must roll back, and a rollback log must be written.

#### Problem Description
Create a database named `contacts.db` with a table named `contacts` (Schema: `name TEXT PRIMARY KEY, phone TEXT, email TEXT`).
Write a function `sync_contacts_batch(db_name, json_patch_str, log_path)`:
1. Parse `json_patch_str` as a JSON list. If parsing fails, raise a `ValueError` with the message `"Invalid patch JSON"`.
2. Connect to the database `db_name` and start a transaction.
3. Process each dictionary entry in the parsed JSON patch list. An entry has an `"action"` key which can be `"insert"`, `"update"`, or `"delete"`.
   - **`"insert"`**:
     - Insert a new contact using `name`, `phone`, and `email`.
     - If the contact `name` already exists in the database (violating the PRIMARY KEY constraint and raising `sqlite3.IntegrityError`), catch it and instead update the existing contact's phone and email (UPSERT behavior).
   - **`"update"`**:
     - Update the `phone` and `email` for the matching `name`.
     - If the `name` does not exist in the database, raise a custom exception `ContactNotFoundError` with the message `"Contact <name> not found for update"`.
   - **`"delete"`**:
     - Delete the record matching `name`.
     - If the `name` does not exist in the database, raise a custom exception `ContactNotFoundError` with the message `"Contact <name> not found for deletion"`.
4. **Atomicity & Logging**:
   - Wrap the loop in a `try` block. If any exception occurs (including `ContactNotFoundError` or standard SQLite errors):
     - Roll back the database transaction using `conn.rollback()` to prevent partial changes.
     - Open the file at `log_path` and append a log entry:
       `[SYNC FAILED] Batch aborted: <Exception Message>\n`
     - Re-raise the exception to notify the caller.
   - If all operations execute successfully:
     - Commit the transaction using `conn.commit()`.
     - Open the file at `log_path` and append a log entry:
       `[SYNC SUCCESS] Batch processed. <N> changes synchronized.\n` (where `N` is the number of items in the JSON patch).
     - Return `True`.

#### Example Walkthrough
```python
# Database has initial entries: [("Alice", "111", "alice@abc.com"), ("Bob", "222", "bob@abc.com")]

# Valid Patch (UPSERT and Update)
valid_patch = """[
    {"action": "insert", "name": "Alice", "phone": "123", "email": "alice@new.com"},
    {"action": "update", "name": "Bob", "phone": "999", "email": "bob@new.com"}
]"""
sync_contacts_batch("contacts.db", valid_patch, "sync.log")
# database successfully commits changes. sync.log writes "[SYNC SUCCESS]..."

# Invalid Patch (Raises ContactNotFoundError)
invalid_patch = """[
    {"action": "insert", "name": "Charlie", "phone": "444", "email": "charlie@abc.com"},
    {"action": "delete", "name": "David"}
]"""
# David does not exist in the database!
try:
    sync_contacts_batch("contacts.db", invalid_patch, "sync.log")
except ContactNotFoundError as e:
    print(e) # Output: Contact David not found for deletion

# Verify Database Atomicity: Charlie must NOT be inserted into contacts database.
# sync.log writes "[SYNC FAILED]..."
```
"""

[
    {"action": "insert", "name": "Alice", "phone": "123", "email": "alice@new.com"},
    {"action": "update", "name": "Bob", "phone": "999", "email": "bob@new.com"}
]"""
sync_contacts_batch("contacts.db", valid_patch, "sync.log")
# database successfully commits changes. sync.log writes "[SYNC SUCCESS]..."

# Invalid Patch (Raises ContactNotFoundError)
invalid_patch = """[
    {"action": "insert", "name": "Charlie", "phone": "444", "email": "charlie@abc.com"},
    {"action": "delete", "name": "David"}
]"""
# David does not exist in the database!
try:
    sync_contacts_batch("contacts.db", invalid_patch, "sync.log")
except ContactNotFoundError as e:
    print(e) # Output: Contact David not found for deletion

# Verify Database Atomicity: Charlie must NOT be inserted into contacts database.
# sync.log writes "[SYNC FAILED]..."
```

---
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
