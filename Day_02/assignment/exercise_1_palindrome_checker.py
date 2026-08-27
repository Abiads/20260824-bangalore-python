"""
Exercise 1: Palindrome Checker

Write a function that checks whether a given string is a palindrome (reads the same forward and backward, ignoring spaces and letter case).
* **Sample Input**: `"A man a plan a canal Panama"`
* **Sample Output**: `True`
"""
def solve():
    a = input("Enter the string: ")

    a = ''.join(char.lower() for char in a if char.isalnum())
    b = a[::-1]

    if a == b:
        print("True")
    else:
        print("False")

    


if __name__ == "__main__":
    solve()
