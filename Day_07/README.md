# Day 7: Libraries, Debugging, Logging & Databases

Welcome to Day 7! Today we cover utility components required for production Python development:
1. **Python Standard Libraries**: Working with `os`, `sys`, `pathlib`, `datetime`, and `json`.
2. **Diagnostic Logging**: Configuring logging levels, handlers, and formats to record program telemetry.
3. **Interactive Debugging**: Using the Python Debugger (`pdb`) to trace variable states and execution lines.
4. **Relational Databases & DB-API**: Querying databases using `sqlite3` and utilizing parameterized inputs to prevent SQL injections.

---

## Part 1: Python Standard Libraries

Python is famous for its "batteries included" philosophy, providing a rich set of built-in modules.

### 1. Modern Paths with `pathlib`
The `pathlib` module offers an object-oriented approach to interacting with filesystem paths across different operating systems.

```python
from pathlib import Path

# Create a path object representing the current working directory
current_dir = Path(".")

# Joins paths using the slash operator (/)
target_file = current_dir / "Day_07" / "Assignment.md"

# Checking properties
print("Exists:", target_file.exists())
print("Is File:", target_file.is_file())
print("Filename:", target_file.name)
print("Parent directory:", target_file.parent)
```

### 2. Dates and Times with `datetime`
The `datetime` module handles date arithmetic and formatting.

```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
print("Now:", now.isoformat())

# Creating specific dates
target_date = datetime(2026, 8, 28)

# Date calculations using timedelta
two_weeks_later = target_date + timedelta(days=14)
print("Two Weeks Later:", two_weeks_later.strftime("%d-%b-%Y"))  # Output: 11-Sep-2026

# Parsing strings to datetime (strptime)
parsed_date = datetime.strptime("2026-08-28", "%Y-%m-%d")
print("Parsed Date Month:", parsed_date.month)
```

### 3. Serialization with `json`
The `json` module translates Python dictionaries and lists to JSON strings (serialization) and back (deserialization).

```python
import json

config = {"host": "localhost", "port": 8080, "debug": True}

# Serialize: Python dict -> JSON string
json_str = json.dumps(config, indent=4)
print(json_str)

# Deserialize: JSON string -> Python dict
parsed_config = json.loads(json_str)
print("Parsed port:", parsed_config["port"])
```

---

## Part 2: Diagnostic Logging

Instead of using `print()` statements—which output to standard console channels and are hard to filter—production applications use Python's built-in `logging` module.

### 1. Logging Levels
Log levels classify events based on severity:
* `DEBUG`: Detailed diagnostic information (primarily for troubleshooting).
* `INFO`: Confirmation that things are working as expected.
* `WARNING`: Indication that something unexpected happened (default threshold).
* `ERROR`: A serious issue that prevented a specific function from executing.
* `CRITICAL`: A severe error indicating the program itself may be unable to continue.

### 2. Configuring Handlers and Formatters
You can configure log messages to output to the console, write to files, or be formatted with metadata (timestamps, file names, line numbers).

```python
import logging

# Create a custom logger
logger = logging.getLogger("CDAC_App")
logger.setLevel(logging.DEBUG)  # Set the lowest threshold level to capture

# Create Handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

# Set thresholds for individual handlers
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.WARNING)

# Create Formatters and link them to handlers
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add Handlers to the Logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Logging statements
logger.info("Application starting up...")         # Console only
logger.warning("Configuration file is missing.")    # Both Console & File
logger.error("Failed to connect to database.")     # Both Console & File
```

---

## Part 3: Interactive Debugging (`pdb`)

The **Python Debugger (`pdb`)** provides an interactive debugging environment for Python programs. It allows you to pause execution, inspect variables, and step through code line by line.

### 1. Setting a Breakpoint
Insert `breakpoint()` (Python 3.7+) or `import pdb; pdb.set_trace()` at the exact line you wish to inspect.

```python
def calculate_average(grades):
    total = sum(grades)
    # Pause execution here
    breakpoint()
    count = len(grades)
    return total / count

calculate_average([85, 90, 78])
```

### 2. Common `pdb` Commands
When execution pauses, you will see a command prompt `(Pdb)`. Use these commands:
* **`n` (next)**: Executes the current line and stops at the next line in the current function.
* **`s` (step)**: Steps *into* the function called on the current line.
* **`c` (continue)**: Resumes standard execution until the next breakpoint.
* **`p <var>` (print)**: Evaluates and prints the value of variable `<var>`.
* **`l` (list)**: Shows the current line and surrounding lines of source code.
* **`w` (where)**: Prints the stack trace, showing the nested function calls leading to this line.
* **`q` (quit)**: Instantly aborts execution and exits the debugger.

---

## Part 4: Relational Databases (`sqlite3`)

Python interacts with SQL database backends using standard drivers compliant with **DB-API 2.0**. For lightweight local storage, Python includes `sqlite3`.

### 1. Parameterized Queries (Preventing SQL Injections)
> [!CAUTION]
> Never format or concatenate strings directly into an SQL statement (e.g., `f"INSERT INTO users VALUES ('{user}')"`). Doing so exposes your database to **SQL Injection Attacks**. Always use parameterized placeholder queries.

```python
import sqlite3

# 1. Establish connection to local database file
conn = sqlite3.connect("database.db")

# 2. Create a cursor object to execute SQL commands
cursor = conn.cursor()

# 3. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT
)
""")

# 4. Insert data using Parameterized SQL (represented by ? placeholders)
new_user = ("vinod_acts", "vinod@acts.com")
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", new_user)

# 5. Commit transaction changes
conn.commit()

# 6. Retrieve data
cursor.execute("SELECT * FROM users WHERE username = ?", ("vinod_acts",))
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# 7. Close resources safely
cursor.close()
conn.close()
```

---

## Practical Examples (Interactive & Runnable)

### Example 1: JSON File Configuration Loader
Demonstrates `pathlib`, `json`, and exception safety.

```python
import json
from pathlib import Path

def load_system_config(filepath):
    config_path = Path(filepath)
    
    # 1. Check file existence
    if not config_path.exists():
        print(f"Warning: '{filepath}' not found. Loading defaults.")
        return {"env": "prod", "cache": True, "limit": 100}
        
    # 2. Attempt to parse JSON contents
    try:
        with open(config_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError as err:
        print(f"Corrupted config JSON: {err}. Reverting to safety parameters.")
        return {"env": "error-state", "cache": False, "limit": 10}

# Write a dummy config file to test
Path("settings.json").write_text('{"env": "development", "cache": false, "limit": 50}')

# Load configuration
settings = load_system_config("settings.json")
print("Settings:", settings)
```

### Example 2: SQLite database Transaction with Rollback
Demonstrates transaction management with commit and rollback.

```python
import sqlite3

def init_bank_db():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts (acc_num TEXT PRIMARY KEY, balance REAL)")
    cursor.execute("INSERT OR REPLACE INTO accounts VALUES ('ACC01', 500.0)")
    cursor.execute("INSERT OR REPLACE INTO accounts VALUES ('ACC02', 200.0)")
    conn.commit()
    conn.close()

def transfer_funds(sender, receiver, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    
    try:
        # Deduct from sender
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE acc_num = ?", (amount, sender))
        
        # Verify sender balance isn't negative (simulate business logic error)
        cursor.execute("SELECT balance FROM accounts WHERE acc_num = ?", (sender,))
        sender_balance = cursor.fetchone()[0]
        if sender_balance < 0:
            raise ValueError(f"Insufficient funds in sender account: {sender}.")
            
        # Add to receiver
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE acc_num = ?", (amount, receiver))
        
    except Exception as e:
        # Roll back all database operations executed in the try block
        print(f"Transaction failed: {e}. Rolling back changes.")
        conn.rollback()
    else:
        # Commit changes if all operations succeeded
        print("Transaction successful! Committing balances.")
        conn.commit()
    finally:
        conn.close()

# Run Setup and Execution
init_bank_db()
transfer_funds("ACC01", "ACC02", 150.0)  # Succeeded
transfer_funds("ACC01", "ACC02", 1000.0) # Fails and rolls back
```
