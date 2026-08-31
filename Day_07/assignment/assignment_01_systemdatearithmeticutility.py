"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
