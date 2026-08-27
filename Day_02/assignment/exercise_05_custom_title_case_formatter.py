"""
Exercise 5: Custom Title Case Formatter

Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters). **Do not use Python's built-in `.title()` method.**

- **Sample Input**: `"WELCOME TO BANGALORE CITY"`
- **Sample Output**: `"Welcome To Bangalore City"`

--------------------------------------------------

💡 Useful Functions & Methods (Note: Do NOT use `.title()`):
1. `str.split()` -> Splits the sentence into individual words.
2. String Slicing & Case Methods:
   - `word[0].upper()` -> Capitalizes the first character.
   - `word[1:].lower()` -> Lowercases the rest of the word.
   - Combined: `word[0].upper() + word[1:].lower()`
3. `str.join(iterable)` -> Joins list of words into a single string separated by space.
   - Example: `" ".join(capitalized_words)`

📋 Step-by-Step Logic:
1. Split sentence into words using `words = text.split()`.
2. For each word, form capitalized word: `w[0].upper() + w[1:].lower()` (handle single-char words safely: `w.capitalize()` or slicing).
3. Join the converted list using `' '.join(...)` and print.
"""

def solve():
    # TODO: Implement your solution following the hints above
    pass

if __name__ == "__main__":
    solve()
