"""
Exercise 4: Odd or Even Checker

Write a program that prompts the user for an integer and prints whether it is even or odd.
* **Sample Input**: `7`
* **Sample Output**: `7 is an Odd number.`
"""

def solve():
    num = int(input("Enter value: "))

    if num < 0:
        print("Enter a positive value")
        return

    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')

if __name__ == "__main__":
    solve()
