"""
Exercise 3: Prime Number Checker

Write a program that checks whether a positive integer entered by the user is a prime number.
* **Logic**: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
* **Sample Input**: `17`
* **Sample Output**: `17 is a prime number.`
"""

def solve():

    num = int(input("Enter a positive integer: "))
    a = num // 2

    if num <= 0:
        print("Retry")
    else:
        for i in range(2, a+1):
            if num % i == 0:
                print(f'{num} is not a prime number as its divisible by {i}')
                break
        else:
            print(f'{num} is a prime number')
                

if __name__ == "__main__":
    solve()
