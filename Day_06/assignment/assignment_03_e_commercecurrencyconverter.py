"""
### Assignment 3: E-Commerce Currency Converter
#### Scenario
An online store represents transaction totals as structured objects containing currency labels. To prevent logic errors, the system must not add different currencies directly and should print descriptive labels.

#### Problem Description
Create a class named `PriceAmount` with the following requirements:
1. **Constructor (`__init__`)**: Accepts `value` (float) and `currency` (string). Standardize the `currency` string value by converting it to uppercase.
2. **Dunder Methods for String Representation**:
   - **`__str__`**: Returns a string formatted as `"<currency> <value>"` with the value rounded to **2 decimal places** (e.g., `"USD 19.99"`).
   - **`__repr__`**: Returns a detailed programmer representation: `"PriceAmount(value=<value>, currency='<currency>')"` (value rounded to 2 decimal places).
3. **Operator Overloading**:
   - **`__add__(self, other)`**:
     - Check if `other` is an instance of `PriceAmount` and has the **same** currency value.
     - If the currency values do not match, raise a `ValueError` with the message:
       `"Cannot add price amounts with different currencies: '<currency1>' and '<currency2>'."`
     - If valid, return a **new** `PriceAmount` instance with the summed value and the same currency.
   - **`__eq__(self, other)`**:
     - Returns `True` if `other` is an instance of `PriceAmount`, has the same currency, and the values are identical. Otherwise, returns `False`.

#### Example Walkthrough
```python
p1 = PriceAmount(19.99, "usd")
p2 = PriceAmount(10.01, "USD")
p3 = PriceAmount(15.00, "EUR")

print(str(p1))      # Output: USD 19.99
print(repr(p1))     # Output: PriceAmount(value=19.99, currency='USD')

total = p1 + p2
print(str(total))   # Output: USD 30.00

print(p1 == PriceAmount(19.99, "USD")) # Output: True

try:
    bad_addition = p1 + p3
except ValueError as e:
    print(e)  # Output: Cannot add price amounts with different currencies: 'USD' and 'EUR'.
```

---
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
