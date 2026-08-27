"""
Exercise 12: Date Validator & Pretty Formatter

Write a program that prompts the user to enter a date string in the format `"DD/MM/YYYY"`. 

> [!WARNING]
> Do not use any built-in date/time library functions (such as the `datetime` or `time` modules) to format or validate the dates. You must parse and split the string manually, and use a custom tuple of month names for the pretty output if needed.

Your program must:
1. Verify if the date is valid. To be valid:
   * The month must be between `1` and `12` inclusive.
   * The day must be valid for that specific month (e.g., April, June, September, November have 30 days; others have 31 days).
   * For February, the day must be at most `29` in a leap year (divisible by 4, except for centuries not divisible by 400) and at most `28` in standard years.
2. If the date is valid, use a tuple of month names `("January", "February", ...)` to format and print the date in a long-form readable layout: `"MonthName DD, YYYY"`.
3. If the date is invalid, print `"Invalid Date"`.

* **Sample Input**: `"26/08/2026"`
* **Sample Output**: `"August 26, 2026"`
* **Sample Input**: `"29/02/2026"`  (2026 is not a leap year)
* **Sample Output**: `"Invalid Date"`
* **Sample Input**: `"31/04/2026"`  (April only has 30 days)
* **Sample Output**: `"Invalid Date"`

--------------------------------------------------

💡 Useful Functions & Data Structures (Note: Do NOT use `datetime` module):
1. `str.split('/')` -> Splits `"DD/MM/YYYY"` into `[day_str, month_str, year_str]`.
2. `int(str)` -> Converts string values into integers for arithmetic checks.
3. Month Names Tuple:
   `MONTH_NAMES = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")`
4. Leap Year Logic:
   `is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`
5. Days per Month Table:
   `days_in_month = (31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)`

📋 Step-by-Step Logic:
1. Split input string by `/`. If it doesn't contain 3 parts, print `"Invalid Date"`.
2. Convert parts to `day`, `month`, `year`.
3. Check if `1 <= month <= 12`.
4. Determine max days for that month using leap year rule for Feb.
5. Check if `1 <= day <= max_days_for_month`.
6. If valid, format as `f"{MONTH_NAMES[month - 1]} {day:02d}, {year}"` and print.
7. If invalid at any step, print `"Invalid Date"`.
"""

def solve():
    # TODO: Implement your solution following the hints above
    pass

if __name__ == "__main__":
    solve()
