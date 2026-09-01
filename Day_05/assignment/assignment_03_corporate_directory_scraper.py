"""
### Assignment 3: Corporate Directory Search & Scraper
#### Scenario
You are writing a parser to extract formatted employee phone records from unstructured text files. Employee phone numbers are formatted in multiple ways across the directory.

#### Problem Description
Write a function `scrape_directory_phones(directory_text)` that extracts phone records from text and returns a structured list of dictionaries.
1. The function must detect phone numbers matching any of the following three formats:
   - `AAA-PPP-LLLL` (e.g., `123-456-7890`)
   - `(AAA) PPP-LLLL` (e.g., `(123) 456-7890`)
   - `AAAPPPLLLL` (10 consecutive digits, e.g., `1234567890`)
   where `AAA` represents the area code (3 digits), `PPP` represents the prefix (3 digits), and `LLLL` represents the line number (4 digits).
2. Design a single compiled RegEx pattern to parse all three formats using **capture groups**.
3. For each match found in `directory_text`, build a dictionary with the following keys:
   - `"area_code"`: String containing the extracted 3 area code digits.
   - `"prefix"`: String containing the extracted 3 prefix digits.
   - `"line_number"`: String containing the extracted 4 line number digits.
   - `"formatted"`: A normalized phone string in the format `"(AAA) PPP-LLLL"`.
4. Return a list of these dictionaries. If no phone numbers are found, return an empty list.

#### Sample Input
```python
directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
```

#### Expected Output
```python
[
    {"area_code": "123", "prefix": "456", "line_number": "7890", "formatted": "(123) 456-7890"},
    {"area_code": "987", "prefix": "654", "line_number": "3210", "formatted": "(987) 654-3210"},
    {"area_code": "555", "prefix": "888", "line_number": "1234", "formatted": "(555) 888-1234"}
]
```
"""

import re

def scrape_directory_phones(directory_text: str) -> list[dict]:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
    results = scrape_directory_phones(directory)
    print("Scraped Phones:", results)

