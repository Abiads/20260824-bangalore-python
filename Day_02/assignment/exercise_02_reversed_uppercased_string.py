"""
Exercise 2: Reversed Uppercased String

Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

- **Sample Input**: `"Bangalore"`
- **Sample Output**: `"EROLAGNAB"`

--------------------------------------------------

💡 Useful Functions & Methods:
1. Extended Slicing `string[start:stop:step]` -> Reverses a sequence when step is `-1`.
   - Syntax: `text[::-1]`
   - Example: `"Bangalore"[::-1]` -> `"erolagnaB"`
2. `str.upper()` -> Returns a copy of the string converted to uppercase.
   - Example: `"erolagnaB".upper()` -> `"EROLAGNAB"`

📋 Step-by-Step Logic:
1. Get the string from the user using `input()`.
2. Reverse the string using sequence slicing `[::-1]`.
3. Convert to uppercase using `.upper()`.
4. Print the final result.
"""

def solve():
    inp = input("Enter a string: ")
    reversed_string = inp[::-1]
    result = reversed_string.upper()
    print(result)

if __name__ == "__main__":
    solve()
