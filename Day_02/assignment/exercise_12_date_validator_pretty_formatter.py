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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
