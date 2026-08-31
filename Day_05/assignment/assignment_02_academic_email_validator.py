"""
Assignment 2: Academic Email Validator

Scenario:
Validate user registration submissions so only academic emails ending in `.edu` or `.res.in` are registered.

Problem Description:
Write `validate_academic_email(email)`:
- Uses RegEx with boundary markers `^` and `$`.
- Username: Lowercase letters, numbers, dots, underscores (at least 1 char).
- Separator: Exactly one `@`.
- Domain: Lowercase letters, numbers, dots, hyphens.
- Suffix: Must end with either `.edu` or `.res.in`.
- Returns True if valid, False otherwise.
"""

import re

def validate_academic_email(email: str) -> bool:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    print(validate_academic_email("arham.khan@cdac.res.in"))  # Expected: True
    print(validate_academic_email("lisa_stud12@mit.edu"))      # Expected: True
    print(validate_academic_email("vinod@gmail.com"))          # Expected: False
    print(validate_academic_email("ALICE@college.edu"))        # Expected: False
    print(validate_academic_email("bob@mit.edu.com"))          # Expected: False

