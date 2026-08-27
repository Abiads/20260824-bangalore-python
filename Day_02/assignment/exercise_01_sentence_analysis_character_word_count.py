"""
Exercise 1: Sentence Analysis (Character & Word Count)

Write a Python program that prompts the user to enter a sentence. The program must count and display:

1. The total number of characters (including spaces and punctuation).
2. The total number of words.

- **Sample Input**: `"Learning Python is fun!"`
- **Sample Output**:
  ```text
  Total Characters: 23
  Total Words: 4
  ```

--------------------------------------------------

💡 Useful Functions & Methods:
1. `input(prompt)` -> Reads a string from standard input.
2. `len(sequence)` -> Returns the total length / character count of the string.
   - Example: `len("Hello World")` -> `11`
3. `str.split(sep=None)` -> Splits a string by whitespace into a list of words.
   - Example: `"Learning Python is fun!".split()` -> `['Learning', 'Python', 'is', 'fun!']`
4. `len(list)` -> Returns the number of items in the list (i.e., word count).

📋 Step-by-Step Logic:
1. Prompt the user for input using `input("Enter a sentence: ")`.
2. Compute total characters using `len(sentence)`.
3. Compute total words using `len(sentence.split())`.
4. Print both results using formatted strings (f-strings).
"""

def solve():
   ...

if __name__ == "__main__":
    solve()
