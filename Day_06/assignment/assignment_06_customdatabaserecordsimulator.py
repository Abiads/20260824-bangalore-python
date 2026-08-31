"""
### Assignment 6: Custom Database Record Simulator
#### Scenario
You are developing a custom result set class to represent database queries. To make it behave like a native Python list, the object must support indexes, search lookups by name strings, iteration using custom iterator classes, and return database size.

#### Problem Description
1. Create a class named `DatabaseRecord`:
   - **Constructor (`__init__`)**: Accepts `record_id` (int) and `data` (dictionary).
   - **Dunder Methods**: Implement `__repr__` and `__str__` returning `"Record(id=<record_id>, data=<data>)"`.
2. Create a custom iterator class named `ResultSetIterator`:
   - **Constructor (`__init__`)**: Accepts `records_list` (list of `DatabaseRecord` instances). Initialize an index counter to `0`.
   - **Dunder Methods**:
     - `__iter__(self)`: Returns `self`.
     - `__next__(self)`: Yields the next `DatabaseRecord` in the list. If no records remain, raises `StopIteration`.
3. Create a class named `DatabaseResultSet`:
   - **Constructor (`__init__`)**: Accepts `records_list` (list of `DatabaseRecord` objects).
   - **Dunder Methods**:
     - **`__len__(self)`**: Returns the count of records in the result set.
     - **`__iter__(self)`**: Returns a new `ResultSetIterator` object initialized with `records_list`.
     - **`__getitem__(self, key)`**:
       - If `key` is an **integer**, return the `DatabaseRecord` at that index. If the index is out of bounds, let it raise a standard `IndexError`.
       - If `key` is a **string**, search the database records. Return the first `DatabaseRecord` object whose `data["name"]` matches the key string.
       - If the name string is not found, raise a custom exception named `RecordNotFoundError` (which you must define) with the message: `"Record with name '<name>' not found in database."`

#### Example Walkthrough
```python
# Setup records
r1 = DatabaseRecord(101, {"name": "Alice", "role": "Admin"})
r2 = DatabaseRecord(102, {"name": "Bob", "role": "User"})

results = DatabaseResultSet([r1, r2])

# 1. Length
print(len(results))  # Output: 2

# 2. Integer Indexing
print(results[0].data["role"])  # Output: Admin

# 3. String lookup
record = results["Bob"]
print(record.record_id)  # Output: 102

# 4. Iteration
for rec in results:
    print(rec.record_id)
# Output:
# 101
# 102

# 5. Missing key lookup
try:
    missing = results["Charlie"]
except RecordNotFoundError as e:
    print(e)  # Output: Record with name 'Charlie' not found in database.
```
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
