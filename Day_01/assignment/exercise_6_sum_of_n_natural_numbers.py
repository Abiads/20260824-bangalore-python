"""
Exercise 6: Sum of N Natural Numbers

Write a script that accepts a positive integer $N$ from the user and calculates the sum of all natural numbers up to $N$.
* **Formula**: $\sum_{i=1}^{N} i = \frac{N(N+1)}{2}$
* **Sample Input**: `N = 10`
* **Sample Output**: `Sum: 55`
"""

def solve():
    num = int(input("Enter a number: "))

    n = num*(num + 1)
    a = n/2

    print(int(a))

if __name__ == "__main__":
    solve()
