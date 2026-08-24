# Day 04 Practice Assignments: Dictionaries & Exception Handling

## Objective
Model key-value storage relations and implement try-except blocks to catch runtime division and typing issues.

---

### Exercise 1: Paragraph Word Counter
Write a program that counts the occurrence of each word in a paragraph entered by the user. Convert all words to lowercase and strip out punctuation.
* **Sample Input**: `"Python is fun. Python is easy to learn."`
* **Sample Output**:
  ```text
  python: 2
  is: 2
  fun: 1
  easy: 1
  ...
  ```

---

### Exercise 2: Dictionary Merger
Write a Python function to merge two dictionaries. If a key is present in both, sum their values.
* **Sample Input**: `d1 = {'a': 10, 'b': 20}`, `d2 = {'b': 30, 'c': 40}`
* **Sample Output**: `{'a': 10, 'b': 50, 'c': 40}`

---

### Exercise 3: Exception-safe Calculator
Write a function `safe_divide()` that prompts the user for two numbers and divides the first by the second.
* **Requirement**: Catch `ZeroDivisionError` (if divisor is 0) and `ValueError` (if inputs are non-numeric) and prompt appropriate messages. Keep requesting inputs in a loop until a valid division is successfully executed.

---

### Exercise 4: Dictionary Key Lookup Safety
Write a function `safe_lookup(dictionary, key, default_value)` that returns the value associated with the key if it exists in the dictionary, otherwise prints a warning and returns the default value without crashing with a `KeyError`.

---

### Exercise 5: Dictionary Inverter
Write a function to swap keys and values in a dictionary. Assume all values are unique.
* **Sample Input**: `{'A': 1, 'B': 2}`
* **Sample Output**: `{1: 'A', 2: 'B'}`

---

### Exercise 6: Nested Dictionary Parser
Given a nested dictionary structure, write a function that extracts a value using a list of keys representing a path. Return `"Key Not Found"` if any key along the path is invalid.
* **Sample Input**: `data = {'a': {'b': {'c': 99}}}`, `keys = ['a', 'b', 'c']`
* **Sample Output**: `99`

---

### Exercise 7: Index and Key Exception Catcher
Write a block of code that accesses a list index and dictionary key based on user input. Wrap the code in exception clauses to handle both `IndexError` and `KeyError` separately, outputting distinct diagnostic instructions for each.

---

### Exercise 8: Age Verification Custom Exception
Create a custom Exception class `NegativeAgeError`. Write a function that accepts an integer age. If the input age is negative, raise a `NegativeAgeError`. Catch it using a `try-except` block and display the custom message.
