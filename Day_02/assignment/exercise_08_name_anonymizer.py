"""
Exercise 8: Name Anonymizer

Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. The output should print the initials of the first and middle names followed by the full last name. If the name consists of only a single word, print it as-is.

- **Sample Input**: `"Vinod Kumar Kayartaya"`
- **Sample Output**: `"V. K. Kayartaya"`
- **Sample Input**: `"Bangalore"`
- **Sample Output**: `"Bangalore"`

--------------------------------------------------

💡 Useful Functions & Methods:
1. `str.split()` -> Splits the full name into a list of name parts.
   - Example: `"Vinod Kumar Kayartaya".split()` -> `['Vinod', 'Kumar', 'Kayartaya']`
2. List Slicing:
   - `parts[:-1]` -> All elements except the last one (first and middle names).
   - `parts[-1]` -> The last name.
3. String Indexing & Formatting:
   - `part[0].upper() + "."` -> Converts name part to initial.
   - `' '.join(...)` -> Joins the formatted parts with spaces.

📋 Step-by-Step Logic:
1. `parts = name.split()`
2. If `len(parts) <= 1`, print the name as-is.
3. If `len(parts) > 1`, convert each part in `parts[:-1]` into initial `f"{p[0].upper()}."`.
4. Append full `parts[-1]` and join with spaces.
"""

def solve():
    name = input("Enter a full name: ")
    parts = name.split()
    
    if len(parts) <= 1:
        print(name)
    else:
        initials = []
        for part in parts[:-1]:
            initials.append(f"{part[0].upper()}.")
        initials.append(parts[-1])
        result = " ".join(initials)
        print(result)

if __name__ == "__main__":
    solve()
