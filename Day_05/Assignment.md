# Day 05 Practice Assignments: Functions, Scopes & RegEx

## Objective
Design modular functions with varied arguments, write custom scopes, and perform text validations using regular expressions.

---

### Exercise 1: Combinations Calculator (nCr)
Write a program that calculates combinations ($^nC_r = \frac{n!}{r!(n-r)!}$) using a helper function to calculate factorials.
* **Requirements**: Implement separate functions for `factorial(x)` and `combinations(n, r)`. Add checks to ensure $n \ge r$.

---

### Exercise 2: Password Validator using RegEx
Write a function `validate_password(password)` that uses Regular Expressions to check the strength of a user-supplied password.
* **Validation Criteria**:
  1. Must contain at least 8 characters.
  2. Must contain at least one uppercase letter.
  3. Must contain at least one lowercase letter.
  4. Must contain at least one number.
  5. Must contain at least one special character (e.g., `@`, `#`, `$`, `&`).

---

### Exercise 3: Lambda Map/Filter Exercises
Given a list of integers: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
1. Use `filter()` and a lambda function to extract all odd numbers.
2. Use `map()` and a lambda function to double every number in the list.

---

### Exercise 4: Recursive Power Function
Write a recursive function `power(base, exp)` that calculates $base^{exp}$ without using Python's base exponentiation operator `**` or `math.pow()`.
* **Sample Input**: `base = 2, exp = 5`
* **Sample Output**: `32`

---

### Exercise 5: Function Execution Logger Decorator
Create a decorator function `log_arguments` that wraps any function and prints out the function's positional and keyword arguments every time it is executed.

---

### Exercise 6: Email Scraper RegEx
Write a Python program using the `re` module that parses a block of text and extracts all valid email addresses.
* **Sample Text**: `"Contact us at info@cdac.in or sales_dept@acts.com for help."`
* **Sample Output**: `['info@cdac.in', 'sales_dept@acts.com']`

---

### Exercise 7: Phone Number Formatter
Write a RegEx validation script that checks if a user input phone number matches a 10-digit format (like `123-456-7890` or `1234567890`) and normalizes it to `(123) 456-7890`.

---

### Exercise 8: Variable Scope Shadow Demo
Create a script containing a global variable. Define nested functions that modify variables using the `global` and `nonlocal` keywords, demonstrating variable shadowing and boundary scopes.
