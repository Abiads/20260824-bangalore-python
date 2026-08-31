"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
