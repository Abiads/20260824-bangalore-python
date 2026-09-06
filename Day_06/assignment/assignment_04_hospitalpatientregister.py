"""
### Assignment 4: Hospital Patient Register
#### Scenario
A hospital patient ledger automatically tracks patient counts and assigns sequentially numbered keys. It also validates input dates to prevent registration crashes.

#### Problem Description
Create a class named `Patient` that satisfies the following:
1. **Class-level Variables**:
   - `_patient_counter` (integer, initialized to `0`): Tracks the total count of patient instances created.
2. **Static Method `validate_dob_format(dob_str)`**:
   - Uses a Regular Expression pattern to check if the date of birth matches the format `"YYYY-MM-DD"` exactly (4 digits, a hyphen, 2 digits, a hyphen, 2 digits).
   - Returns `True` if correct, and `False` otherwise.
3. **Constructor (`__init__`)**:
   - Accepts parameters: `name` (string) and `dob` (string, representation of date of birth).
   - First, calls `Patient.validate_dob_format(dob)`. If it returns `False`, raise a `ValueError` with the message: `"Invalid date of birth format: '<dob>'. Expected YYYY-MM-DD."`
   - If validation passes, increments the class variable `_patient_counter` by `1`.
   - Assigns a unique `patient_id` as a string: `"PAT-"` followed by the value of `1000 + _patient_counter` (e.g., `"PAT-1001"`, `"PAT-1002"`).
   - Stores `name` and `dob` as instance variables.
4. **Class Method `get_total_patients()`**:
   - Returns the value of `_patient_counter`.

#### Example Walkthrough
```python
# 1. Valid Registration
p1 = Patient("Arham Khan", "1999-05-15")
print(p1.patient_id)  # Output: PAT-1001

# 2. Invalid DOB registration (throws ValueError)
try:
    p2 = Patient("Lisa", "12/08/1998")
except ValueError as e:
    print(e)  # Output: Invalid date of birth format: '12/08/1998'. Expected YYYY-MM-DD.

print(Patient.get_total_patients())  # Output: 1
```
"""

import re


class Patient:
    _patient_counter: int = 0

    @staticmethod
    def validate_dob_format(dob_str: str) -> bool:
        """Validates if date of birth string matches YYYY-MM-DD format using regex."""
        if not isinstance(dob_str, str):
            return False
        return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", dob_str))

    def __init__(self, name: str, dob: str):
        if not Patient.validate_dob_format(dob):
            raise ValueError(f"Invalid date of birth format: '{dob}'. Expected YYYY-MM-DD.")

        Patient._patient_counter += 1
        self.patient_id = f"PAT-{1000 + Patient._patient_counter}"
        self.name = name
        self.dob = dob

    @classmethod
    def get_total_patients(cls) -> int:
        """Returns the total number of patient instances created."""
        return cls._patient_counter


if __name__ == "__main__":
    # 1. Valid Registration
    p1 = Patient("Arham Khan", "1999-05-15")
    print(p1.patient_id)  # Output: PAT-1001

    # 2. Invalid DOB registration (throws ValueError)
    try:
        p2 = Patient("Lisa", "12/08/1998")
    except ValueError as e:
        print(e)  # Output: Invalid date of birth format: '12/08/1998'. Expected YYYY-MM-DD.

    print(Patient.get_total_patients())  # Output: 1
