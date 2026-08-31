"""
Assignment 3: Corporate Directory Search & Scraper

Scenario:
Extract structured phone records from unstructured text files.

Problem Description:
Write `scrape_directory_phones(directory_text)`:
- Detects phone formats: `AAA-PPP-LLLL`, `(AAA) PPP-LLLL`, `AAAPPPLLLL`.
- Uses a single compiled RegEx with capture groups for area_code, prefix, line_number.
- Returns a list of dicts:
  `[{"area_code": "...", "prefix": "...", "line_number": "...", "formatted": "(AAA) PPP-LLLL"}, ...]`
"""

import re

def scrape_directory_phones(directory_text: str) -> list[dict]:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
    results = scrape_directory_phones(directory)
    print("Scraped Phones:", results)

