"""
Exercise 2: Fibonacci Sequence Generator

Write a Python script to print the first $N$ terms of the Fibonacci sequence, where $N$ is provided by the user.
* **Fibonacci sequence**: $0, 1, 1, 2, 3, 5, 8, 13, 21, \dots$
* **Sample Input**: `N = 6`
* **Sample Output**: `0, 1, 1, 2, 3, 5`
"""

def solve():
    n = int(input("Enter the number: "))
    a,b=0,1
    for i in range(n):
        print(a, end = ", " if i < n-1 else " ")
        
        temp = a+b
        a = b
        b = temp

if __name__ == "__main__":
    solve()
