"""
Exercise 5: Basic Operator Calculator

Create a program that takes two numbers and a math operator (`+`, `-`, `*`, `/`) from the user, performs the corresponding calculation, and prints the result.
* **Sample Input**: `num1=15`, `num2=3`, `operator='/'`
* **Sample Output**: `Result: 5.0`
"""

def solve():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    choice = int(input("Choose 1,2,3,4 for operations (`+`, `-`, `*`, `/`) respectively: "))

    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2 )
    else: 
        print("Invalid Choice")

if __name__ == "__main__":
    solve()
