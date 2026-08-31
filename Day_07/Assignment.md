# Day 7 Practice Assignments: Standard Libs, Debugging & Databases

## Objective
Utilize standard datetime operations, parse JSON configuration trees safely using `pathlib` checks, configure dual handler loggers, establish and query SQLite databases using parameterized commands, and manage rollback database transactions.

---

## Easy Assignments

### Assignment 1: System Date Arithmetic Utility
#### Scenario
You are writing a cleanup utility for system backups. The script must calculate file retention expiration dates and output warning flags when a backup is nearing its expiration date.

#### Problem Description
Write a function `calculate_backup_dates(start_date_str, retention_days)` that performs date arithmetic:
1. `start_date_str` is a string representing the backup base date. Format: `"YYYY-MM-DD"`.
2. `retention_days` is an integer representing the retention duration in days.
3. **Validation**: Attempt to parse `start_date_str` into a `datetime.date` object using `datetime.strptime()`. If the string doesn't match the format, catch the `ValueError`, print the warning: `"Invalid date format. Expected YYYY-MM-DD."`, and return `None`.
4. **Calculations**:
   - `expiry_date`: Calculate the date exactly `retention_days` **after** the parsed start date.
   - `warning_date`: Calculate the warning date exactly **3 days before** the calculated `expiry_date`.
5. **Formatting**: Format the calculated dates back to string representations in the exact format `"DD-Mon-YYYY"` (e.g. `"15-May-2026"`, `"08-Sep-2026"`).
6. **Return**: A dictionary containing:
   `{"expiry_date": <expiry_date_str>, "warning_date": <warning_date_str>}`.

#### Example Walkthrough
```python
# 1. Valid Input
dates = calculate_backup_dates("2026-08-28", 14)
print(dates)
# Output: {'expiry_date': '11-Sep-2026', 'warning_date': '08-Sep-2026'}

# 2. Invalid Input
invalid_dates = calculate_backup_dates("28/08/2026", 10)
# Console output: Invalid date format. Expected YYYY-MM-DD.
print(invalid_dates) # Output: None
```

---

### Assignment 2: JSON Configuration Validator
#### Scenario
An AI web engine boots configurations from a JSON file. If the file is missing, empty, or contains corrupt syntax, the system crashes. You need to write a safe configuration loading module that provides default values in case of errors.

#### Problem Description
Write a function `load_config_safely(file_path_str)`:
1. Convert `file_path_str` to a path using `pathlib.Path`.
2. **Check Existence**: Check if the file exists and is indeed a file. If the file is missing, print: `"Error: Config file not found."` and return the default fallback configuration:
   `{"status": "default", "port": 8080}`.
3. **Check Size**: Check if the file size is 0 bytes (empty). If empty, print: `"Error: Config file is empty."` and return the default fallback dictionary.
4. **JSON Parsing**: Read the file contents. Attempt to deserialize the contents as JSON using `json.loads()` or `json.load()`.
   - If the file contains invalid JSON structures (throws `json.JSONDecodeError`), catch the exception, print: `"Error: Invalid JSON syntax."`, and return the default fallback dictionary.
5. If the file parses successfully, return the loaded configuration dictionary.

#### Example Walkthrough
```python
from pathlib import Path

# Setup files for testing
Path("corrupt.json").write_text("invalid data string")
Path("empty.json").write_text("")

# Test Cases
print(load_config_safely("missing.json"))
# Output: Error: Config file not found.
# Returns: {"status": "default", "port": 8080}

print(load_config_safely("empty.json"))
# Output: Error: Config file is empty.
# Returns: {"status": "default", "port": 8080}

print(load_config_safely("corrupt.json"))
# Output: Error: Invalid JSON syntax.
# Returns: {"status": "default", "port": 8080}
```

---

## Medium Assignments

### Assignment 3: Corporate Event Logger
#### Scenario
You are developing a secure authentication firewall. The login gateway must log authorization attempts. File logs must track serious threats with detailed timestamps, while console channels show warnings in real time.

#### Problem Description
1. Write a function `configure_system_logger(log_file_path)`:
   - Configure a logger named `"CDAC_Security"` and set its baseline capture level to `logging.DEBUG`.
   - Clear any existing handlers on the logger to prevent duplicate outputs.
   - Create two log destination handlers:
     - **File Handler (`logging.FileHandler`)**: Writes logs to `log_file_path`. Set its logging threshold level to `logging.WARNING`.
     - **Console Handler (`logging.StreamHandler`)**: Outputs logs to standard console. Set its logging threshold level to `logging.INFO`.
   - Create and link formatters for both handlers:
     - The File Handler log format must be: `"[%(asctime)s] [%(levelname)s] - %(message)s"`
     - The Console Handler log format must be: `"[CONSOLE] %(levelname)s: %(message)s"`
   - Add both handlers to the `"CDAC_Security"` logger and return it.
2. Write a function `process_login_attempt(logger, username, is_success, ip_address)`:
   - If `is_success` is `True`, write an `INFO` message: `"User '<username>' successfully logged in from IP <ip_address>."`
   - If `is_success` is `False`:
     - If the username is `"admin"`, this indicates a critical threat. Write an `ERROR` message: `"CRITICAL: Unauthorized admin access attempt from IP <ip_address>!"`
     - For any other username, write a `WARNING` message: `"Failed login attempt for user '<username>' from IP <ip_address>."`

#### Expected Output
* Calling `process_login_attempt(logger, "arham", True, "192.168.1.100")` prints to console:
  `[CONSOLE] INFO: User 'arham' successfully logged in from IP 192.168.1.100.` (Not written to file).
* Calling `process_login_attempt(logger, "lisa", False, "10.0.0.5")` prints to console:
  `[CONSOLE] WARNING: Failed login attempt for user 'lisa' from IP 10.0.0.5.`
  And writes to log file: `[<timestamp>] [WARNING] - Failed login attempt for user 'lisa' from IP 10.0.0.5.`
* Calling `process_login_attempt(logger, "admin", False, "8.8.8.8")` prints to console:
  `[CONSOLE] ERROR: CRITICAL: Unauthorized admin access attempt from IP 8.8.8.8!`
  And writes to log file: `[<timestamp>] [ERROR] - CRITICAL: Unauthorized admin access attempt from IP 8.8.8.8!`

---

### Assignment 4: Relational Employee Database CRUD Registry
#### Scenario
You are developing a local employee database registry tool for HR. The application needs CRUD (Create, Read, Update, Delete) methods and must use parameterized parameters to prevent SQL injection.

#### Problem Description
Create a class named `EmployeeDBRegistry` that connects to a local SQLite database:
1. **Constructor (`__init__`)**:
   - Accepts a database file name (string, e.g. `"hr.db"`).
   - Establishes a connection to the database.
   - Creates a table named `employees` if it does not exist, with the following columns:
     - `emp_id` (INTEGER PRIMARY KEY AUTOINCREMENT)
     - `name` (TEXT NOT NULL)
     - `department` (TEXT)
     - `salary` (REAL)
2. **Methods**:
   - **`add_employee(name, department, salary)`**:
     - Inserts a new employee record using parameterized SQL execution (using `?` placeholders).
     - Commits the transaction.
     - Returns the newly created auto-incremented `emp_id` (using `cursor.lastrowid`).
   - **`get_employees_by_department(department)`**:
     - Queries the database for all records matching `department`.
     - Returns a list of tuples containing all columns of the matching employees.
   - **`update_salary(emp_id, new_salary)`**:
     - Updates the salary column of the record matching `emp_id`.
     - Commits the change.
     - Returns `True` if a record was modified, and `False` if no employee matching `emp_id` was found in the database.
   - **`delete_employee(emp_id)`**:
     - Deletes the record matching `emp_id`.
     - Commits the change.
3. Ensure you close cursors and database connections safely.

#### Example Walkthrough
```python
db = EmployeeDBRegistry("hr.db")

# 1. Add employees
id1 = db.add_employee("Alice", "Engineering", 75000.0)
id2 = db.add_employee("Bob", "HR", 50000.0)

# 2. Query department
eng_staff = db.get_employees_by_department("Engineering")
print(eng_staff) # Output: [(1, 'Alice', 'Engineering', 75000.0)]

# 3. Update salary
success = db.update_salary(id1, 80000.0)
print(success) # Output: True

# 4. Attempt update on non-existent ID
print(db.update_salary(999, 100.0)) # Output: False
```

---

## Difficult Assignments

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

---

### Assignment 6: File System Space Monitor & Database Auditing Daemon
#### Scenario
You are writing a system audit utility that scans disk directories, tracks storage space allocation, and logs records to an SQLite database for monitoring.

#### Problem Description
Write a function `audit_directory_space(directory_path_str, db_name, log_path)`:
1. **Directory Scan**:
   - Check if `directory_path_str` represents a valid directory using `pathlib.Path`. If it does not exist or is not a directory, raise `FileNotFoundError` with message: `"Target directory not found."`
   - Recursively scan all files inside the directory (use `Path.glob("**/*")` or `Path.rglob("*")`).
   - Calculate:
     - `file_count`: The total count of file objects found.
     - `total_bytes`: The sum of all file sizes in bytes.
     - `largest_file_name`: The filename (basename string) of the largest file.
     - `largest_file_bytes`: The size of the largest file in bytes.
     - (Note: Ignore directory objects during scanning, only count files). If the directory has no files, set the largest filename to `""` and largest file size to `0`.
2. **Logging**:
   - Write a log entry to the log file at `log_path` (level `INFO`):
     `"Audited directory '<dir_path>': <file_count> files, <total_bytes> bytes."`
3. **Database Audit Entry**:
   - Connect to database `db_name` and create a table `dir_audit` if it does not exist:
     - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
     - `scan_time` (TEXT, ISO format timestamp)
     - `dir_path` (TEXT)
     - `file_count` (INTEGER)
     - `total_bytes` (INTEGER)
     - `largest_file_name` (TEXT)
     - `largest_file_bytes` (INTEGER)
   - Insert a new record containing the audit values using a parameterized query (`?` placeholders).
   - For `scan_time`, use the current system time in ISO format: `datetime.now().isoformat()`.
   - Commit the transaction and close SQLite resources.

#### Example Walkthrough
```python
# Assuming a directory structure:
# my_data/
#  |- file1.txt (50 bytes)
#  |- docs/
#      |- doc1.pdf (500 bytes)

audit_directory_space("my_data", "monitoring.db", "system.log")
# system.log writes: "Audited directory 'my_data': 2 files, 550 bytes."
# database inserts record: ("2026-08-28T...", "my_data", 2, 550, "doc1.pdf", 500)
```
