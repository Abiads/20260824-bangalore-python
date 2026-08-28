"""
Exercise 6: Shift Cipher Encrypter

Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher. It should shift each alphabetical character in the string by the specified shift number down the alphabet. Maintain uppercase and lowercase characters, and leave spaces or punctuation marks completely unchanged.

- **Sample Input**: (User inputs string `"Vinod"` and shift `3`)
- **Sample Output**: `"Ylqrg"`

--------------------------------------------------

💡 Useful Functions & Methods:
1. `ord(char)` -> Returns the integer ASCII value of a character.
   - Example: `ord('A')` -> `65`, `ord('a')` -> `97`
2. `chr(int)` -> Returns the character corresponding to an ASCII integer value.
   - Example: `chr(68)` -> `'D'`
3. `char.isupper()` / `char.islower()` -> Checks casing of character.
4. Modulo Arithmetic (`% 26`) -> Handles circular wrapping around alphabet (e.g. 'z' -> 'c'):
   - Uppercase: `chr((ord(c) - ord('A') + shift) % 26 + ord('A'))`
   - Lowercase: `chr((ord(c) - ord('a') + shift) % 26 + ord('a'))`

📋 Step-by-Step Logic:
1. Loop over each character in the input string.
2. If `char.isupper()`, apply uppercase formula.
3. If `char.islower()`, apply lowercase formula.
4. Otherwise (spaces, numbers, punctuation), leave character unchanged.
5. Combine characters and print the encrypted string.
"""

def solve():
    text = input("Enter a string: ")
    shift = int(input("Enter shift value: "))
    
    encrypted = ""
    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    
    print(encrypted)

if __name__ == "__main__":
    solve()
