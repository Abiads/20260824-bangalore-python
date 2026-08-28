"""
Exercise 9: Longest Palindromic Substring

Write a program that prompts the user to enter a text string and finds the longest substring within it that reads the same forward and backward. If there are multiple palindromic substrings of the same maximum length, print any one of them.

- **Sample Input**: `"babad"`
- **Sample Output**: `"bab"` (or `"aba"`)
- **Sample Input**: `"cbbd"`
- **Sample Output**: `"bb"`

--------------------------------------------------

💡 Useful Functions & Methods:
1. Palindrome Check with Slicing: `sub == sub[::-1]`
2. Nested loop substring generation:
   - Outer loop `i` from `0` to `len(s)`
   - Inner loop `j` from `i + 1` to `len(s) + 1`
   - Substring: `s[i:j]`
3. Tracking max palindrome:
   - Keep a variable `longest = ""`
   - If `sub == sub[::-1]` and `len(sub) > len(longest)`, update `longest = sub`.

📋 Step-by-Step Logic:
1. Initialize `longest_palindrome = ""`.
2. Generate all contiguous substrings using nested loops `for i in range(len(s)): for j in range(i+1, len(s)+1):`.
3. Check if substring `sub = s[i:j]` is a palindrome (`sub == sub[::-1]`).
4. If it is and `len(sub) > len(longest_palindrome)`, store it.
5. Print `longest_palindrome`.
"""

def solve():
    text = input("Enter a text string: ")
    longest_palindrome = ""
    
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    
    if longest_palindrome:
        print(longest_palindrome)
    else:
        print("")

if __name__ == "__main__":
    solve()
