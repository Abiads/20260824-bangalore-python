"""
Exercise 7: Multiplication Table Generator

Write a program that takes an integer from the user and prints its multiplication table from 1 to 10.
* **Sample Input**: `5`
* **Sample Output**:
  ```text
  5 x 1 = 5
  5 x 2 = 10
  ...
  5 x 10 = 50
  ```
"""

def solve():
    a = int(input("Enter a value: "))

    for i in range(1, 11):
        print(f'{a} x {i} = ', a*i)

if __name__ == "__main__":
    solve()
